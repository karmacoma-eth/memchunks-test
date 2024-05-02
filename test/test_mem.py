import pytest

from memchunks_test.memory import Memory


def test_memory_reads():
    mem = Memory()

    # empty memory checks
    assert len(mem) == 0
    assert not mem
    assert mem[0] == 0
    assert mem[2:8] == b'\x00' * 6

    chunks = [b'abc', b'hello', b'world']
    for chunk in chunks:
        mem.append(chunk)

    assert len(mem) == 13
    assert mem[0] == b'a'[0]
    assert mem[1] == b'b'[0]
    assert mem[2] == b'c'[0]
    assert mem[3] == b'h'[0]
    assert mem[4] == b'e'[0]

    assert mem[12] == b'd'[0]
    assert mem[13] == 0
    assert mem[14] == 0
    assert mem[15] == 0
    assert mem[16] == 0

    assert mem[:2] == b'ab'
    assert mem[2:8] == b'chello'
    assert mem[8:] == b'world'
    assert mem[2:16] == b'chelloworld\x00\x00\x00'


def test_memory_write_bytes():
    mem = Memory()

    # write a single byte into empty memory
    mem[0] = 0x42
    assert mem[0] == 0x42
    assert len(mem) == 1

    # write another byte to extend non-empty memory
    mem[12] = 0x42
    assert mem[12] == 0x42
    assert len(mem) == 13

    # write a single byte into an existing chunk
    mem[6] = 0x42
    assert len(mem) == 13 # unchanged
    assert mem[6] == 0x42


def test_memory_write_slices():
    mem = Memory()

    with pytest.raises(Exception):
        # length mismatch
        mem[32:64] = b'hello'

    # write a slice into empty memory
    mem[2:7] = b'hello'
    assert len(mem) == 7
    assert mem[:] == b'\x00\x00hello'
    assert mem._well_formed()

    # overwrite into the existing chunk
    mem[4:6] = b'!!'
    assert mem._well_formed()
    assert len(mem) == 7 # unchanged
    assert mem[:] == b'\x00\x00he!!o'

    # add a couple more chunks
    mem[10:15] = b'world'
    assert mem._well_formed()
    assert len(mem) == 15
    assert mem[:] == b'\x00\x00he!!o\x00\x00\x00world'

    mem[20:32] = b'foofeefoofum'
    assert mem._well_formed()
    assert len(mem) == 32
    assert mem[:] == b'\x00\x00he!!o\x00\x00\x00world\x00\x00\x00\x00\x00foofeefoofum'

    # stomp the existing chunks
    mem[:32] = b'hellohellohellohellohellohellohe'
    assert mem._well_formed('after stomping')
    assert len(mem) == 32
    assert mem[:] == b'hellohellohellohellohellohellohe'
    assert mem[:5] == b'hello'

    # stomp in the middle of the existing chunk and extend the memory
    mem[16:48] = b'worldworldworldworldworldworldwo'
    assert mem._well_formed()
    assert len(mem) == 48
    assert mem[:32] == b'hellohellohellohworldworldworldw'
