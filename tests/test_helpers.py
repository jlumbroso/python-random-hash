
from randomhash import helpers


_SOME_STRING = "some string"
_SOME_UTF8_STRING = "some étè string"


# none of these check output, just make sure there is no crash

def test_call_affine_transform():
    helpers.affine_transform(0, 1, 0)

def test_call_generate_coprime():
    helpers.generate_coprime()

def test_call_str_to_bytes():
    helpers.str_to_bytes(_SOME_STRING)

def test_call_str_to_bytes_utf8():
    helpers.str_to_bytes(_SOME_UTF8_STRING)

def test_call_truncate_number():
    helpers.truncate_number(0)
    helpers.truncate_number(0, as_real=True)