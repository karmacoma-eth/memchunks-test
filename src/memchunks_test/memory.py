from sortedcontainers import SortedDict

def byte_length(elem):
    # TODO support for bv
    return len(elem)


class Memory:
    def __init__(self, oob_error=False):
        self.data = SortedDict()
        self.length = 0
        self.oob_error = oob_error

    def append(self, chunk):
        # can not append empty chunks
        if len(chunk) == 0:
            return

        start = self.length
        self.data[start] = chunk
        self.length += len(chunk)

    def __getslice__(self, start, stop):
        # works but we don't want to do one byte at a time
        # return bytes(self[i] for i in range(start, stop))

        first_chunk_index = self.data.bisect_right(start) - 1
        if first_chunk_index < 0:
            return self.__read_oob_range(stop - start)

        expected_length = stop - start

        # we will store (fragments of) subelements in this list
        acc = []
        acc_len = 0

        for (chunk_start, chunk) in self.data.items()[first_chunk_index:]:
            chunk_len = byte_length(chunk)

            if chunk_start >= stop:
                break

            if start == chunk_start and stop >= chunk_start + chunk_len:
                # the entire chunk is in the slice
                acc.append(chunk)
                acc_len += chunk_len

            else:
                # a portion of the chunk is in the slice
                start_offset = max(0, start - chunk_start)
                end_offset = min(chunk_len, stop - chunk_start)
                chunk_slice_len = end_offset - start_offset
                assert chunk_slice_len > 0

                chunk_slice = chunk[start_offset:end_offset]
                acc.append(chunk_slice)
                acc_len += chunk_slice_len

            assert acc_len <= expected_length

            if acc_len == expected_length:
                break

        if acc_len < expected_length:
            acc.append(self.__read_oob_range(expected_length - acc_len))

        # return ByteVec(acc)
        return b''.join(acc)

    def __getitem__(self, key):
        if isinstance(key, slice):
            start = key.start or 0
            stop = key.stop or self.length
            step = key.step or 1

            if step != 1:
                raise NotImplementedError

            return self.__getslice__(start, stop)

        index = key
        chunk_index = self.data.bisect_right(index) - 1
        if chunk_index < 0:
            return self.__read_oob_byte()

        start, chunk = self.data.peekitem(chunk_index)
        offset = index - start
        assert offset >= 0

        if offset >= len(chunk):
            return self.__read_oob_byte()

        return chunk[offset]

    def __setslice__(self, start, stop, value):
        if start > stop:
            raise ValueError("Start index must be less than or equal to stop index")

        if start < 0:
            start = max(0, self.length + start)
        if stop < 0:
            stop = max(0, self.length + stop)

        if start < 0 or stop < 0:
            raise IndexError

        if stop - start != len(value):
            raise ValueError("Length of value must match the length of the slice")

        first_chunk_index = self.data.bisect_right(start) - 1
        if first_chunk_index < 0:
            # there are no chunks, so we backfill
            self.append(b'\x00' * start)
            self.append(value)
            return

        # there are one or more existing chunks
        first_chunk_start, chunk = self.data.peekitem(first_chunk_index)
        first_chunk_end = first_chunk_start + len(chunk)

        # aligned write, just overwrite the existing chunk
        if start == first_chunk_start and stop == first_chunk_end:
            self.data[first_chunk_start] = value

            # length is unchanged, so we can exit early
            return

        last_chunk_index = self.data.bisect_right(stop) - 1
        last_chunk_start, last_chunk = self.data.peekitem(last_chunk_index)
        last_chunk_end = last_chunk_start + len(last_chunk)

        # if we are past the end of the last chunk, pad and append
        if start >= last_chunk_end:
            self.append(b'\x00' * (start - last_chunk_end))
            self.append(value)
            return

        # remove the chunks that will be overwritten
        for key in list(self.data.irange(minimum=first_chunk_index, maximum=last_chunk_index, inclusive=(False, False))):
            print(f"deleting chunk@{key}")
            del self.data[key]

        # unaligned write, split the chunk
        start_offset = start - first_chunk_start
        stop_offset = start_offset + len(value)
        new_chunk = chunk[:start_offset] + value + chunk[stop_offset:]
        self.data[first_chunk_start] = new_chunk

        self.length = max(self.length, stop)

    def __setitem__(self, key, value) -> None:
        if isinstance(key, slice):
            start = key.start or 0
            stop = key.stop or self.length
            step = key.step or 1

            if step != 1:
                raise NotImplementedError

            return self.__setslice__(start, stop, value)

        # value must be a byte
        assert value & 0xff == value
        value_bytes = value.to_bytes(1)

        index = key
        chunk_index = self.data.bisect_right(index) - 1
        if chunk_index < 0:
            # there is no chunk so we must backfill
            chunk = b'\x00' * (index) + value_bytes
            self.append(chunk)
            return

        start, chunk = self.data.peekitem(chunk_index)
        offset = index - start
        assert offset >= 0

        if offset >= len(chunk):
            # we are after the bounds of the last chunk so we must backfill
            new_chunk = b'\x00' * (offset - len(chunk)) + value_bytes
            self.append(new_chunk)
            return

        # we are overwriting a byte in an existing chunk
        # (potentially expensive if the chunk is large?)
        chunk = chunk[:offset] + value_bytes + chunk[offset + 1:]
        self.data[start] = chunk


    def __read_oob_range(self, length):
        if self.oob_error:
            raise IndexError
        else:
            return b'\x00' * length

    def __read_oob_byte(self):
        return self.__read_oob_range(1)[0]

    def __len__(self):
        return self.length#

    def dump(self, msg=None):
        print(f"-- MEMORY DUMP (length: {self.length}) -- {msg if msg else ''}")
        for (start, chunk) in self.data.items():
            print(f'chunk@{start}: {chunk}')

    def _well_formed(self, msg=None):
        self.dump(msg=msg)
        cumulative_length = 0
        for (start, chunk) in self.data.items():
            if len(chunk) == 0:
                raise ValueError("Empty chunk")
            if start != cumulative_length:
                raise ValueError("Non-contiguous chunks")
            cumulative_length += len(chunk)

        if cumulative_length != self.length:
            raise ValueError("Length mismatch")

        return True
