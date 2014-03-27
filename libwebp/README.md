How to compile
----

	wget https://webp.googlecode.com/files/libwebp-0.3.0.tar.gz
	tar xf libwebp-0.3.0.tar.gz
	cd libwebp-0.3.0
	autoreconf -vif
	./configure --host=x86_64-nacl --prefix=${ZVM_PREFIX}/x86_64-nacl --disable-shared --enable-static --disable-threading LIBPNG_CONFIG=${ZVM_PREFIX}/x86_64-nacl/bin/libpng-config LIBS="-lz -lm"
	make
	make install

