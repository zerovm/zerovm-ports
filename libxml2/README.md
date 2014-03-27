How to compile
----

	wget ftp://xmlsoft.org/libxml2/libxml2-2.9.0.tar.gz
	tar xf libxml2-2.9.0.tar.gz
	cd libxml2-2.9.0
	autoreconf -vif
	./configure --host=x86_64-nacl --prefix=${ZVM_PREFIX}/x86_64-nacl --without-threads
	make
	make install
	wget ftp://xmlsoft.org/libxml2/libxslt-1.1.28.tar.gz
	tar xf libxslt-1.1.28.tar.gz
	cd libxslt-1.1.28
	autoreconf -vif
	./configure --host=x86_64-nacl --prefix=${ZVM_PREFIX}/x86_64-nacl --disable-shared --with-libxml-prefix=${ZVM_PREFIX}/x86_64-nacl
	make
	make install

