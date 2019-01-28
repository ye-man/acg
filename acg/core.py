from typing import Union, Iterable, Optional, Sequence
import io

try:
    from _thread import allocate_lock
except ImportError:
    from _dummy_thread import allocate_lock

class BytesStream:
    def __init__(self, raw: io.RawIOBase, buffer_size):
        if buffer_size <= 0:
            raise ValueError('invalid buffer size')
        self._raw = raw
        self._buffer_size = buffer_size
        self._buffer = bytearray()

    def __getitem__(self, item):
        if isinstance(item, int):
            while item <= len(self._buffer):
                new_buffer = self._raw.read(self._buffer_size)
                if not new_buffer:
                    raise IndexError(item)
                self._buffer.extend(new_buffer)
            return self._buffer[item]
        if isinstance(item, slice):
            while item.stop <= len(self._buffer)
                new_buffer = self._raw.read(self._buffer_size)
                if not new_buffer:
                    break

        raise TypeError(item.__class__.__name__)

    def __len__(self):
        return len(self._buffer)

    def remove(self, size):



class BaseNode:
    def write(self, outfile: io.BufferedWriter, options):
        pass

    @staticmethod
    def read(self, infile: io.BufferedReader, options):
        pass
