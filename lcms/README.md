How to compile
----

	wget 'http://downloads.sourceforge.net/project/lcms/lcms/1.19/lcms-1.19.tar.gz?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Flcms%2Ffiles%2Flcms%2F1.19%2F&ts=1365464613&use_mirror=iweb' -O lcms-1.19.tar.gz
	tar xvf lcms-1.19.tar.gz
	cd lcms-1.19
	autoreconf -vif
	./configure --host=x86_64-nacl --enable-static --disable-shared --prefix=/usr/x86_64-nacl LIBS="-lz -llzma -lm"
	make
	sudo make install
	wget 'http://downloads.sourceforge.net/project/lcms/lcms/2.4/lcms2-2.4.tar.gz?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Flcms%2Ffiles%2Flcms%2F2.4%2F&ts=1365465045&use_mirror=iweb' -O lcms2-2.4.tar.gz
	tar xvf lcms2-2.4.tar.gz
	cd lcms2-2.4
	./configure --host=x86_64-nacl --enable-static --disable-shared --prefix=/usr/x86_64-nacl LIBS="-lz -llzma -lm"
        make
        sudo make install

