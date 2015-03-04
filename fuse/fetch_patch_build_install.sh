#!/bin/bash
PROJECT_NAME=fuse-2.9.3
PROJECT_LINK=http://liquidtelecom.dl.sourceforge.net/project/fuse/fuse-2.X/2.9.3/fuse-2.9.3.tar.gz

echo build $PROJECT_NAME
if [[ ! -d $PROJECT_NAME ]] ; then \
    wget -c $PROJECT_LINK && tar xvf $PROJECT_NAME.tar.gz && patch -sp0 <patch; \
fi

cd $PROJECT_NAME || exit 1
LIBS=-lfuseglue CFLAGS="-D__ZRT__ -D_ATFILE_SOURCE -g2" ./configure --host=x86_64-nacl --prefix=$ZVM_PREFIX/x86_64-nacl  || exit 1
make clean all install
