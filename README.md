# 50-days-of-restudying-js
Think you are confident with javascript? 
Here's 50 Days of restudying javascript. 

# Topics
- Preferrable practices
- Functional & declartive programming
- In-depth inspection: `Symbol`, `this`, `bind`, `WeakMap`, `WeakSet`, `Object`, `prototype`, `class`, `async`, `await`, and more. 

# Prerequisites
* Have read the latest edition of ["Learning javascript"](http://shop.oreilly.com/product/9780596527464.do) at least three times.
* Have read ["You Don't Know JS"](https://github.com/getify/You-Dont-Know-JS) at least once (roughly is ok)
* Have coded substantial amount of javascript already
* Now wanting to get some really fine techniques on javascript

# Table of Contents

   * [50-days-of-restudying-js](#50-days-of-restudying-js)
   * [Topics](#topics)
   * [Prerequisites](#prerequisites)
   * [Table of Contents](#table-of-contents)
   * [Day 1](#day-1)
      * [Clearing up questions for Day 1](#clearing-up-questions-for-day-1)
         * [1. Array.prototype.slice() in <a href="https://github.com/airbnb/javascript#arrays--from-array-like">4.5</a>:](#1-arrayprototypeslice-in-45)
         * [2. Array.from in <a href="https://github.com/airbnb/javascript#arrays--mapping">4.6</a>](#2-arrayfrom-in-46)
   * [Day 2](#day-2)
      * [Things that I think it would be hard to remember for Day 2](#things-that-i-think-it-would-be-hard-to-remember-for-day-2)
   * [Day 3](#day-3)
      * [Things that I find useful for Day 3](#things-that-i-find-useful-for-day-3)
   * [Day 4 (Started learning functional javascript)](#day-4-started-learning-functional-javascript)
      * [List of possible sources (I did not include sample code repos or fp libaries)](#list-of-possible-sources-i-did-not-include-sample-code-repos-or-fp-libaries)
         * [Books](#books)
         * [Articles](#articles)
         * [Others](#others)
   * [Day 5](#day-5)
      * [Notes for Chapter 1](#notes-for-chapter-1)
      * [Notes for chapter 2](#notes-for-chapter-2)
   * [Day 6](#day-6)
      * [Pure function](#pure-function)
      * [What's possible in pure functions](#whats-possible-in-pure-functions)
         * [1. Cache](#1-cache)
            * [Why is pure function important at all here?](#why-is-pure-function-important-at-all-here)
         * [2. Portable and self-documenting](#2-portable-and-self-documenting)
         * [3. Testable](#3-testable)
         * [4. Reasonable](#4-reasonable)
         * [5. Parallel code](#5-parallel-code)
   * [Day 7](#day-7)
      * [Currying](#currying)
      * [Currying examples](#currying-examples)
      * [Just one more example](#just-one-more-example)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)

# Day 1
Read [Airbnb's javascript style guide](https://github.com/airbnb/javascript):
* :hourglass:: 30 ~ 60 mins
* From [1. Types](https://github.com/airbnb/javascript#types) 
* To  [7.6 Never use arguments, opt to use rest syntax ...](https://github.com/airbnb/javascript#es6-rest)

## Clearing up questions for Day 1

### 1. `Array.prototype.slice()` in [4.5](https://github.com/airbnb/javascript#arrays--from-array-like): 

The `slice()` method returns a shallow copy of a portion of an array into a new array object selected from begin to end (end not included). The original array will not be modified.

* Q: `slice` works on objects?
* A: [Slice method can also be called to convert Array-like objects / collections to a new Array.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice#Array-like_objects). So you could do something like:
  ```js
  const info = Array.prototype.slice.call({0: "Korea", 1: "KST", length: 2})
  // ["Korea", "KST"]
  ```
  Remember you need to specify the length, and the object keys should be indices. The following would result in nothing but an empty array:
  ```js
  const info = Array.prototype.slice.call({home: "Korea", time: "KST"})
  // []
  ```
  But anyways, it's not recommended to use `Array.prototype.slice`, but `Array.from`.

  
### 2. `Array.from` in [4.6](https://github.com/airbnb/javascript#arrays--mapping)
  
* Q: So what can `Array.from` actually do with mapping? 
* A: This:  
  `Array.from` can receive a mapping function as the second argument, as such:
  ```js
  const mapped = Array.from([1,2,3], elem=>elem*2)
  // 2,4,6
  ```

# Day 2
Read [Airbnb's javascript style guide](https://github.com/airbnb/javascript):
* :hourglass:: 30 ~ 60 mins
* From [7.7 Use default parameter syntax...](https://github.com/airbnb/javascript#es6-default-parameters) 
* To [15.5 Use braces to create blocks in case and default clauses...](https://github.com/airbnb/javascript#comparison--switch-blocks) 

## Things that I think it would be hard to remember for Day 2
1. [14.2 Anonymous function expressions hoist their variable name, but not the function assignment.](https://github.com/airbnb/javascript#hoisting--anon-expressions)
2. [14.3 Named function expressions hoist the variable name, not the function name or the function body.](https://github.com/airbnb/javascript#hoisting--named-expressions)

# Day 3
Read [Airbnb's javascript style guide](https://github.com/airbnb/javascript):
* :hourglass:: 45 ~ 60 mins
* From [15.6 Ternaries should not be nested...](https://github.com/airbnb/javascript#comparison--nested-ternaries) 
* To [30.2 No, but seriously:](https://github.com/airbnb/javascript#testing--for-real) (The end)

## Things that I find useful for Day 3
* [18.4 You can use `FIXME` or `TODO` to annotate something in the comment.](https://github.com/airbnb/javascript#comments--actionitems)  
* [19.6 Use indentation when making long method chains...](https://github.com/airbnb/javascript#whitespace--chains)
* [21.1 Use semicolons.](https://github.com/airbnb/javascript#semicolons--required): You know, I don't really use semicolons in Javascript because the code tends to look cleaner. But airbnb certainly has suggested possible grounds for this, such as:
  * "rules will become more complicated as new features become a part of JavaScript. Explicitly terminating your statements and configuring your linter to catch missing semicolons will help prevent you from encountering issues."
  * But doesn't `prettier` do the job for filling out all the semicolons? I will have to dig into this a bit more. 
* [22.2 Type casting for strings: don't use new keyword, but just 'String', because using the new keyword will let javascript recognize the variable as an object. (typeof)](https://github.com/airbnb/javascript#coercion--strings)
* [23.4 Do not use trailing or leading underscores.](https://github.com/airbnb/javascript#naming--leading-underscore)
* [25.1 When attaching data payloads to events (whether DOM events or something more proprietary like Backbone events), pass an object literal (also known as a "hash") instead of a raw value. ](https://github.com/airbnb/javascript#events--hash)
* [29.1 Use `Number.isNaN` instead of `isNaN` (same for `Number.isFinite`)](https://github.com/airbnb/javascript#standard-library--isnan)

# Day 4 (Started learning functional javascript)

* :hourglass:: 20 mins
Gathered up some resources 

## List of possible sources (I did not include sample code repos or fp libaries)
### Books
* [Mostly adequate guide to FP](https://github.com/MostlyAdequate/mostly-adequate-guide)
* [Functional Light JS](https://github.com/getify/Functional-Light-JS)

### Articles
* [Short read on functional javascript: the good parts](https://github.com/seanhess/functional-javascript)
* [JavaScript Functional Programming Cookbook (ES6)](https://github.com/js-functional/js-funcional)
* [Real world functional programming in JS: Tips and guidelines for real world functional code-bases in JS](https://github.com/haskellcamargo/js-real-world-functional-programmingv)
* [ALDO FP Guide](https://github.com/aldo-dev/javascript)

### Others
* [Awesome functional programming (Really comprehensive!)](https://github.com/xgrommx/awesome-functional-programming)
* [List of awesome fp in js](https://github.com/stoeffel/awesome-fp-js)
* [Functional JavaScript Resources](https://github.com/jkup/functional-javascript)
* [Curation of resources in FP in javascript](https://github.com/busypeoples/functional-programming-javascript)

# Day 5
And so, I will look at those two books mentioned in Day 4.

* :hourglass:: 30 ~ 60 mins

## Notes for Chapter 1
* Read ['Chapter 1: What Ever Are We Doing?' of Mostly adequate guide to FP](https://github.com/MostlyAdequate/mostly-adequate-guide/blob/master/ch01.md)

* Many times we tend to write many more lines code than needed. If you think, and especially  **inFP way, you can greatly reduce the code to more exact, concise one.**
* Associative, commutative, identity, distributive rules work to further reduce the code (if you have done some math classes), like below (from chapter 1):
  ```js
  const add = (x, y) => x + y;
  const multiply = (x, y) => x * y;
  
  /* associative
   * Wiki link: https://en.wikipedia.org/wiki/Associative_property#Definition
   * Example: (x ∗ y) ∗ z = x ∗ (y ∗ z) for all x, y, z in S.(Multiplication)
   */
   
  add(add(x, y), z) === add(x, add(y, z));
  
  /* commutative
   * Wiki link: https://en.wikipedia.org/wiki/Commutative_property#Mathematical_definitions
   * Example: x * y = y * x for all x,y in S.
   */ 
   
  add(x, y) === add(y, x);
  
  /* identity
   * Wiki link: https://en.wikipedia.org/wiki/Identity_function#Definition
   * Example: f(x) = x for all x in certain domain.
   */
  
  add(x, 0) === x;
  
  /* distributive
   * Wiki link: https://en.wikipedia.org/wiki/Distributive_property#Definition
   * Example: x * ( y + z ) = (x * y) + (x * z)
   */
   
  multiply(x, add(y,z)) === add(multiply(x, y), multiply(x, z));
  ```
  
  apply these rules to reduce the code: 
  ```js
  // Original line
  add(multiply(flockB, add(flockA, flockC)), multiply(flockA, flockB));
  
  // Apply the identity property to remove the extra add
  // (add(flockA, flockC) == flockA)
  add(multiply(flockB, flockA), multiply(flockA, flockB));
  
  // Apply distributive property to achieve our result
  multiply(flockB, add(flockA, flockA));
  ```
* And that's only the beginning.

## Notes for chapter 2

* Read ['Chapter 2: First class functions' of Mostly adequate guide to FP ](https://github.com/MostlyAdequate/mostly-adequate-guide/blob/master/ch02.md)

* What is a first class function?: 
  > **A programming language is said to have First-class functions when functions in that language are treated like any other variable.** For example, in such a language, a function can be passed as an argument to other functions, can be returned by another function and can be assigned as a value to a variable. (From [Mozilla](https://developer.mozilla.org/en-US/docs/Glossary/First-class_Function))

  > **We can treat functions like any other data type and there is nothing particularly special about them** - they may be stored in arrays, passed around as function parameters, assigned to variables, and what have you. (From [the book](https://github.com/MostlyAdequate/mostly-adequate-guide/blob/master/ch02.md#a-quick-review))

* Often we write more code than needed:
  ```js
  // this line
  ajaxCall(json => callback(json));
  
  // is the same as this line
  ajaxCall(callback);
  
  // so refactor getServerStuff
  const getServerStuff = callback => ajaxCall(callback);
  
  // ...which is equivalent to this
  const getServerStuff = ajaxCall; // <-- look mum, no ()'s
  ```
  Now you can run `ajaxCall` with as many arguments as you want to put in. Just treat it like any other variables. That's the point.

* Note on naming functions: don't be too specific. Be broader so that you can use them for any other future projects. Make it reusable. 

# Day 6

* Read ['Chapter 03: Pure Happiness with Pure Functions' of Mostly adequate guide to FP ](https://github.com/MostlyAdequate/mostly-adequate-guide/blob/master/ch03.md)

* :hourglass:: 30 ~ 60 mins

## Pure function
> A pure function is a function that, given the same input, will always return the same output and does not have any observable side effect.

This is exactly the same principle for the definition of function in the world of real math: each input maps exactly to one (not several) output only. 

To make it easy to write a pure function, do not rely on the variables from outside world. 

You could 'freeze' or use other tools like [`immutable.js`](https://github.com/facebook/immutable-js/) to make sure that constant variables stay constant inside a function. 

## What's possible in pure functions 
### 1. Cache
Pure functions can be cached by input. This technique is sometimes called memoization:

> In computing, memoization or memoisation is an optimization technique used primarily to speed up computer programs by **storing the results of expensive function calls and returning the cached result when the same inputs occur again.**

So this would be a simple code for `memoize`:
```javascript
const memoize = (f) => {
  const cache = {};
  return (...args) => {
    const argStr = JSON.stringify(args);
    console.log(argStr)
    console.log(cache) // for help
    cache[argStr] = cache[argStr] || f(...args);
    return cache[argStr];
  };
};
```
This is only really a simple case for memoization. You simply store in `cache` object.

Let's have a multiply function memoized:

```javascript
multiply=memoize((x,y)=>x*y)
```

1st time you run it, you get: 
```
multiply(1,2)
[1,2]
{}
```

But the 2nd time you call it:
```
multiply(1,2)
[1,2]
{[1,2]: 2}
```

Your input and the corresponding output were stored in the cache and those were used instead of calculating the result by running the function once more.

#### Why is pure function important at all here?
Because if the function were impure, there's no point in saving the function output in the cache, as it does not have a guarantee that it is going to be the same each time.

### 2. Portable and self-documenting
```javascript
// impure
const signUp = (attrs) => {
  const user = saveUser(attrs);
  welcomeUser(user);
};

// pure
const signUp = (Db, Email, attrs) => () => {
  const user = saveUser(Db, attrs);
  welcomeUser(Email, user);
};
```
1. **Pure function is honest about its dependencies** (signature). You know exactly what to use. It's more informative. 
2. **You must use dependencies as function arguments.** Otherwise you've got no choice. It's more flexible and at the same time, self-documenting. But look at the impure version. You modify database and more without relying on the arguments. The logic is hidden behind.
3. **Pure function, likewise, is portable.** You can serialize/send over pocket. You can run your code anywhere. 

### 3. Testable
**Outputs are always predictable**. Therefore you don't have to:

> mock a "real" payment gateway or setup and assert the state of the world after each test.

You just need input and predict (assert) output in your tests.

### 4. Reasonable
**Referential transparency**. Codes can be substituted around because you already know that output of function will stay the same anyways.

You can use this property to easily refactor functions. For more, see [this part of the book](https://github.com/MostlyAdequate/mostly-adequate-guide/blob/master/ch03.md#reasonable).

### 5. Parallel code
Pure functions **do not need to access shared memory and cannot have a race condition due to side effects.**

# Day 7
* Read ['Chapter 04: Currying ](https://github.com/MostlyAdequate/mostly-adequate-guide/blob/master/ch04.md)

* :hourglass:: 30~60 mins

## Currying 

**Currying** is:

> In mathematics and computer science, currying is the technique of translating the evaluation of a function that takes multiple arguments into evaluating a sequence of functions, each with a single argument.

For example,
```javascript
curry((x,y) => x*y)
```
will get curried down to
```javascript
x => y => x*y
```

Similarly,

```javascript
curry((x,y,z) => x*y*z)
```
will get curried down to
```javascript
x => y => => z => x*y*z
```

Simple, right? Here's a [definition of `curry`](https://github.com/MostlyAdequate/mostly-adequate-guide/blob/master/appendix_a.md#curry):

```javascript
// curry :: ((a, b, ...) -> c) -> a -> b -> ... -> c

function curry(fn) {
  const arity = fn.length;
  return function $curry(...args) {
    if (args.length < arity) {
      return $curry.bind(null, ...args);
    }

    return fn.call(null, ...args);
  };
};
```

Let's inspect it. First change the code so that you can log outputs:
```javascript
function curry(fn) {
  const arity = fn.length;
  console.log(`arity: ${arity}`)
  return function $curry(...args) {
    console.log(`args: ${args}
args.length: ${args.length}`)
    if (args.length < arity) {
      return $curry.bind(null, ...args);
    }

    return fn.call(null, ...args);
  };
};
```

Now run:
```javascript
multiply=curry((x,y,z) => x*y*z)
```
It of course logs:
```
arity: 3
```

Then run the function:
```javascript
multiply(1,2,3)
```

Then it logs
```
args:1,2,3
args.length: 3
// returns
6
```

Cool. But what if `args.length < arity`? Let's try this out.
```javascript
const multiplyLast=multiply(1,2)
// logs
args: 1,2
args.length: 2
```
Now
```javascript
multiplyLast(3)
// logs
args: 1,2,3
args.length: 3
// returns
6
```

Wow. yeah. So you can actually stop the execution of function at certain point by manipulating the number of arguments. 

## Currying examples 
Now you can understand more of such functions:
```javascript
const match = curry((what, s) => s.match(what));
const replace = curry((what, replacement, s) => s.replace(what, replacement));
const filter = curry((f, xs) => xs.filter(f));
const map = curry((f, xs) => xs.map(f));
```

Look at [these usages](https://github.com/MostlyAdequate/mostly-adequate-guide/blob/master/ch04.md#cant-live-if-livin-is-without-you). Beautiful. You can mix them around, plug them into each other, do whatever you want essentially. 
```javascript
match(/r/g, 'hello world'); // [ 'r' ]

const hasLetterR = match(/r/g); // x => x.match(/r/g)
hasLetterR('hello world'); // [ 'r' ]
hasLetterR('just j and s and t etc'); // null

filter(hasLetterR, ['rock and roll', 'smooth jazz']); // ['rock and roll']

const removeStringsWithoutRs = filter(hasLetterR); // xs => xs.filter(x => x.match(/r/g))
removeStringsWithoutRs(['rock and roll', 'smooth jazz', 'drum circle']); // ['rock and roll', 'drum circle']

const noVowels = replace(/[aeiou]/ig); // (r,x) => x.replace(/[aeiou]/ig, r)
const censored = noVowels('*'); // x => x.replace(/[aeiou]/ig, '*')
censored('Chocolate Rain'); // 'Ch*c*l*t* R**n'
```

## Just one more example
instead of 
```javascript
const allTheChildren = elements => map(elements, getChildren);
```

you can do
```javascript
const getChildren = x => x.childNodes;
const allTheChildren = map(getChildren);
```

You can just directly transform the function into something that works on bunch of elements (array) instead of one element.