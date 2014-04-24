# PCRE

First, see original `README` for information about `PCRE`. 
Added "reverse" version of pcregrep called `pcreigrep` which doing search from the end to the beginning.

# How to compile 

    ./configure --host=x86_64-nacl --prefix=$ZVM_PREFIX/x86_64-nacl
    make install

# Testing `pcreigrep`

Make sure you have `zvsh` installed ([github.com](https://github.com/zerovm/zerovm-cli))

    ./zerovm-test.sh