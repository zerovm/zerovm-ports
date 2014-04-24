# How to compile

    wget http://ftp.gnu.org/pub/gnu/libiconv/libiconv-1.14.tar.gz
    tar xfz libiconv-1.14.tar.gz
    patch < config.sub.patch -p0
    cd libiconv-1.14/
    ./configure --host=x86_64-nacl --prefix=$ZVM_PREFIX/x86_64-nacl --disable-shared --enable-static
    make install