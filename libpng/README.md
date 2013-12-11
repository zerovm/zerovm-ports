How to compile
----

	wget http://download.sourceforge.net/libpng/libpng-1.6.1.tar.gz
	tar xvf libpng-1.6.1.tar.gz
	cd libpng-1.6.1
	autoreconf -vif
	./configure --host=x86_64-nacl --prefix=${ZVM_PREFIX}/x86_64-nacl
	make
	sudo make install

