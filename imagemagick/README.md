How to compile
----

Install prerequisite libraries/apps (in this order) from zerovm-ports `pkg-config zlib bzip2 libxml2 xz-utils libjpeg jasper libpng lcms tiff libwebp freetype`

	wget http://www.imagemagick.org/download/ImageMagick-6.8.8-10.tar.gz
	tar xf ImageMagick-6.8.8-10.tar.gz
	cd ImageMagick-6.8.8-10
	./configure --host=x86_64-nacl --enable-static --disable-shared --prefix="${ZVM_PREFIX}/x86_64-nacl" PATH="${ZVM_PREFIX}/x86_64-nacl/bin:$PATH" LIBS=-llzma
	make
	make install

