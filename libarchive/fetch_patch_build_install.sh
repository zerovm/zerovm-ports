#!/bin/bash
PROJECT_NAME=libarchive-3.1.2
PROJECT_LINK=http://www.libarchive.org/downloads/libarchive-3.1.2.tar.gz

echo build $PROJECT_NAME
if [[ ! -d $PROJECT_NAME ]] ; then \
    wget -c $PROJECT_LINK && tar xvf $PROJECT_NAME.tar.gz && patch -p0 <patch; \
fi

cd $PROJECT_NAME || exit 1
./configure --without-xml2 --host=x86_64-nacl --prefix=$ZVM_PREFIX/x86_64-nacl || exit 1
make clean all install
