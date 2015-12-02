Title: Python Cheatsheet
Date: 2015-12-01 23:34
Slug: python-cheatsheet
Authors: Liwen Wen
Status: draft

[TOC]

This cheatsheet is based on the book Writing Idiomatic Python. by Jeff Knupp.

# Control Structure

1. `if x <= y <= z:` is legal and efficient;

2. `is_generic_name = name in ('Tom', 'Dick', 'Harry')` = `if name == 'Tom' or name == 'Dick' or name == 'Harry'` 

3. `if my_list:` instead of `if my_list == []:`

4. `if position is not None:`

5. `value = 1 if foo else 0` just like `x? True:False` in C++ 

* for loop(???format function):

    :::python
    for index, element in enumerate(my_contaniter):
        print('{} {}'.format(index, element))

7. Mutable objects: list, dict, set and most class instances

8. Immutable objects: string, int, tuple

9. Dont use mutable object as the default value for a function argument.`def f(a, L=None)` instead of `def L(a, L=[])` 

10. Return expression instead of values to be concise.`return a == b == c`  
