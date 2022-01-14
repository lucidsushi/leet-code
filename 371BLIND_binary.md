In the binary system, each digit represents an increasing power of 2

... 2<sup>3</sup> 2<sup>2</sup> 2<sup>1</sup> 2<sup>0</sup>  
... 8   4   2   1  

1010 =   
`1`*8 + `0`*4 + `1`*2 + `0`*1 = 8 + 2 = 10  

10 =   
`1`*2 + `0`*1 = 2

32bit mask using hexadecimal:
0xffffffff (each f = 1111)
assert 0xffffffff == 0b11111111111111111111111111111111)

Learning Negative Number in Two's Complement
(https://www.youtube.com/watch?v=4qH4unVtJkE)
(to negate(sum as 0) a two's complement number, flip all the bits and add 1 to the binary number)
0101 = 5
1010 (flip)
1011 = -5 (flip + 1)

(looking at the table, when you get complement using ~, ~x is always -x-1)
~5 = ~0101 = 1010 = -8 (1000) + 2 (010) = -6 = -5-1

## In Python there's near infinite 1s

`assert 8 == 0b1000`　（1000 is 8）

`assert -8 == -0b1000` (sign is displayed in the front -- Python implementation)

using mask of 0xff (8 bits)　　

`assert -8 & mask == 0b11111000` (masked result is no longer in the form of -0b... but should still be -8)

`assert 0b11111000 == 248` （python not treating the first bit as a sign bit）




Binary addition is similar to normal expected decimal arithmetic, but only represented with 1 and 0s
```
Decimal (base-ten)
 19
+11
---
 30

Binary (base-two)  
 10011
+ 1011
------
 11110

print(0b10011) >> 19
print(0b1011) >> 11
print(0b11110) >> 30
```  
*0b is the Python prefix for the representation of binary numbers*

using ^ and & to simulate addition (handling carry)

looking at binary addition of a digit without handling of carry, say 1 + 1 = 0 (with 1 as carry); we know any time we want to move to the next digit it means the current digit combines to 0; using x ^ y we can get 1 ^ 1 is 0 (with unhandled carry) and 1 ^ 0 is 1 (no carry)

to account for carry we can use & where 1 & 1 is 1 (captures carry) and 1 ^ 0 is 0 (no carry)
but the carry value belongs to to the next digit so we have to shift the bit by one to the left (just like for 01 + 09, the "1" shifts to the left "0" location which results in sum being 10)

addition therefore ends when all the digits are added and there's no more carry to handle

if we look at  11 + 10 = 101 in without using a "+" sign:

  11
^ 10
----
  01 (addition without carry)

  11
 &10
----
  10 
<< 1
 100 (carry)


carry is not all resolved (0) so we continue

  01
^100 
----
 101 (addition without carry)

  01
&100
----
 000 (carry -- all resolved)

the result of adding 11 (3) and 10 (2) as 101 (5) is what we expect using the "+" arithmetic operator, and the above show the biwise logic to achieve the same result (looping until carry is 0)  

Capturing this logic in an attempt of self documenting Python code:
```python
def sum_via_bitwise(a: int, b: int) -> int:
    carry = 'sum_without_carry accounts for carry when carry is 0'
    while carry:
        carry = (a & b) << 1
        sum_without_carry = a ^ b
        a = sum_without_carry
        b = carry
    return sum_without_carry
```

But what happens when the addition contains negative numbers?
```
Decimal (base-ten)
 -3
+11
---
  8


Binary (base-two)  

3  = 00011
-3 = 11101 

 11101
+01011
------
 01000

assert (-16 + 0b01101) == -3
assert 0b01011 == 11
assert 0b01000 == 8
```  





'%03.2f' can be translated to '{:03.2f}'
https://docs.python.org/3/library/string.html?highlight=string%20formatting#format-examples


32 16 8 4 2 1

```
&	Bitwise AND	x & y         Returns 1 if both the bits are 1 else 0.
|	Bitwise OR	x | y         Returns 1 if either of the bits is 1 else 0.
~	Bitwise NOT	~x            Returns the complement of x.
^	Bitwise XOR	x ^ y         Returns 1 if only one of the bits is 1, else 0.
>>	Bitwise right shift	x>>   Shift x to the right by y positions.
<<	Bitwise left shift	x<<   Shift x to the left by y positions.
```

```python
def using_bitwise_and():
    """Returns 1 if both the bits are 1 else 0.
    """
    print("\nUsing bitwise and")
    x = 0b1010
    y = 0b0101
    print(f"{x:06b}, {x} = X")
    print(f"{y:06b}, {y} = Y")
    print(f"{x & y:06b}, {x & y} = X & Y")

using_bitwise_and()

def using_bitwise_or():
    """Returns 1 if either of the bits is 1 else 0.
    """
    print("\nUsing bitwise or")
    x = 0b1010
    y = 0b0101
    print(f"{x:06b}, {x} = X")
    print(f"{y:06b}, {y} = Y")
    print(f"{x | y:06b}, {x | y} = X | Y")

using_bitwise_or()

def using_bitwise_not():
    """Returns the complement of x.
    """
    print("\nUsing bitwise not")
    x = 0b01010
    print(f"{x:05b}, {x} = X")
    print(f"{~x:05b}, {~x} = ~X")

using_bitwise_not()
```

# what is f-string 08b
# https://www.python.org/dev/peps/pep-0498/
