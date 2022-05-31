

import zlib
import xxhash

from . import abstract
from . import helpers

class CRC32RandomHashFamily(abstract.AbstractRandomHashFamily):
    
    @staticmethod
    def crc32_unsigned(key: str) -> int:
        
        # crc32 in python takes bits, not strings
        
        encoded_key = helpers.str_to_bytes(key=key)
        
        # python 3 (this library is py3 only)'s zlib implementation
        # of CRC32 already returns unsigned numbers
        
        hashed_key = zlib.crc32(encoded_key)
        
        return hashed_key
        
    def _base_hash(self, key):
        return CRC32RandomHashFamily.crc32_unsigned(key=key)


class xxhash32RandomHashFamily(abstract.AbstractRandomHashFamily):
    
    @staticmethod
    def xxhash32_unsigned(key: str) -> int:
        hashed_key = xxhash.xxh32_intdigest(key)
        return hashed_key
        
    def _base_hash(self, key):
        return xxhash32RandomHashFamily.xxhash32_unsigned(key=key)


# the standard is CRC32, so we'll make that the default
RandomHashFamily = CRC32RandomHashFamily