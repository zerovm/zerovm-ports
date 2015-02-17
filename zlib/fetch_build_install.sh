#!/bin/bash
PROJECT_NAME=zlib-1.2.8
PROJECT_LINK=http://zlib.net/zlib-1.2.8.tar.gz

echo build $PROJECT_NAME
if [[ ! -d $PROJECT_NAME ]] ; then \
    wget -c $PROJECT_LINK & tar xvf $PROJECT_NAME.tar.gz; \
fi

cd $PROJECT_NAME || exit 1
CC=x86_64-nacl-gcc ./configure --prefix=${ZVM_PREFIX}/x86_64-nacl || exit 1
make clean all install
