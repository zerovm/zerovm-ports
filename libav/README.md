How to compile
----

	wget http://libav.org/releases/libav-10.1.tar.gz
	tar xf libav-10.1.tar.gz
	cd libav-10.1
	./configure --prefix=${ZVM_PREFIX}/x86_64-nacl --disable-asm --enable-static --disable-shared --cross-prefix=x86_64-nacl- --target-os=linux --arch=x86_64
	make
	make install

