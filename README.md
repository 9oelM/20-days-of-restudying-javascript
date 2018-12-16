# rjs
(re)studying javascript

Table of Contents
=================

   * [rjs](#rjs)
      * [Prerequisites](#prerequisites)
      * [Day 1](#day-1)
      * [Clearing up questions for Day 1](#clearing-up-questions-for-day-1)
         * [1. Array.prototype.slice() in <a href="https://github.com/airbnb/javascript#arrays--from-array-like">4.5</a>:](#1-arrayprototypeslice-in-45)
         * [2. Array.from in <a href="https://github.com/airbnb/javascript#arrays--mapping">4.6</a>](#2-arrayfrom-in-46)
      * [Day 2](#day-2)
      * [Things that I think it would be hard to remember for Day 2](#things-that-i-think-it-would-be-hard-to-remember-for-day-2)
      * [Day 3](#day-3)
      * [Things that I find useful for Day 3](#things-that-i-find-useful-for-day-3)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)

# Prerequisites
* Have read the latest edition of ["Learning javascript"](http://shop.oreilly.com/product/9780596527464.do) at least three times.
* Have read ["You Don't Know JS"](https://github.com/getify/You-Dont-Know-JS) at least once
* Have coded substantial amount of javascript already
* Now wanting to get some really fine techniques on javascript

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