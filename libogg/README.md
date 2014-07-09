# How to compile

    wget http://downloads.xiph.org/releases/ogg/libogg-1.3.2.tar.gz
    tar xfz libogg-1.3.2.tar.gz
    cd libogg-1.3.2/
    ./configure --host=x86_64-nacl --prefix=$ZVM_PREFIX/x86_64-nacl --disable-shared --enable-static
    make
    make install
