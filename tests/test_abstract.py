
import pytest

from randomhash import abstract


_SOME_STRING = "some string"
_SOME_INT = 0
_SOME_K = 3
_SOME_LARGER_K = _SOME_K + 1
_SOME_OTHER_K = 10
_NO_SEED = None
_SOME_SEED = 2
_BAD_COUNT = -1
_NO_COUNT = None


def test_abstract_rhf_init():
    """
    Test whether we can successfully initialize an object (an error will fail the test).
    """
    abstract.AbstractRandomHashFamily(count=_SOME_K, seed=_NO_SEED, as_real=False)
    abstract.AbstractRandomHashFamily(count=_SOME_OTHER_K, seed=_NO_SEED, as_real=False)
    abstract.AbstractRandomHashFamily(count=_SOME_K, seed=_SOME_SEED, as_real=False)
    abstract.AbstractRandomHashFamily(count=_SOME_OTHER_K, seed=_SOME_SEED, as_real=True)

def test_abstract_rhf_init_bad_count():
    """
    Test whether an error is thrown when trying to initialize with an invalid count.
    """
    with pytest.raises(ValueError):
        abstract.AbstractRandomHashFamily(count=_BAD_COUNT, seed=_NO_SEED, as_real=False)

def test_abstract_rhf_gen_tbls_with_force():
    """
    Test whether we can successfully generate tables (an error will fail the test).
    """
    rhf = abstract.AbstractRandomHashFamily(count=1, seed=None, as_real=False)
    rhf._gen_tbls(force=True)

def test_abstract_rhf_gen_tbls_without_force():
    """
    Test whether an error is thrown when trying to overwrite the tables (no error will fail the test).
    """
    rhf = abstract.AbstractRandomHashFamily(count=1, seed=None, as_real=False)

    with pytest.raises(ValueError):
        rhf._gen_tbls(force=False)

def test_abstract_rhf_hash():
    """
    Test whether we can successfully hash a value (an error will fail the test).
    """
    rhf = abstract.AbstractRandomHashFamily(count=1, seed=None, as_real=False)

    with pytest.raises(NotImplementedError):
        rhf.hash(_SOME_STRING)
    
    with pytest.raises(NotImplementedError):
        rhf.hash(_SOME_INT)

def test_abstract_rhf_hashes():
    """
    Test whether we can successfully hash a value (an error will fail the test).
    """
    rhf = abstract.AbstractRandomHashFamily(count=10, seed=None, as_real=False)
    
    with pytest.raises(NotImplementedError):
        rhf.hashes(_SOME_STRING)
    
    with pytest.raises(NotImplementedError):
        rhf.hashes(_SOME_INT, count=_SOME_K)

def test_abstract_rhf_hashes_bad_count():
    """
    Test whether an error is thrown when trying to hash with an invalid count.
    """
    rhf = abstract.AbstractRandomHashFamily(count=_SOME_K, seed=None, as_real=False)

    with pytest.raises(ValueError):
        rhf.hashes(_SOME_STRING, count=_SOME_LARGER_K)
    
    with pytest.raises(ValueError):
        rhf.hashes(_SOME_STRING, count=_BAD_COUNT)