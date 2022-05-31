import random
import typing

from . import helpers

class AbstractRandomHashFamily:

    _WORD_SIZE = helpers.WORD_SIZE

    _count = 1
    _prng = None
    _seed = None
    _as_real = False

    _tbl_coprime = None
    _tbl_noise = None

    def _gen_tbls(
        self,
        force: bool = False
    ) -> typing.NoReturn:

        if self._tbl_coprime is not None or self._tbl_noise is not None:
            if not force:
                raise ValueError(
                    "trying to overwrite already generated tables, use `force=True`"
                )

        # should not be regenerated (as this invalidates previous hashes)

        self._tbl_coprime = [
            helpers.generate_coprime(
                bits=self._WORD_SIZE,
                prng=self._prng
            )
            for i in range(self._count)
        ]

        self._tbl_noise = [
            self._prng.getrandbits(self._WORD_SIZE)
            for i in range(self._count)
        ]

    def __init__(
        self,
        count: int = 1,
        seed: typing.Optional[int] = None,
        as_real: bool = False
    ):

        # set instance variables according to parameters

        try:
            # implicitly checks `count` is a number
            assert count > 0
        except Exception as exc:
            raise ValueError("error with `count`: {}".format(exc))

        self._count = count
        self._seed = seed
        self._as_real = as_real

        # initialize local PRNG

        self._prng = random.Random(self._seed)

        # initialize tables

        self._gen_tbls()

    def _base_hash(
        self,
        key: str,
    ) -> int:
        raise NotImplementedError(
            "trying to call methods on an abstract class; "
            "subclass and implement `base_hash()`"
        )

    def hashes(
        self,
        key: str,
        count: typing.Optional[int] = None,
        as_real: typing.Optional[bool] = None,
    ) -> typing.List[int]:
        
        # before hashing anything, do argument validation

        # determine how to output the hashes

        as_real = as_real or self._as_real

        # figure out how many new hashes to generate

        if count is None:
            count = self._count

        if count > self._count:
            raise ValueError((
                "cannot generate more than m={} hash values; "
                "initialize class with larger count of hash values"
            ).format(self._count))
        
        if count < 0:
            raise ValueError("cannot generate invalid count of hash values")

        # compute the base hash

        base_key_hash = self._base_hash(key=key)

        # generate the derivate hashes using the tables

        computed_hashes = [
            helpers.truncate_number(
                x=helpers.affine_transform(
                    x=base_key_hash,
                    a=self._tbl_coprime[i],
                    b=self._tbl_noise[i],
                ),
                bits=self._WORD_SIZE,
                as_real=as_real,
            )
            for i in range(count)
        ]

        return computed_hashes

    def hash(
        self,
        key: str,
        as_real: typing.Optional[bool] = None,
    ) -> int:
        array = self.hashes(key=key, count=1, as_real=as_real)
        return array[0]
