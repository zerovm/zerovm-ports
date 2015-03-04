#!/bin/bash
PROJECT_NAME=archivemount-0.8.3
PROJECT_LINK=http://www.cybernoia.de/software/archivemount/archivemount-0.8.3.tar.gz

echo build $PROJECT_NAME
if [[ ! -d $PROJECT_NAME ]] ; then \
    wget -c $PROJECT_LINK && tar xvf $PROJECT_NAME.tar.gz && patch -p0 <patch; \
fi

cd $PROJECT_NAME || exit 1
aclocal && autoreconf -vif && LIBS="-lbz2 -lz" CFLAGS="-D__ZRT__ -I$ZVM_PREFIX/x86_64-nacl/include" ./configure --host=x86_64-nacl --prefix=$ZVM_PREFIX/x86_64-nacl --enable-debug || exit 1
make clean all install
