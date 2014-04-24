# How to compile

    wget http://heanet.dl.sourceforge.net/project/expat/expat/2.1.0/expat-2.1.0.tar.gz
    tar xfz expat-2.1.0.tar.gz
    cd expat-2.1.0
    ./configure --host=x86_64-nacl prefix=$ZVM_PREFIX/x86_64-nacl
    make install