How to compile
----

	wget https://webp.googlecode.com/files/libwebp-0.3.0.tar.gz
	tar xvf libwebp-0.3.0.tar.gz
	cd libwebp-0.3.0
	autoreconf -vif
	./configure --host=x86_64-nacl --prefix=/usr/x86_64-nacl --disable-shared --enable-static --disable-threading LIBPNG_CONFIG=/usr/x86_64-nacl/bin/libpng-config LIBS="-lz -lm"
	make
	sudo make install

