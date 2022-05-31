"""
A simple, time-tested, family of random hash functions in Python, based on CRC32
and xxHash, affine transformations, and the Mersenne Twister.
"""

__version__ = "0.6.0"
__author__ = "Jérémie Lumbroso <lumbroso@cs.princeton.edu>"

version_info = tuple(int(v) if v.isdigit()
                     else v for v in __version__.split('.'))


from .implemented import RandomHashFamily

# to allow for normalizations

from .helpers import int_to_real, real_to_int

# for convenience, create an instantiated version of the class

_default_hash_function_count = 100

_default_random_hash_family = RandomHashFamily(
    count=_default_hash_function_count,
    seed=None,
    as_real=False, # default is to return integers, because exact
)

hash = _default_random_hash_family.hash
hashes = _default_random_hash_family.hashes