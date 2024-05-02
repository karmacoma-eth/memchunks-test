from z3 import *

from typing import Optional

def byte_length(x, strict=True) -> int:
    if is_bv(x):
        if x.size() % 8 != 0 and strict:
            raise ValueError(f"byte_length({x}) with bit size {x.size()}")
        return math.ceil(x.size() / 8)

    if isinstance(x, bytes):
        return len(x)

    if isinstance(x, list):
        # assume list of bytes, as used in calldata
        return len(x)

def extract_bytes(
    data: Optional[BitVecRef], byte_offset: int, size_bytes: int
) -> BitVecRef:
    """Extract bytes from calldata. Zero-pad if out of bounds."""
    if data is None:
        return BitVecVal(0, size_bytes * 8)

    n = data.size()
    if n % 8 != 0:
        raise ValueError(n)

    # will extract hi - lo + 1 bits
    hi = n - 1 - byte_offset * 8
    lo = n - byte_offset * 8 - size_bytes * 8
    lo = 0 if lo < 0 else lo

    val = simplify(Extract(hi, lo, data))

    # zero_padding = size_bytes * 8 - val.size()
    # if zero_padding < 0:
    #     raise ValueError(val)
    # if zero_padding > 0:
    #     val = simplify(Concat(val, con(0, zero_padding)))

    return val

class HalmosMemory:
    def __init__(self):
        self.data = []

    def append(self, value):
        if isinstance(value, bytes):
            self.data.append(x for x in value)

        if isinstance(value, BitVecRef):
            blen = byte_length(value)
            for i in range(blen):
                self.data.append(Extract(i * 8 + 7, i * 8, value))

    def __len__(self):
        return len(self.data)
