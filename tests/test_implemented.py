
from randomhash import implemented


_SOME_STRING = "some string"


def test_init_crc32_rhf():
    implemented.CRC32RandomHashFamily()

def test_init_xxhash32_rhf():
    implemented.xxhash32RandomHashFamily()

def test_init_default_rhf():
    implemented.RandomHashFamily()

def test_hash_crc32_rhf():
    rhf = implemented.CRC32RandomHashFamily()
    rhf.hash(_SOME_STRING)

def test_hash_xxhash32_rhf():
    rhf = implemented.xxhash32RandomHashFamily()
    rhf.hash(_SOME_STRING)

def test_hash_default_rhf():
    rhf = implemented.RandomHashFamily()
    rhf.hash(_SOME_STRING)