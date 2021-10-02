========== DAY ONE ========== 

jorn peterson - data engineering/ data ingestion / data science 
simon weib (weiss) - recommendation engine
    research type - translate matlab to python
walter reade - kaggle
ayman sal-blade

============
lighting talks by each person -- to share what you've learnt
============

- type instability: panda.loc --> dataframe or series
- pep572: walrus operator
- python is flooring division   5//2 = 2,  -5//2 = -3
- python (what is pragma, import prevoius behavior?)
    from __future__ import division
- pep448 (import to know unpacking generalizations)
- itertool, collections receipes ()
- string fomatting ( { = } , { = :>})
- type of immutable makes it hashable
- api design question: why is slic() unhashable
- python3.6 ordered dict became the default dictionary(?)

- homogeneous and hetereogenous array?
- list (data, collection) -- typtically homogeneous?
- tuple(structure, record) -- typically hetereogenous, access via unpacking

- handling modalities to elimite type instability for better API design?
- numpy ndarray reshape is cheap (vs list)
    __array_interface["data"][0] is the same

- programming structure vs computation
    - python int has a lot of overhead
        `from sys import getsizeof`
    - list / program structuring (human scale)
    - ndarray / computational (machine scale)


- pure functions can be part of the value of a lookup table?
- from collections import Counter

- decorator @bee/aaa --> blah = bee(aaa)
    - decorator just has to be a callable that takes a def/class object and return a value

- from inspect import signature / signature.bind() ? -- normalize?
    - when to use sig.bind (composition?)

    print(f'\N{black club suit}')

- @timed if __debug__ else passthru (another debug)

- *args disamuguates consistent calling convention by forcingi everything to a tuple


========== DAY TWO ==========
- find small trivial thing, dig until it works
    - read source code!!
    - olds peps have less value because it could not be where the real discussion happened

- python tail recursion optimization
- memoization (dynamic programming?)
- from time import perf_counter (better than time.time?, no monotonic)
- write functions to reduce "update anomaly"

- from hypothetis import given
    - from hypothetis.strategies import integer

- iteration helpers
    - first , last, nwise, longest

- iterator is a reference to an iterable

- yield
    - in generator, yield value, and yield control

- coroutine (some way to pass more info into )
    - more flexibility to plug into your api
- state machines
- what is tee()


========== DAY Three ==========

- learn to use enum (from enum import Enum, auto)
- class. __repr__ should be a string that prints as closely as to what inputs to the class is

- learn why classmethod is useful

- from dataclasses import dataclass

- from functools import total_ordering

~ vm(metaclass=vmeta)is just  a mechanical placeholder for you to hook into things

- mor mor mro your boat, up the type heiarchy

- from inspect import getfile, getmodule, getsource

- it's worth understanding how getattr works (mro)

- understand usage of @property
    - one fair use is for attributes that are expensive for compute