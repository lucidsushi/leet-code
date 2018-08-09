<!-- Javascript -->

1. What is Hoisting?

    "Variable binding created at the top to the (block for let/const) scope (function scope) containing the delcartion"

    "Hoisting was thought up as a general way of thinking about how execution contexts (specifically the creation and execution phases) work in JavaScript. However, the concept can be a little confusing at first.
    Conceptually, for example, a strict definition of hoisting suggests that variable and function declarations are physically moved to the top of your code, but this is not in fact what happens. Instead, the variable and function declarations are put into memory during the compile phase, but stay exactly where you typed them in your code."

    "JavaScript only hoists declarations, not initializations. If a variable is declared and initialized AFTER using it, the value will be undefined"

    <!-- Examples -->

    #1
    console.log(num); // Returns undefined 
    var num;
    num = 6;

    num = 6;
    console.log(num); // returns 6
    var num;

    #2
    var x = 1; // Initialize x
    console.log(x + " " + y); // '1 undefined'
    var y = 2; // Initialize y

    // The above example is implicitly understood as this: 
    var x = 1; // Initialize x
    var y; // Declare y
    console.log(x + " " + y); // '1 undefined'
    y = 2; // Initialize y

    #3 (IIFE - Immediately Invoked Function Expression)
    var x = 'outer scope';
    (function() {
        console.log(x); //undefined
        var x = 'inner scope';
    })();

    #4 Function scope where declaration cannot make it above it's scope
    var foo = 1;
    function bar() {
        if (!foo) {
            var foo = 10;
        }
        console.log(foo); //10
    }
    bar();
    ================
    var a = 1;
    function b() {
        a = 10;
        return;
        function a() {}
    }
    b();
    console.log(a); //1

    #5 Functions hoists before declaration, assignment happens at it's location
    var a = 10;
    console.log(a); //10
    function a() {}
    ================
    console.log(a); //[Function: a]
    var a = 10;
    function a() {}


    (https://tinyurl.com/y9dmfnru)
    Temporal Dead Zone
    let bindings are created at the top of the (block) scope containing the declaration, commonly referred to as "hoisting". Unlike variables declared with var, which will start with the value undefined, let variables are not initialized until their definition is evaluated. Accessing the variable before the initialization results in a ReferenceError. The variable is in a "temporal dead zone" from the start of the block until the initialization is processed.

    <!-- hoisting + temporal dead zone -->
    function do_something() {
      console.log(bar); // undefined
      console.log(foo); // ReferenceError
      var bar = 1;
      let foo = 2;
    }

    <!-- temporal dead zone + lexical scoping -->
    function test(){
       var foo = 33;
       if (true) {
          let foo = (foo + 55); // ReferenceError
       }
    }
    test();


2. What is Closure?

    "Closure is when a function is able to remember and access its lexical scope even when that function is executing outside its lexical scope."

    "Closures are nothing but functions with 'preserved' data"

    <!-- Examples -->

    const arr = [10, 12, 15, 21];
    for (var i = 0; i < arr.length; i++) {
      setTimeout(function() {
        console.log('The index of this number is: ' + i);
      }, 1000);
    }

    // The index of this number is: 4 (FOUR TIMES)

    // Not a clear example as to why it prints 4, probably related to some asynchronous/event loop/que fundamentals


    https://stackoverflow.com/questions/3572480/please-explain-the-use-of-javascript-closures-in-loops

    https://coderbyte.com/algorithm/3-common-javascript-closure-questions