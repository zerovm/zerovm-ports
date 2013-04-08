How to compile
----

	wget http://zlib.net/zlib-1.2.7.tar.gz
	tar xvf zlib-1.2.7.tar.gz
	cd zlib-1.2.7
	CC=x86_64-nacl-gcc ./configure --prefix=/usr/x86_64-nacl
	make
	sudo make install

