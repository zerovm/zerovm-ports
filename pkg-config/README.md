How to compile
----

	wget http://pkgconfig.freedesktop.org/releases/pkg-config-0.27.1.tar.gz
	tar xvf pkg-config-0.27.1.tar.gz
	cd pkg-config-0.27.1
	./configure --program-prefix=x86_64-nacl- --prefix=/usr
	make
	sudo make install

