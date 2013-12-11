How to compile
----

	wget http://zlib.net/zlib-1.2.8.tar.gz
	tar xvf zlib-1.2.8.tar.gz
	cd zlib-1.2.8
	CC=x86_64-nacl-gcc ./configure --prefix=/usr/x86_64-nacl
	make
	sudo make install

