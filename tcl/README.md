Tcl port
========

Porting 8.5 version of Tcl. This paricular version is used in some
projects of our own. Feel free to switch branch to latest development
version and porting it by yourself.

    git clone https://github.com/tcltk/tcl -b core_8_5_branch tcl8.5
    cd tcl8.5
    git apply ../strtoul.patch
    ./configure --host=x86_64-nacl --disable-shared --disable-load
    make

Testing
=======

Automatic testing has not been ported yet. If you need some testing you could try the following:

+ create tar archive with tcl standard library (i.e. tcl.tar)
+ `make test` will generate tcltest binary
+ `zvsh --zvm-image=tcl.tar ./tcltest`

