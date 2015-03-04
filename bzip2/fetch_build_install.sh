#!/bin/bash
PROJECT_NAME=bzip2-1.0.6
PROJECT_LINK=http://www.bzip.org/1.0.6/bzip2-1.0.6.tar.gz

echo build $PROJECT_NAME
if [[ ! -d $PROJECT_NAME ]] ; then \
    wget -c $PROJECT_LINK && tar xvf $PROJECT_NAME.tar.gz; \
fi

cd $PROJECT_NAME || exit 1
CC=x86_64-nacl-gcc PREFIX=${ZVM_PREFIX}/x86_64-nacl make clean all install
