#!/bin/bash
PROJECT_LINK=https://github.com/rpodgorny/unionfs-fuse.git
PROJECT_NAME=unionfs-fuse

if [[ ! -d $PROJECT_NAME ]] ; then \
    git clone $PROJECT_LINK && cd $PROJECT_NAME && \
    git checkout 4186fa0227ff5c4fed50e7c15a001d27643db911 \
    && cd .. && patch -p0 <patch; \
fi

cd $PROJECT_NAME/src
PREFIX=$ZVM_PREFIX CFLAGS="-Dexit=exit_fuse_main -D__ZRT__" CC=x86_64-nacl-gcc make clean all install
