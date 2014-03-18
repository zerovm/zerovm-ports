How to compile
----

	wget http://www.openssl.org/source/openssl-1.0.1f.tar.gz
	tar xf openssl-1.0.1f.tar.gz
	cd openssl-1.0.1f
	./Configure no-asm no-dso no-threads no-shared linux-generic32 --prefix=${ZVM_PREFIX}/x86_64-nacl --openssldir=${ZVM_PREFIX}/x86_64-nacl
	make CC=x86_64-nacl-gcc LD=x86_64-nacl-ld MAKEDEPPROG=x86_64-nacl-gcc RANLIB=x86_64-nacl-ranlib
	make CC=x86_64-nacl-gcc LD=x86_64-nacl-ld MAKEDEPPROG=x86_64-nacl-gcc RANLIB=x86_64-nacl-ranlib install

