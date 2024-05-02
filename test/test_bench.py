import pytest

from memchunks_test.memory import Memory
from memchunks_test.halmos_mem import HalmosMemory

from z3 import *

@pytest.mark.benchmark
@pytest.mark.parametrize("size", [32, 256, 1024, 32768])
def test_chunkmem_append(benchmark, size):
    mem = Memory()
    data = b'x' * size
    benchmark(mem.append, data)


@pytest.mark.benchmark
@pytest.mark.parametrize("size", [32, 256, 1024, 32768])
def test_halmosmem_append_concrete(benchmark, size):
    mem = HalmosMemory()
    data = b'x' * size
    benchmark(mem.append, data)


@pytest.mark.benchmark
@pytest.mark.parametrize("size", [32, 256, 1024, 32768])
def test_halmosmem_append_symbolic(benchmark, size):
    mem = HalmosMemory()
    data = BitVec('x', 8 * size)
    benchmark(mem.append, data)
