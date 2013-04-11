How to compile
----

	wget http://download.savannah.gnu.org/releases/freetype/freetype-2.4.11.tar.gz
	tar xvf freetype-2.4.11.tar.gz
	cd freetype-2.4.11
	autoreconf -vif
	./configure --host=x86_64-nacl --enable-static --disable-shared --prefix=/usr/x86_64-nacl
	make
	sudo make install

