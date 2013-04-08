How to compile
----

	wget http://www.bzip.org/1.0.6/bzip2-1.0.6.tar.gz
	tar xvf bzip2-1.0.6.tar.gz
	cd bzip2-1.0.6
	patch -p0 < ../Makefile.patch
	make
	sudo make install

