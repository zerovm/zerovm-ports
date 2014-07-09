# How to compile

    wget http://downloads.xiph.org/releases/vorbis/libvorbis-1.3.4.tar.gz
    tar xfz libvorbis-1.3.4.tar.gz
    cd libvorbis-1.3.4/
    ./configure --host=x86_64-nacl --prefix=$ZVM_PREFIX/x86_64-nacl --disable-shared --enable-static
    make
    make install
