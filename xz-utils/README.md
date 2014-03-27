How to compile
----

	wget http://tukaani.org/xz/xz-5.0.4.tar.bz2
	tar xf xz-5.0.4.tar.bz2
	cd xz-5.0.4
	./configure --prefix=${ZVM_PREFIX}/x86_64-nacl --host=x86_64-nacl --disable-threads
	make
	make install

