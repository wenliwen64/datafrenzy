Title: Python Cheatsheet
Date: 2015-12-01 23:34
Slug: python-cheatsheet
Authors: Liwen Wen

[TOC]

This cheatsheet is mainly based on the book Writing Idiomatic Python. by Jeff Knupp.

# Control Structure

1. `if x <= y <= z:` is legal and efficient;

2. `is_generic_name = name in ('Tom', 'Dick', 'Harry')` = 

        :::python
        if name == 'Tom' or name == 'Dick' or name == 'Harry':
            is_generic_name = True

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

11. `if not 'happy' in cur_dict: ` == happy is not in the current dictionary.  

12. Why use 'if \_\_name\_\_ == '\_\_main\_\_': ' 

# Dealing with data

1. No reason to use temporary variable to swap varibles' values: `(b, a) = (a, b)`

2. Chain string functions: `formatted_book_info = book_info.strip().upper().replace(":", "by")`

3. Use `''.join(result_list)`

4. Use `ord` function to convert char to ASCII or vice versa.

5. How to format strings in python:

    i. use `+` operator to concatenate strings and variables.
   
    ii. 'old-style' string

    iii. `''.join(string_list)` 

    The best way to do is to use `output = 'Name: {user.name}, Age: {user.age}, Sex: {user.sex}'.format(user=user)`. This [link](https://docs.python.org/2/library/string.html#formatspec) is very helpful.

6. `some_list = [element + 5 for element in some_other_list if is_prime(element)]`

7. Prefer list comprehensions to the built-in `map()` and `filter()` functions

8. Use `sum()` function which is built-in

9. Use `all(list)` or `any(list)` to check if all of the elements or any one element is equal to `True`

10. Use a dict as a substitue for a `switch`...case statement. return long expression is preferred.  

11. `log_severity = configuration.get('severity', 'Info')`

12. `user_email = {user.name: user.email for user in users_list if user.email}` 
13. Set operations `A|B, A&B, A-B, A^B`  
14. `return(set(get_list_of_most_active_users()) & set(get_list_of_most_popular_users()))`

15. `users_first_names = {user.first_name for user in users}`

16. How to define a variable arguments function: 

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

17. P48 example very impressive

18. `(user, name, _, _) = get_user_info(user)` is better than `(user, name, temp, temp2) = get_user_info(user)`

19. tuple can be used to accept upacked list. `(name, age, sex) = list_from_comma_separated_file` 

20. `return (mean, median, variance)` to return multiple values from one fucntion. 

21. Reread class part. Very helpful but hard at this point of time(https://www.jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/)

22. `for uppercase_name in (name.upper() for name in usernames)` is better than `for uppercase_name in [name.upper() for name in usernames]`

# Organize Your Code
- - -

1. Use capital letters when declaring global constant values. 

2. Format your code according to PEP8. `$sudo easy_install pep8` and `$pep8 myfirstpythonprogram.py`!

3. `from foo import *` << `from foo import (a, b ,c, d)` < `import foo`

4. Make use of `__init__.py` to initialize your package. If you have a package contating large amount of modules but only a few of them are meant to be used by clients, you should use `__init__.py`: like `import gzimo.clinet as Gzimo`, so client can write like `import Gzimo` instead of nested expressions.

5. Use `if __name__ == '__main__'` to make a script executable.

6. Under `if __name__ == '__main__'` you should write `sys.exit(main())`

7. Use `sys.argv` to parse command line parameters

8. Use `os.path` to deal with directory paths.

9. Use automated test tool like the standard library providing `unittest` should suffice

10. Use `self.assertEqual(a, b)` instead of `self.assertTrue(a == b)`

5. 
