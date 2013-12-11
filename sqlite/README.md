How to compile
----

	wget http://www.sqlite.org/2013/sqlite-autoconf-3071601.tar.gz
	tar xvf sqlite-autoconf-3071601.tar.gz
	cd sqlite-autoconf-3071601
	autoreconf -vif
	./configure --host=x86_64-nacl --enable-static --disable-shared --prefix=${ZVM_PREFIX}/x86_64-nacl --enable-threadsafe=no --enable-dynamic-extensions=no CFLAGS="-DSQLITE_DEFAULT_LOCKING_MODE=1 -DSQLITE_THREADSAFE=0 -DSQLITE_TEMP_STORE=3"
	make
	sudo make install

