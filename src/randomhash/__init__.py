"""
A simple, time-tested, family of random hash functions in Python, based on CRC32
and xxHash, affine transformations, and the Mersenne Twister.
"""

__version__ = "0.5.0"
__author__ = "Jérémie Lumbroso <lumbroso@cs.princeton.edu>"

version_info = tuple(int(v) if v.isdigit()
                     else v for v in __version__.split('.'))
