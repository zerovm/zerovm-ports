How to compile
----

	wget ftp://xmlsoft.org/libxml2/libxml2-2.9.0.tar.gz
	tar xvf libxml2-2.9.0.tar.gz
	cd libxml2-2.9.0
	autoreconf -vif
	./configure --host=x86_64-nacl --prefix=/usr/x86_64-nacl --without-threads
	make
	sudo make install
	wget ftp://xmlsoft.org/libxml2/libxslt-1.1.28.tar.gz
	tar xvf libxslt-1.1.28.tar.gz
	cd libxslt-1.1.28
	autoreconf -vif
	./configure --host=x86_64-nacl --prefix=/usr/x86_64-nacl --disable-shared --with-libxml-prefix=/usr/x86_64-nacl
	make
	sudo make install

