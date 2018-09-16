#### Table of Contents

#### [1. What is Hoisting?](https://github.com/lucidsushi/leet-code/blob/master/misc/javascript_top10.md#1-what-is-hoisting-sushi)

#### [2. What is Closure?](https://github.com/lucidsushi/leet-code/blob/master/misc/javascript_top10.md#2-what-is-closure-sushi)

#### [3. Implement TwoSum()](https://github.com/lucidsushi/leet-code/blob/master/misc/javascript_top10.md#3-implement-twosum-sushi)

#### [4. Implement Fibonacci / Debounce](https://github.com/lucidsushi/leet-code/blob/master/misc/javascript_top10.md#4-implement-fibonaccidebounce-sushi)

#### [5.Implement Best Time to Buy and Sell Stock](https://github.com/lucidsushi/leet-code/blob/master/misc/javascript_top10.md#5-implement-best-time-to-buy-and-sell-stock-sushi)

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
// Not a clear example as to why it prints 4 four times, probably related to some asynchronous/event loop/que fundamentals
// Anonymous functions from setTimeout are only run after the for loop is done; and by then the `i` value is 4 as a result of the last `i++` before the loop ends
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
- [repo example](https://github.com/lucidsushi/leet-code/blob/master/121_algo_bestTimeToBUyAndSellStock.py) 
