# Python `randomhash` package

[![pytest](https://github.com/jlumbroso/python-random-hash/actions/workflows/continuous-integration.yaml/badge.svg)](https://github.com/jlumbroso/python-random-hash/actions/workflows/continuous-integration.yaml)
[![codecov](https://codecov.io/gh/jlumbroso/python-random-hash/branch/main/graph/badge.svg?token=4S8TD999YC)](https://codecov.io/gh/jlumbroso/python-random-hash)

A simple, time-tested, family of random hash functions in Python, based on CRC32
and xxHash, affine transformations, and the Mersenne Twister.

This is a companion library to [the identical Java version](https://github.com/jlumbroso/java-random-hash).

## Installation and usage

The library is available on PyPI, and can be installed through normal means:

```shell
$ pip install randomhash
```

Once installed, it can be called either by instantiating a family of random
hash functions, or using the default instantiated functions:

```python
import randomhash

# Create a family of random hash functions, with 10 hash functions

rfh = randomhash.RandomHashFamily(count=10)
print(rfh.hashes("hello"))  # will compute the ten hashes for "hello"

# Use the default instantiated functions

print(randomhash.hashes("hello", count=10))
```

## Features

This introduces a family of hash functions that can be used to implement probabilistic
algorithms such as HyperLogLog. It is based on _affine transformations of either the
CRC32 hash functions_, which have been empirically shown to provide good performance
(for consistency with other versions of this library, such as the Java version), or
[the more complex xxHash hash functions](https://cyan4973.github.io/xxHash/) that are
made available through [the `xxhash` Python bindings](https://github.com/ifduyue/python-xxhash).
The pseudo-random numbers are drawn according to
[the standard Python implementation](https://docs.python.org/3/library/random.html)
of the [Mersenne Twister](http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/emt.html).

<!-- NEEDS TO BE REWRITTEN FOR PYTHON VERSION

To try out the hash functions, you can compile and run the example program:

```shell
javac Example.java
java Example
```

This will generate a report, such as the one below, which shows how a hundred
hash functions perform on provided data that appears pseudo-random (note that it
is important when running these audits that the data provide as input be made
of _unique_ elements, even if the hash functions will mainly be used in streaming
algorithms, to project duplicates to the same hashed value):

```
java Example
input: data/unique.txt
number of hash functions: 100
hashing report:
> bucket count: 10
> total values hashed: 1670700
> [ 10.00% 10.03% 10.03%  9.96% 10.01% 10.00%  9.99%  9.98% 10.02%  9.98%  ]
> chi^2 test: 0.000399
> is uniform (with 90% confidence)? true
```

In practice, you can use it this way, by instantiating a family and using the
`hash(String)` method to generate a single hashed value:

```java
import randomhash.RandomHashFamily;

RandomHashFamily rhf = new RandomHashFamily(1);

System.out.print("hello -> ");
System.out.print(rhf.hash("hello"));
```

which will print:

```
hello -> 2852342977
```

and it can also generate several pseudo-random hash values at the same time,
in this case 10, which it will return in an array:

```java
RandomHashFamily rhf = new RandomHashFamily(10);
long[] hashes = rhf.hashes(); // 10 elements
```

-->

## Some history

In 1983, G. N. N. Martin and Philippe Flajolet introduced the algorithm known
as [_Probabilistic Counting_](http://algo.inria.fr/flajolet/Publications/FlMa85.pdf),
designed to provide an extremely accurate and efficient
estimate of the number of unique words from a document that may contain repetitions.
This was an incredibly important algorithm, which introduced a **revolutionary idea**
at the time:

> The only assumption made is that records can be hashed in a suitably pseudo-uniform
> manner. This does not however appear to be a severe limitation since empirical
> studies on large industrial files [5] reveal that _careful_ implementations of
> standard hashing techniques do achieve practically uniformity of hashed values.

The idea is that hash functions can "transform" data into pseudo-random variables.
Then a text can be treated as a sequence of random variables drawn from a uniform
distribution, where a given word will always occur as the same random value (i.e.,
`a b c a a b c` could be hashed as `.00889 .31423 .70893 .00889 .00889 .31423 .70893` with
every occurrence of `a` hashing to the same value). While this sounds strange,
empirical evidence suggests it is true enough in practice, and eventually [some
theoretical basis](https://people.seas.harvard.edu/~salil/research/streamhash-Jun10.pdf)
has come to support the practice.

The original _Probabilistic Counting_ (1983) algorithm gave way to _LogLog_ (2004),
and then eventually _HyperLogLog_ (2007), one of the most famous algorithms in the
world as described in [this article](https://arxiv.org/abs/1805.00612). These algorithms
and others all used the same idea of hashing inputs to treat them as random variables,
and proved remarkably efficient and accurate.

But as highlighted in the above passage, it is important to be _careful_.

## Hash functions in practice

In practice, it is easy to use poor quality hash functions, or to use cryptographic
functions which will significantly slow down the speed (and relevance) of the
probabilistic estimates. However, on most data, some the cyclic polynomial checksums
(such as Adler32 or CRC32) provide good results---as do efficient, general-purpose
non-cryptographic hash functions such as xxHash.
