#### Table of Contents

#### [1. What is Hoisting?](https://github.com/lucidsushi/leet-code/blob/master/misc/javascript_top10.md#1-what-is-hoisting-sushi)

#### [2. What is Closure?](https://github.com/lucidsushi/leet-code/blob/master/misc/javascript_top10.md#2-what-is-closure-sushi)

#### [3. Implement TwoSum()](https://github.com/lucidsushi/leet-code/blob/master/misc/javascript_top10.md#3-implement-twosum-sushi)

#### [4. Implement Fibonacci / Debounce](https://github.com/lucidsushi/leet-code/blob/master/misc/javascript_top10.md#4-implement-fibonaccidebounce-sushi)

#### [5. Implement Best Time to Buy and Sell Stock](https://github.com/lucidsushi/leet-code/blob/master/misc/javascript_top10.md#5-implement-best-time-to-buy-and-sell-stock-sushi)

#### [6. More Scoping Question](https://github.com/lucidsushi/leet-code/blob/master/misc/javascript_top10.md#6-more-scoping-question-sushi)

#### [7. Something Async](https://github.com/lucidsushi/leet-code/blob/master/misc/javascript_top10.md#7-something-async-sushi)

#### [8. What are Promises?](https://github.com/lucidsushi/leet-code/blob/master/misc/javascript_top10.md#8-what-are-promises-sushi)

#### [9. (Uncommon) == vs ===](https://github.com/lucidsushi/leet-code/blob/master/misc/javascript_top10.md#9-uncommon--vs--sushi)

#### [10. (Uncommon) Floating Point Numbers](https://github.com/lucidsushi/leet-code/blob/master/misc/javascript_top10.md#10-uncommon-floating-point-numbers-sushi)



---
<br />

## 1. What is Hoisting? [:sushi:](https://github.com/lucidsushi/leet-code/blob/master/misc/javascript_top10.md#table-of-contents)

- "Variable binding created at the top to the (block for let/const) scope (function scope) containing the delcartion"

- "Hoisting was thought up as a general way of thinking about how execution contexts (specifically the creation and execution phases) work in JavaScript. However, the concept can be a little confusing at first.
    Conceptually, for example, a strict definition of hoisting suggests that variable and function declarations are physically moved to the top of your code, but this is not in fact what happens. Instead, the variable and function declarations are put into memory during the compile phase, but stay exactly where you typed them in your code."

- "JavaScript only hoists declarations, not assignments. If a variable is declared and assigned AFTER using it, the value will be undefined"


#### Example 1
```javascript
console.log(num); // Returns undefined 
var num;
num = 6;

num = 6;
console.log(num); // returns 6
var num;
```

#### Example 2
```javascript
var x = 1; // Assigned x
console.log(x + " " + y); // '1 undefined'
var y = 2; // Assigned y

// The above example is implicitly understood as this: 
var x = 1; // Assigned x
var y; // Declare y
console.log(x + " " + y); // '1 undefined'
y = 2; // Assigned y
```
#### Example 3 (IIFE - Immediately Invoked Function Expression)
```javascript
var x = 'outer scope';
(function() {
    console.log(x); //undefined
    var x = 'inner scope';
})();
// group operator forces a lexical scope
```
#### Example 4 (Function scope where declaration cannot make it above it's scope)
```javascript
var foo = 1;
function bar() {
    if (!foo) {
        var foo = 10;
    }
    console.log(foo); //10
}
bar();
//
var a = 1;
function b() {
    a = 10;
    return;
    function a() {}
}
b();
console.log(a); //1
```
#### Example 5 (Functions hoists before declaration, assignment happens at it's location）
```javascript
var a = 10;
console.log(a); //10
function a() {}
///
console.log(a); //[Function: a]
var a = 10;
function a() {}
```

#### Temporal Dead Zone (https://tinyurl.com/y9dmfnru)
- "`let` bindings are created at the top of the (block) scope containing the declaration, commonly referred to as "hoisting". Unlike variables declared with var, which will start with the value undefined, let variables are not initialized until their definition is evaluated. Accessing the variable before the initialization results in a ReferenceError. The variable is in a "temporal dead zone" from the start of the block until the initialization is processed."

#### hoisting + temporal dead zone
```javascript    
function do_something() {
  console.log(bar); // undefined
  console.log(foo); // ReferenceError
  var bar = 1;
  let foo = 2;
}
```

#### temporal dead zone + lexical scoping
```javascript    
function test(){
   var foo = 33;
   if (true) {
      let foo = (foo + 55); // ReferenceError
   }
}
test();
```
<br />

## 2. What is Closure? [:sushi:](https://github.com/lucidsushi/leet-code/blob/master/misc/javascript_top10.md#table-of-contents)

- "Closure is when a function is able to remember and access its lexical scope even when that function is executing outside its lexical scope."

- "Closures are nothing but functions with 'preserved' data"

#### Most Basic Closure
```
var a = 'stuff'
function blah(){
    console.log(a)  //stuff
}
```

#### Example 1 - Write a function that loops through an array and print it's index after a delay
```javascript
const arr = [10, 12, 15, 21];
for (var i = 0; i < arr.length; i++) {
  setTimeout(function() {
    console.log(i);
  }, 1000);
}
// 4 (FOUR TIMES).. anonymous function here is a closure
// Anonymous functions from setTimeout are "queued" only runs after the for loop is done (blocking event on call stack); and by then the `i` value is 4 as the result of the last `i++` which is accessible by the closure
// Hence, closure closes in the variable not the value(?)
```
##### Example 1 Cont' - Using `let` (no hoisting to the outside of for loop)
```javascript
const arr = [10, 12, 15, 21];
for (let i = 0; i < arr.length; i++) {
  setTimeout(function() {
    console.log(i);
  }, 1000);
}
// 0 1 2 3  prints as expected (each loop's function gets closed with a new `i`)
```
##### Example 1 Cont' - Using function factory (when a function returns an object) https://www.sitepoint.com/factory-functions-javascript/
```javascript
const arr = [10, 12, 15, 21];
for (var i = 0; i < arr.length; i++) {
  setTimeout(function() {
    return function(localized_i){
        console.log(localized_i);
    }
  }(i), 1000);
}
// 0 1 2 3 localized_i is passed in by value (as it's a primitive), which gives it a unique memory location (a different copy)
// https://codeburst.io/javascript-passing-by-value-vs-reference-explained-in-plain-english-8d00fd06a47c (sort of)
```

#### Example 2  - Private Counter
```javascript
function private_counter(){
    //  JAVASCRIPT
    var current_value = 0;
    return {
      add: x => current_value += x,
      retrieve_current: () => console.log(current_value)
    }
}

counter = private_counter();
counter.add(10);
counter.add(5);
counter.retrieve_current();
```

```python
def private_counter():
    # PYTHON (good example of pass immutable in by val and mutable in by reference(?))
      _count = [1]
    
      def add(x):
        _count[0] = _count[0] + x
        return _count
      
      def retrieve():
        print 'Current count is at', _count[0]
    
      return {'add': add,
              'retrieve': retrieve}

counter = private_counter()
counter['add'](5)
counter['add'](10)
counter['retrieve']()
#　Current count is at  16
```

#### Resources
- https://stackoverflow.com/questions/3572480/please-explain-the-use-of-javascript-closures-in-loops
- https://coderbyte.com/algorithm/3-common-javascript-closure-questions
- https://medium.freecodecamp.org/3-questions-to-watch-out-for-in-a-javascript-interview-725012834ccb
<br />

## 3. Implement TwoSum() [:sushi:](https://github.com/lucidsushi/leet-code/blob/master/misc/javascript_top10.md#table-of-contents)
- TwoSum(numbers, target) => (index1, index2), https://leetcode.com/problems/two-sum/
- [repo example](https://github.com/lucidsushi/leet-code/blob/master/001_algo_twosum.py)  
<br />

## 4. Implement Fibonacci()/Debounce() [:sushi:](https://github.com/lucidsushi/leet-code/blob/master/misc/javascript_top10.md#table-of-contents)
 ![Fibonacci](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/FibonacciSpiral.svg/220px-FibonacciSpiral.svg.png)
#### Fibonacci
  + array where current number is the sum of previous two numbers for a requested size of array
```javascript
function get_fibonacci_of_size(size){
  let sequence = [0, 1]

  if(size === 0){
    return []
  } else if (size === 1){
    return sequence[0]
  }
  for(let i=2; i<size; i++){
    const last_two_number = sequence[i - 1] + sequence[i - 2]
    sequence.push(last_two_number)
  }
  return sequence
}

console.log(get_fibonacci_of_size(8))

```
```python
def get_fibonacci_of_size(size):
  sequence = [0, 1]

  if size == 0:
    return []
  elif size == 1:
    return sequence[0]

  for i in range(2, size):
    last_two_number = sequence[i - 1] + sequence[i - 2]
    sequence.append(last_two_number)
  return sequence

print get_fibonacci_of_size(5)
```

#### Debounce
  + a wrapper function to make the inner function only run once (either at the start or end of the series) on a series of invocations 
```javascript
/**
 - (immediate = true, calls first invocation)
 - functionCall runs once only until a setTimeout() completes and timeout is set to null again
 - mutiple calls trigger clearTimeouts so timeout never is set to null unless one setTimeout() finishes
 - 
 - (immediate = false, calls last invocation)
 - functionCall runs after setTimeout() finishes
 - mutiple calls trigger clearTimeout on previous setTimeout()s therefore cancels them
 */
const debounce = (func, wait, immediate) => {
  let timeout
  return function(...arguments) {
    const functionCall = () => {
      timeout = null
      if (!immediate) func.apply(this, arguments)
    }
    if (immediate && !timeout) func.apply(this, arguments)
    clearTimeout(timeout)
    timeout = setTimeout(functionCall, wait)
  }
}

window.addEventListener('keyup', debounce((e) => {
  console.log(e);
}, 1000, true));
```
#### Resources
- https://davidwalsh.name/javascript-debounce-function
- [debounce-deep-dive-javascript-es6](https://medium.com/@TCAS3/debounce-deep-dive-javascript-es6-e6f8d983b7a1)

<br />

## 5. Implement Best Time to Buy and Sell Stock [:sushi:](https://github.com/lucidsushi/leet-code/blob/master/misc/javascript_top10.md#table-of-contents)
- https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
- [repo example](https://github.com/lucidsushi/leet-code/blob/master/121_algo_bestTimeToBuyAndSellStock.py)

<br />

## 6. More Scoping Question [:sushi:](https://github.com/lucidsushi/leet-code/blob/master/misc/javascript_top10.md#table-of-contents)

- EG. what will this output. Why?
```javascript
// first version
var myObject = {
    foo: "bar",
    func: function() {
        // console.log(this === window) //false
        var self = this;
        console.log("outer func:  this.foo = " + this.foo);
        console.log("outer func:  self.foo = " + self.foo);
        (function() {
            console.log("inner func:  this.foo = " + this.foo);
            console.log("inner func:  self.foo = " + self.foo);
        }());
    }
};
myObject.func();
```

```javascript
// myObject now a function myFunction
var myFunction = () => {
 //  console.log(this === window) //true
 this.foo = "window_foo"
 var self = this;
 return {
   foo: "bar",
   func: function() {
       //  console.log(this === window) //false
       this.foo = "object_func_foo"
       console.log("outer func:  this.foo = " + this.foo);
       console.log("outer func:  self.foo = " + self.foo);
       (function() {
           console.log("inner func:  this.foo = " + this.foo);
           console.log("inner func:  self.foo = " + self.foo);
       }());
   }
 };
} 
myFunction().func();
```

```javascript
// func: function() -> func: () =>
// arrow function take `this` context from enclosing scope
this.foo = 'window_foo'
var myFunction = () => {
 // console.log(this === window) //true
 // this.foo = "window_foo1"
 var self = this;
 return {
   foo: "bar",
   func: () => {
       // console.log(this === window) //true
       // this.foo = "window_foo2"
       console.log("outer func:  this.foo = " + this.foo);
       console.log("outer func:  self.foo = " + self.foo);
       (function() {
           console.log("inner func:  this.foo = " + this.foo);
           console.log("inner func:  self.foo = " + self.foo);
       }());
   }
 };
} 
myFunction().func();
```

<br />

## 7. Something Async [:sushi:](https://github.com/lucidsushi/leet-code/blob/master/misc/javascript_top10.md#table-of-contents)

```javascript
(function() {
    console.log(1); 
    setTimeout(function(){console.log(2)}, 1000); 
    setTimeout(function(){console.log(3)}, 0); 
    console.log(4);
})();

//1
//4
//3
//2
```
- https://alanthai.github.io/event-loop-lessons/#introduction
- [javascript-event-loop-explained](https://medium.com/front-end-hacking/javascript-event-loop-explained-4cd26af121d4)

<br />

## 8. What are Promises? [:sushi:](https://github.com/lucidsushi/leet-code/blob/master/misc/javascript_top10.md#table-of-contents)
- Promises are useful for avoiding callback hell
- Promises are useful for structuring asynchronous methods to return like synchronous methods
- Promises are objects useful for being proxies for the eventual success or failure of asynchronous method returns
- Promises are objects that takes an executor function which takes another two functions as arguments (resolve and reject)
![mdn promise flow](https://mdn.mozillademos.org/files/15911/promises.png)

**Using promises to handle asynchronous calls synchronously** 
```javascript
// Example One - Not using Promises
asyncFunctionOne()
asyncFunctionTwo()
console.log('Will be ran 3rd (Not using Promise)')
// Will be ran 3rd (Not using Promise)
// Will be ran 1st (Not using Promise)
// Will be ran 2nd (Not using Promise)

function asyncFunctionOne(){
  setTimeout(() => console.log('Will be ran 1st (Not using Promise)'), 0)
}
function asyncFunctionTwo(){
  setTimeout(() => console.log('Will be ran 2nd (Not using Promise)'), 0)
}
```
```javascript
// Example Two - Using Promises
(async function runAsync(){
  console.log(await promiseAsyncFunctionOne())
  console.log(await promiseAsyncFunctionTwo())
  console.log('Will be ran 3rd (Using Promise)')
})()
// Will be ran 1st (Using Promise)
// Will be ran 2nd (Using Promise)
// Will be ran 3rd (Using Promise)

function promiseAsyncFunctionOne(){
  return new Promise((resolve, reject) => {
    setTimeout(() => resolve('Will be ran 1st (Using Promise)'), 0)
  })
}
function promiseAsyncFunctionTwo(){
  return new Promise((resolve, reject) => {
    setTimeout(() => resolve('Will be ran 2nd (Using Promise)'), 0)
  })
}
```

**Using promises to escape callback hell**
```javascript
// Example One - Not using Promises

// When operations take time to complete, code execution order is not straight forward
(function asyncAdd(){

  let num1 = 1;
  let num2 = 2;
  let num3 = 3;
  let num4 = 4;
  let resultA;
  let resultB;
  let resultC;

  setTimeout(() => {
    resultA = num1 + num2
    console.log(`sumA is ${resultA}`)
    }, 90)

  setTimeout(() => {
    resultB = resultA + num3
    console.log(`sumB is ${resultB}`)
    }, 80)

  setTimeout(() => {
    resultC = resultB + num4
    console.log(`sumC is ${resultC}`)
  }, 70)
})()

// sumC is NaN
// sumB is NaN
// sumA is 3

// nested callbacks gives correct execution order but results in callback hell (not super obvious here)
(function asyncAdd(){

  let num1 = 1;
  let num2 = 2;
  let num3 = 3;
  let num4 = 4;
  let resultA;
  let resultB;
  let resultC;

  setTimeout(() =>{
    resultA = num1 + num2
    console.log(`sumA is ${resultA}`)

    setTimeout(() => {
      resultB = resultA + num3
      console.log(`sumB is ${resultB}`)

      setTimeout(() => {
        resultC = resultB + num4
        console.log(`sumC is ${resultC}`)
      }, 90)
    }, 80)
  }, 70)
})()

// sumA is 3
// sumB is 6
// sumC is 10
```
```javascript
// Example Two - Using Promises
(function asyncAdd(){

  let num1 = 1;
  let num2 = 2;
  let num3 = 3;
  let num4 = 4;

  let Add = (a, b) => {
    return new Promise((resolve) => {
      setTimeout(() => {
        console.log(`sum is ` + (a + b))
        resolve(a + b)
      }, 100)
    })
  }

  Add(num1, num2)
    .then((resolved) => Add(resolved, num3))
    .then((resolved) => Add(resolved, num4))

})()

// sum is 3
// sum is 6
// sum is 10

```

#### Resources
- [Youtube Techsith](https://www.youtube.com/watch?v=s6SH72uAn3Q)
- [Promises for Dummies](https://scotch.io/tutorials/javascript-promises-for-dummies)
- [Async Function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)

<br />

## 9. (Uncommon) == vs === [:sushi:](https://github.com/lucidsushi/leet-code/blob/master/misc/javascript_top10.md#table-of-contents)

- What is the difference between == and ===
```
== (abstract equality comparison) <- does type conversion
=== (strict equality comparison)  <- doesn't do type conversion
```
- [equality comparisons and sameness](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness)

- What will this output:
```javascript
console.log(1 == '1');
console.log(1 === '1');
console.log(0 == false);
console.log(0 == 'false');


//true
//false
//true
//false
```

<br />

## 10. (Uncommon) Floating Point Numbers [:sushi:](https://github.com/lucidsushi/leet-code/blob/master/misc/javascript_top10.md#table-of-contents)

- What will this output and why:
  +  console.log(0.1 + 0.2)
        *  (floating point number)
  +  console.log(0.1 + 0.2 + 0.3 === 0.3 + 0.2 + 0.1)
        *  (floating point number + order of operation)
  
-  0.1 base10 is 1/10, represented in binary =

    <img src="https://latex.codecogs.com/svg.latex?\Large&space;\frac{16}{2}+\frac{8}{2}+\frac{4}{2}+\frac{2}{2}+0+\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\frac{1}{16}+\frac{1}{32}"/>
    
        
                          0.  0   (0    0    1    1)...
- Storing in IEEE754 format
    
    ![Floating Point Schema (IBM)](https://www.ibm.com/developerworks/library/j-jtp0114/float.gif)
    
    **Sign bit (1 bit)** - "0"
    
        0 (positive number)
    
    **Exponent (8 bit)** - "01111011"
        
        -4 (has to store number in normalized form so it has to start from 1,  so in 0.00011 the decimal shifts four over to be 1.1...)
        127 (representing location for 0)
        127 - 4 = 123 = 01111011 (8 bit binary)

    **Mantissa/Fraction (23 bit)** - "10011001100110011001101"

        Store 23 bit starting from after the "1." (0.0(0011) is now 00001.1)
        1(0011)(0011)(0011)(0011)(0011)(00) | 1 <- the 24th bit rounds up
        1(0011)(0011)(0011)(0011)(0011)(01) <- Final result

    0.1 in base10 therefore becomes this format in IEEE754 binary32:

      0 01111011 10011001100110011001101
    
    which when convertd back to base 10 is about:

      0.100000001490116119384765625

- In Summary

  Going through the process for "0.2" would yield (in base10):

  0.20000000298023223876953125

  So 0.1 + 0.2 in binary32 becomes:

    0.100000001490116119384765625 +
    0.20000000298023223876953125    =
    0.300000004470348358154296875

  So console.log(0.1+02) != 0.3

#### Resources
- [floating point number](https://www.youtube.com/watch?v=PZRI1IfStY0)
- [IEEE754 binary 32](https://en.wikipedia.org/wiki/Single-precision_floating-point_format#IEEE_754_single-precision_binary_floating-point_format:_binary32)
- https://www.h-schmidt.net/FloatConverter/IEEE754.html

