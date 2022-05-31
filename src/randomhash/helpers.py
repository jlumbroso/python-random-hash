
import random


WORD_SIZE: int = 32


def affine_transform(
    x: int,
    a: int = 1,
    b: int = 0,
) -> int:
    return a*x + b


def generate_coprime(
    bits: int = WORD_SIZE,
    prng: random.Random = random,
) -> int:

    # Return a random integer N such that 0 <= N <= 2^bits - 1
    # (when bits=32, this corresponds to drawing one number from
    # the Mersenne Twister, aka calling genrand_int32())

    k = prng.getrandbits(bits)

    # this ensure the number is highly likely coprime with the
    # any random number that is drawn

    coprime = 2*k + 1

    return coprime


def str_to_bytes(
    key: str
) -> bytes:
    
    # NOTE: does it make sense to try two encodings?
    
    try:
        # try most restrictive encoding first
        encoded_key = key.encode("ascii")
        
    except UnicodeEncodeError:
        # if ascii fails, use UTF-8 (least restrictive)
        encoded_key = key.encode("utf-8")
        
    return encoded_key


def truncate_number(
    x: int,
    bits: int = WORD_SIZE,
    as_real: bool = False,
) -> int:

    # this is the binary mask of:
    #  1111111...110000...0000000
    # where there are exactly `bits' bits set to 1

    mask = 2**bits - 1

    # truncate the number provided

    truncated_x = x & mask

    if as_real:
        real_x = truncated_x / (2**bits - 1.0)
        return real_x

    return truncated_x
