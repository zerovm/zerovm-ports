How to compile
----

	apt-get source libjpeg62
	cd libjpeg6b-6b1
	./configure --host=x86_64-nacl --prefix=${ZVM_PREFIX}/x86_64-nacl --disable-shared --enable-static
	make
	sudo make install

