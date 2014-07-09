How to compile
----

	wget https://webm.googlecode.com/files/libvpx-v1.3.0.tar.bz2
	tar xf libvpx-v1.3.0.tar.bz2
	cd libvpx-v1.3.0
	CROSS=x86_64-nacl- ./configure --target=generic-gnu --enable-pic --enable-realtime-only --enable-postproc --disable-install-srcs --enable-multi-res-encoding --enable-temporal-denoising --disable-unit-tests --disable-install-docs --disable-examples --prefix=$ZVM_PREFIX/x86_64-nacl --disable-multithread
	make
	make install

