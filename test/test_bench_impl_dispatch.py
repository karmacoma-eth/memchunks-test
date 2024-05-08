import pytest
 
from memchunks_test.memory import Memory
from memchunks_test.halmos_mem import HalmosMemory

from z3 import *

MAX_UINT256 = 2**256 - 1

def basic_dispatch_add(x, y):
    if isinstance(x, BitVecRef) or isinstance(x, BitVecRef):
        return x + y
    
    return (x + y) & MAX_UINT256

def bv_add(x, y):
    return x + y

def int_add_and(x, y):
    return (x + y) & MAX_UINT256

def int_add_mod(x, y):
    return (x + y) % 2**256


add_insn = {
    BitVecRef: {
        BitVecRef: bv_add,
        int: bv_add
    },
    int: {
        BitVecRef: bv_add,
        int: int_add_and
    }
}

def fancy_dispatch_add(x, y):
    return add_insn[type(x)][type(y)](x, y)


@pytest.mark.benchmark
def test_symbolic_add_basic(benchmark):
    benchmark(basic_dispatch_add, BitVec('x', 256), 42)


@pytest.mark.benchmark
def test_symbolic_add_fancy(benchmark):
    benchmark(fancy_dispatch_add, BitVec('x', 256), 42)


@pytest.mark.benchmark
def test_concrete_add_basic(benchmark):
    benchmark(basic_dispatch_add, MAX_UINT256, 42)


@pytest.mark.benchmark
def test_concrete_add_fancy(benchmark):
    benchmark(fancy_dispatch_add, MAX_UINT256, 42)
