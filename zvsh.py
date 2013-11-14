#!/usr/bin/python
import ConfigParser
import argparse
import os
import sys
import re
from tempfile import mkstemp
from subprocess import Popen, PIPE
import threading
import tarfile

env_match = re.compile(r'([_A-Z0-9]+)=(.*)')
temp_files = []


def create_manifest_channel(channels, chan_conf, file_name):
    temp_files.append(file_name)
    devname = '/dev/file%s' % len(temp_files)
    channels.append('Channel = %s,%s,3,0,%s,%s,%s,%s'
                    % (os.path.abspath(file_name), devname,
                       chan_conf['reads'], chan_conf['rbytes'],
                       chan_conf['writes'], chan_conf['wbytes']))
    return devname


def stdin_reader(output):
    if sys.stdin.isatty():
        try:
            for l in sys.stdin:
                output.write(l)
        except IOError:
            pass
    else:
        read_iter = iter(lambda: sys.stdin.read(65535), '')
        try:
            for l in read_iter:
                output.write(l)
        except IOError:
            pass
    output.close()


def spawn(func, **kwargs):
    t = threading.Thread(target=func, kwargs=kwargs)
    t.daemon = True
    t.start()
    return t


def cleanup(file_list):
    for f in file_list:
        if f:
            try:
                os.unlink(f)
            except OSError:
                pass


nvram_env = {}
nvram_fstab = {}
manifest_conf = {
    'Version': '20130611',
    'Memory': '419430400, 0',
    'Node': 1,
    'Timeout': 50
}
channel_conf = {
    'reads': str(1024 * 1024 * 1024 * 4),
    'rbytes': str(1024 * 1024 * 1024 * 4),
    'writes': str(1024 * 1024 * 1024 * 4),
    'wbytes': str(1024 * 1024 * 1024 * 4)
}
config = ConfigParser.ConfigParser()
config.optionxform = str
cfg_file = os.path.join(os.path.abspath(sys.argv[0]), 'zap.cfg')
config.read(cfg_file)
try:
    manifest_conf.update(dict(config.items('manifest')))
except ConfigParser.NoSectionError:
    pass
try:
    nvram_env.update(dict(config.items('env')))
except ConfigParser.NoSectionError:
    pass
try:
    nvram_fstab.update(dict(config.items('fstab')))
except ConfigParser.NoSectionError:
    pass
try:
    channel_conf.update(dict(config.items('limits')))
except ConfigParser.NoSectionError:
    pass
manifest_channels = [
    'Channel = /dev/stdin,/dev/stdin,0,0,%s,%s,0,0'
    % (channel_conf['reads'], channel_conf['rbytes']),
    'Channel = /dev/stdout,/dev/stdout,0,0,0,0,%s,%s'
    % (channel_conf['writes'], channel_conf['wbytes']),
    'Channel = /dev/stderr,/dev/stderr,0,0,0,0,%s,%s'
    % (channel_conf['writes'], channel_conf['wbytes'])
]
argparser = argparse.ArgumentParser()
argparser.add_argument('executable', help='ZeroVM executable')
argparser.add_argument('--zvm-image', help='ZeroVM image file(s)', action='append')
argparser.add_argument('--zvm-debug', help='Enable ZeroVM debug output into zvsh.log', action='store_true')
argparser.add_argument('--zvm-trace', help='Enable ZeroVM trace output into zvsh.trace.log', action='store_true')
argparser.add_argument('cmd_args', help='command line arguments', nargs=argparse.REMAINDER)
args = argparser.parse_args()
untrusted_args = [os.path.basename(args.executable)]
for arg in args.cmd_args:
    if arg.startswith('@'):
        arg = arg[1:]
        m = env_match.match(arg)
        if m:
            nvram_env[m.group(1)] = m.group(2)
        else:
            dev_name = create_manifest_channel(manifest_channels, channel_conf, arg)
            untrusted_args.append(dev_name)
    else:
        untrusted_args.append(arg)

nvram_args = {
    'args': untrusted_args
}

tmpnexe_fn = None
if args.zvm_image:
    for img in args.zvm_image:
        (imgpath, imgmp, imgacc) = (img.split(',') + [None] * 3)[:3]
        dev_name = create_manifest_channel(manifest_channels, channel_conf, imgpath)
        nvram_fstab[dev_name] = '%s %s' % (imgmp or '/', imgacc or 'ro')
        tar = tarfile.open(name=imgpath)
        nexe = None
        try:
            nexe = tar.extractfile(args.executable)
        except KeyError:
            pass
        if nexe:
            tmpnexe_fd, tmpnexe_fn = mkstemp()
            read_iter = iter(lambda: nexe.read(65535), '')
            for chunk in read_iter:
                os.write(tmpnexe_fd, chunk)
            os.close(tmpnexe_fd)
            args.executable = tmpnexe_fn
if args.zvm_debug:
    manifest_channels.append('Channel = %s,/dev/debug,0,0,0,0,%s,%s'
                             % (os.path.abspath('zvsh.log'),
                                channel_conf['writes'], channel_conf['wbytes']))
nvram = '[args]\n'
nvram += 'args = %s\n' % ' '.join([a.replace(',', '\\x2c') for a in nvram_args['args']])
if len(nvram_env) > 0:
    nvram += '[env]\n'
    for k, v in nvram_env.iteritems():
        nvram += 'name=%s,value=%s\n' % (k, v.replace(',', '\\x2c'))
if len(nvram_fstab) > 0:
    nvram += '[fstab]\n'
    for channel, mount in nvram_fstab.iteritems():
        (mp, access) = mount.split()
        nvram += 'channel=%s,mountpoint=%s,access=%s,removable=no\n' % (channel, mp, access)
manifest = ''
for k, v in manifest_conf.iteritems():
    manifest += '%s = %s\n' % (k, v)
manifest += 'Program = %s\n' % os.path.abspath(args.executable)
manifest_fn = None
nvram_fn = None
zerovm = None
reader = None
try:
    nvram_fd, nvram_fn = mkstemp()
    os.write(nvram_fd, nvram)
    os.close(nvram_fd)
    manifest_channels.append('Channel = %s,/dev/nvram,3,0,%s,%s,0,0'
                             % (os.path.abspath(nvram_fn),
                                channel_conf['reads'], channel_conf['rbytes']))
    manifest += '\n'.join(manifest_channels)
    manifest_fd, manifest_fn = mkstemp()
    os.write(manifest_fd, manifest)
    os.close(manifest_fd)
    #print '\n'.join(['-' * 10 + 'NVRAM' + '-' * 10, open(nvram_fn).read(), '-' * 25])
    #print '\n'.join(['-' * 8 + 'MANIFEST' + '-' * 8, open(manifest_fn).read(), '-' * 24])
    zvm_run = ['zerovm', '-PQt1']
    if args.zvm_trace:
        trace_log = os.path.abspath('zvsh.trace.log')
        zvm_run.extend(['-T', trace_log])
    zvm_run.append(manifest_fn)
    zerovm = Popen(zvm_run, stdin=PIPE, stdout=PIPE)
    reader = spawn(stdin_reader, output=zerovm.stdin)
    if sys.stdout.isatty():
        for line in zerovm.stdout:
            sys.stdout.write(line)
    else:
        read_iter = iter(lambda: zerovm.stdout.read(65535), '')
        for line in read_iter:
            sys.stdout.write(line)
    zerovm.wait()
    cleanup([manifest_fn, nvram_fn, tmpnexe_fn])
except (KeyboardInterrupt, Exception):
    if zerovm:
        zerovm.wait()
    cleanup([manifest_fn, nvram_fn, tmpnexe_fn])
