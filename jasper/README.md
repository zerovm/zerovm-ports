How to compile
----

	wget http://www.ece.uvic.ca/~frodo/jasper/software/jasper-1.900.1.zip
	unzip jasper-1.900.1.zip
	cd jasper-1.900.1
	autoreconf -vif
	./configure --host=x86_64-nacl --prefix=${ZVM_PREFIX}/x86_64-nacl
	make
	sudo make install

