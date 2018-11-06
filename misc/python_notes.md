#### How to be a Python Expert
- https://www.youtube.com/watch?v=7lmCu8wz8ro
- https://github.com/austin-taylor/code-vault/blob/master/python_expert_notebook.ipynb


#### Data Model
- google python data model
- the python data model is a means by which you can implement protocols;
  those protocols have some abstract meaning depending on the object itself
    + meaning whatever you want to do some __method__ probably exists and some
      associated functions probably exist to help define the specifics of that __method__
- use __repr__ to give your class object a nice string reprensentation
  (10:03)
- 3 core patterns to understand object orientation in Python
    + *protocol view of python*:
        + using associated top-level function (or syntax) to define
          some arbitrary object's behavior that has corresponding __function__ (11:10)
          (14:44)
          (16:20)
        + x + y   -> __add__
        + init x  -> __init__
        + repr(x) -> __repr__
        + x()     -> __call__

    + *built-in inheritance protocal - where you go on a python object to look for things*
    + *some caveats around how object orientation of python works*

#### Metaclasses
- pattern: base class trying to force some constraint (hook in) to the derived class

- how to make sure class works before runtime
    + check on import
    + tests are good but slower
    + `assert hasattr(Base, 'food'), "foo doesn't exist!"` (derived constrain base)

    Three Approaches
    + class is run time executable code in python (hook into build class)
      (37:00)
        ```python
        # Catch Building of Classes
        # (Not the way to do it, but showcase hooking / python protocol)
        class Base:
            def foo(self):
                return self.bar()

        old_bc = __build_class__ # python3 only ?
        def my_bc(fun, name, base=None, **kw):
            if base is Base:
                        print('Check if bar method defined')
            if base is not None:
                return old_bc(fun, name, base, **kw)
            return old_bc(fun, name, **kw)

        import builtins
        builtins.__build_class__ = my_bc
        ```
    + metaclasses
      (type of class derived from class `type` with special methods)
        ```python
        class BaseMeta(type):
          def __new__(cls, name, bases, body):
              if not 'bar' in body:
                  raise TypeError('bad user class')
              return super().__new__(cls, name, bases, body)

        class Base(metaclass=BaseMeta):
            def foo(self):
                return self.bar()
        ```
    + python3.6 init_subclass
        ```python
        class BaseMeta(type):
        def __new__(cls, name, bases, body):
            if name != 'Base' and not 'bar' in body:
                raise TypeError('bad user class')
            return super().__new__(cls, name, bases, body)

        class Base(metaclass=BaseMeta):
            def foo(self):
                return self.bar()
            
            def __init_subclass__(self, *a, **kw):
                print('init_subclass', a, kw)
                return super().__init_subclass__(*a, **kw)
        ```

- "He could have used an Abstract Base Class to enforce creation of a method in a subclass﻿"
    +　https://stackoverflow.com/questions/4382945/abstract-methods-in-python
    +　"Before abc was introduced you would see this frequently."
    　　（https://stackoverflow.com/a/4383103)
    + Python 2/3 differences (https://stackoverflow.com/a/18513858)

- https://www.python-course.eu/python3_abstract_classes.php


#### Decorator (45:56)
- everything happens live in the programming language
- complexity extension is a strength in python? how (53:36)
- @decorator on top of *function* is syntx for =>
  `function_return = decorator(*function*)`
- higher order decoraters (another level of nesting?) (1:03:04)
- closure object duality (1:03:27)

```python
from time import time

def add(x, y=10):
  return x + y

# method 1 (pollutes user code heavily)
before = time()
print('add(10)', add(10))
after = time()
print('time taken:', after - before)
#

# method 2
# (add into function BUT would have to repeat in all other functions)
def add(x, y=10):
  before = time()
  rv = x + y
  after = time()
  print('time taken:', after - before)
  return rv 

print('add(10)', add(10))
#

# method 3 create a timer function
# (downside is you have to go change all your calls)
def timer(func, x, y):
  before = time()
  rv = func(x, y)
  after = time()
  print('elapsed', after - before)

print('add(10)', timer(add, 10))
#

# method 4 using a wrapper f()
def timer(func):
  def f(x, y=10):
    before = time()
    rv = func(x, y)
    after = time()
    print('elapsed', after - before)
    return rv
  return f

add = timer(add) # now add is enhanced with `timer` logic
print('add(10)', add(10))

'''and this is where DECORATOR syntax kicks in for turning
   `add = timer(add)` ===> `@timer`
'''
# also don't need to hard code args
def timer(func):
  def f(*args, **kwargs):
    before = time()
    rv = func(*args, **kwargs)
    after = time()
    print('elapsed', after - before)
    return rv
  return f
#

# higher order decorators
def add_to(n):
  def inner(f):
    def do_this(*args, **kwargs):
      print 'doing something before function!!' + 'added %s' % n
      rv = f(*args, **kwargs)
      return rv
    return do_this
  return inner

@add_to(3) <== test = add_to(3)(test)
def test():
  print 'test is ran'

test()
```


#### Generator (1:04:46) （Function that doesn't return "eagerly"
- *instead of eagerly computing values you give them to the user as they asked for*
- class implementation (1:15:45) <-- fundamental
  + using __iter__ to set initial value for counting
- Yield gives result AND control back to the user (interleaving library / user code)
- *Interleaving AND enforce Sequencing (heart of generator importance) API design (1:21:18)* (co-routine https://stackoverflow.com/a/553745)


`Eager return / Uses storage`
```python
def compute():
    rv = []
    for i in range(10):
        sleep(.5)
        rv.append(i)
    return rv
```

Implementation of `for loop` in python is something like
```python
for x in xs:
  pass

x1 = iter(xs)  --> __iter__
while True:
  x = next(x1) --> __next__

```

`Not eager, not using storage`
```python
import time
class Compute:
  def __init__(self):
    self.last = 100

  def __iter__(self):
    self.last = 0 # ensure proper staring value when you DO iterate
    return self

  # __next__ in python 3
  def next(self):
    rv = self.last
    self.last += 1
    if self.last > 10:
      raise StopIteration()
    time.sleep(.5)
    return rv

c = Compute()
print c.last
for item in c:
  print item
```

`Not eager, not using storage -> generator syntax`
```python
def Computer():
    for i in range(10):
        sleep(.5)
        yield i
```


#### Context Manager (~resource allocation is initialization (c++))
- some desire to setup and tear down
- sqlite3 example (1:26:32)
- context manager pattern:
```python
# with ctx() as x:
#   pass

# x = ctx().__enter__()
# try:
#   pass
# finally:
#    x.__exit__()
```
- combining core pieces together to write pythonic code
```python
from sqlite3 import connect

# method 0 original block
with connect('test.db') as conn:
  cur = conn.cursor()
  cur.execute('create table points(x int, y int)')
  cur.execute('insert into points (x, y) values(1, 1)')
  cur.execute('insert into points (x, y) values(1, 2)')
  cur.execute('insert into points (x, y) values(2, 1)')
  cur.execute('insert into points (x, y) values(2, 2)')
  for row in cur.execute("select x, y from points"):
      print(row)
  for row in cur.execute('select sum(x * y) from points'):
      print(row)
  cur.execute('drop table points')


# method 1 impelement ctx()
class temptable:
  def __init__(self, cur):
    self.cur = cur
  def __enter__(self):
    self.cur.execute('create table points(x int, y int)')
  def __exit__(self, *args):
    self.cur.execute('drop table points')


with connect('test.db') as conn:
  cur = conn.cursor()
  with temptable(cur):
    cur.execute('insert into points (x, y) values(1, 1)')
    cur.execute('insert into points (x, y) values(1, 2)')
    cur.execute('insert into points (x, y) values(2, 1)')
    cur.execute('insert into points (x, y) values(2, 2)')
    for row in cur.execute("select x, y from points"):
        print(row)
    for row in cur.execute('select sum(x * y) from points'):
        print(row)
    



```
- decorator to turn a generator into a contextmanager 
  （`from contextlib import contextmanager`)

#### Summary (1:40:00)
- good python code is code that has a certain clarity to where and
  when a feature should be used; it's code that doesn't waste the
  time of the person that is writing it

#### Super
- introduced for `cooperative mutiple inheritance`
- super(class_name, self) returns an object that can be used to call methods of its parent
- if you don't `def __init__` on the subclass,
  it would automatically inherit from the superclass
- if you `def __init__` on the subclass but do not
  super(subclass, self).__init__ or
  superclass.__init__(self), you won't inherit the superclass

```python
class Shape(object):
    def __init__(self):
        self.color = 'shape color'
        self.name = 'general shape'

class Triangle(Shape):
  def __init__(self):
      self.bar = 'self bar'
      super(Triangle, self).__init__()

test = Triangle()

print test.bar
print dir(test)
```  


- REVIEW CONCEPTS related to PYTHON
- RELATE EACH PROJECT EXPERIENCE TO A BUSINESS NEED/PROBLEM
- 