# memchunks-test

```sh
# first, install rye
open https://rye-up.com/

# install dependencies
rye sync

# run tests
rye test

# run benchmarks
rye test -- -m benchmark

# generate a histogram
rye test -- -m benchmark --benchmark-histogram --benchmark-group-by=func --benchmark-sort=mean 

# scope to a single test file
rye test -- -k test_bench_insn_dispatch.py
```
