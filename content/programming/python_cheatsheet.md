Title: Python Cheatsheet
Date: 2015-12-01 23:34
Slug: python-cheatsheet
Authors: Liwen Wen

[TOC]

This cheatsheet is mainly based on the book Writing Idiomatic Python. by Jeff Knupp.

### Control Structure

* `if x <= y <= z:` is legal and efficient;

* `is_generic_name = name in ('Tom', 'Dick', 'Harry')` is equivalent to: 

        :::python
        if name == 'Tom' or name == 'Dick' or name == 'Harry':
            is_generic_name = True

* `if my_list:` instead of `if my_list == []:`

* `if position is not None:`

* `value = 1 if foo else 0` just like `x? True:False` in C++ 

* for loop(???format function):

        :::python
        for index, element in enumerate(my_contaniter):
            print('{} {}'.format(index, element))

* Mutable objects: list, dict, set and most class instances

* Immutable objects: string, int, tuple

* Dont use mutable object as the default value for a function argument.`def f(a, L=None)` instead of `def L(a, L=[])` 

* Return expression instead of values to be concise.`return a == b == c`  

* `if not 'happy' in cur_dict: ` is equivalent to happy is not in the current dictionary.  

* Why use `if __name__ == '__main__': `

### Dealing with data

* No reason to use temporary variable to swap varibles' values: `(b, a) = (a, b)`

* Chain string functions: `formatted_book_info = book_info.strip().upper().replace(":", "by")`

* Use `''.join(result_list)`

* Use `ord` function to convert char to ASCII or vice versa.

* How to format strings in python:
      * use `+` operator to concatenate strings and variables.
      * 'old-style' string
      * `''.join(string_list)` 

*  The best way to do is to use `output = 'Name: {user.name}, Age: {user.age}, Sex: {user.sex}'.format(user=user)`. This [link](https://docs.python.org/2/library/string.html#formatspec) is very helpful.

* `some_list = [element + 5 for element in some_other_list if is_prime(element)]`

* Prefer list comprehensions to the built-in `map()` and `filter()` functions

* Use `sum()` function which is built-in

* Use `all(list)` or `any(list)` to check if all of the elements or any one element is equal to `True`

* Use a dict as a substitue for a `switch`...case statement. return long expression is preferred.  

* `log_severity = configuration.get('severity', 'Info')`

* `user_email = {user.name: user.email for user in users_list if user.email}` 
* Set operations `A|B, A&B, A-B, A^B`  
* `return(set(get_list_of_most_active_users()) & set(get_list_of_most_popular_users()))`

* `users_first_names = {user.first_name for user in users}`

* How to define a variable arguments function: 

        :::python 
        In [0]: def foo(*args, **kwargs):
          ...:      for a in args:
          ...:          print a;
        
        In [1]: foo(1, 2, 3)
        1
        2
        3
        In [7]: def bar(*args, **kwargs):
                    for a in kwargs:
                        print(kwargs[a])
           ...:      
        In [8]: bar(1,2,3)
        
        In [9]: bar(num1=1,num2=2,num3=3)
        1
        2
        3

* P48 example very impressive

* `(user, name, _, _) = get_user_info(user)` is better than `(user, name, temp, temp2) = get_user_info(user)`

* tuple can be used to accept upacked list. `(name, age, sex) = list_from_comma_separated_file` 

* `return (mean, median, variance)` to return multiple values from one fucntion. 

* Reread class part. Very helpful but hard at this point of time(https://www.jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/)

* `for uppercase_name in (name.upper() for name in usernames)` is better than `for uppercase_name in [name.upper() for name in usernames]`

### Organize Your Code
- - -

* Use capital letters when declaring global constant values. 

* Format your code according to PEP8. `$sudo easy_install pep8` and `$pep8 myfirstpythonprogram.py`!

* `from foo import *` << `from foo import (a, b ,c, d)` < `import foo`

* Make use of `__init__.py` to initialize your package. If you have a package contating large amount of modules but only a few of them are meant to be used by clients, you should use `__init__.py`: like `import gzimo.clinet as Gzimo`, so client can write like `import Gzimo` instead of nested expressions.

* Use `if __name__ == '__main__'` to make a script executable.

* Under `if __name__ == '__main__'` you should write `sys.exit(main())`

* Use `sys.argv` to parse command line parameters

* Use `os.path` to deal with directory paths.

* Use automated test tool like the standard library providing `unittest` should suffice

* Use `self.assertEqual(a, b)` instead of `self.assertTrue(a == b)`

### Structure of your code

* What a typical project look like structurally? 

        :::python
        README
        environment.yml
        Makefile
        setup.py
        src/__init__.py
        src/core.py
        src/helpers.py
        docs/conf.py
        docs/index.rst
        tests/test_basic.py
        tests/test_advanced.py

* What is the use of `environment.yml` ?  `conda env create -f environment.yml`

* What is the use of `Makefile`? An example is:

        :::Makefile
        test: 
        	test.py test
        .PHONY: test

* What is the use of `setup.py`? 

     `python setup.py build && python setup.py install` == `make && make install` 

* What is the use of `__init__.py`? This file will be loaded and executed when any module of this package, some top-level statements will be executed. After this, it will look for the `core.py` to execute the statements in `core.py`. But usually it is left empty.
