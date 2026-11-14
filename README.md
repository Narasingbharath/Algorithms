# Python Map and Reduce

This repository contains simple Python examples demonstrating the use of the `map()` and `reduce()` functions.

## 1. Map Function

The `map()` function applies a given function to every element in an iterable, such as a list.

### Examples

- Add 2 to each number.
- Multiply each number by 5.
- Find the square of each number.

**Example input:**
```python
numbers = [1, 2, 3, 4, 5]
```

**Output:**
```text
[3, 4, 5, 6, 7]
[5, 10, 15, 20, 25]
[1, 4, 9, 16, 25]
```

## 2. Reduce Function

The `reduce()` function applies a function cumulatively to the elements of an iterable and produces a single result.

It is available in Python through the `functools` module.

### Examples

- Calculate the sum of all numbers.
- Calculate the product of all numbers.
- Calculate the sum of squares of all numbers.

**Example input:**
```python
numbers = [1, 2, 3, 4, 5]
```

**Output:**
```text
15
120
55
```

## Concepts Learned

- Python functions
- Lists and iteration
- `map()` function
- `reduce()` function
- `functools` module
- Difference between transformation and aggregation

## Purpose

This repository was created as part of my learning journey to understand Python programming concepts and build a foundation for learning MapReduce and Hadoop.

**Language:** Python
