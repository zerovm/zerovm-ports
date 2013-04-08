How to compile
----

	wget ftp://ftp.remotesensing.org/pub/libtiff/tiff-4.0.3.tar.gz
	tar xvf tiff-4.0.3.tar.gz
	cd tiff-4.0.3
	autoreconf -vif
	./configure --host=x86_64-nacl --prefix=/usr/x86_64-nacl --disable-shared --enable-static
	make
	sudo make install

