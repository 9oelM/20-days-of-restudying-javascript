# js
studying javascript

## Day 1
Read [Airbnb's javascript style guide](https://github.com/airbnb/javascript):
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

## Day 2
Read [Airbnb's javascript style guide](https://github.com/airbnb/javascript):
* From [7.7 Use default parameter syntax...](https://github.com/airbnb/javascript#es6-default-parameters) 
* To [15.5 Use braces to create blocks in case and default clauses...](https://github.com/airbnb/javascript#comparison--switch-blocks) 

## Things that I think it would be hard to remember for Day 2
1. [14.2 Anonymous function expressions hoist their variable name, but not the function assignment.](https://github.com/airbnb/javascript#hoisting--anon-expressions)
2. [14.3 Named function expressions hoist the variable name, not the function name or the function body.](https://github.com/airbnb/javascript#hoisting--named-expressions)
