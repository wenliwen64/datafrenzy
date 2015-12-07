Title: Python for Data Analysis Notes
Date: 2015-12-05 16:14
Slug: python-for-data-analysis-note
Authors: Liwen Wen

[TOC]

This note is based on Python For Data Analysis written by Wes McKinney

# Chapter1. Preliminaries
- - -

1. Why python for data analysis? Ans: pandas + general purpose programming strength. 

2. Glue:??

3. Domain-specific language-MATLAB, R, oftentimes, people will do research, prototype and test new ideas using R or MATLAB and then later port these ideas to a larger production system written in Java/C++. Python can do both, making scientists and technologist use same programatic tools.   

4. When to avoid Python? Parallel computing, ??? Multithreded and process, cpu-bounded thread.

5. Essential Python Libraries:

   * NumPy: ndarray, element-wise computations, read/write array-based data sets to disk, linear algebra operations, FFT, random number generators, tools to connect C/C++/Fortran code to Python; ndarray is used to pass data between algorithms.

   * pandas: rich data structures and functions. Major data structure->DataFrame, a two dimensional tabular, column-oriented data structure with both row and column labels. Combines SQL and numpy's advantages. Sophisticated indexing functionality. 

   * matplotlib: generate publication quality plots.

   * IPython: enhanced Python shell and accelerate the writting and testing and debugging of Python code. 

   * SciPy: a collection of packages addressing a number of different standard problem domains in scientific computing, `scipy.integrate`, `scipy.linalg`, `scipy.optimize`, `scipy.signal`, `scipy.sparse`, `scipy.special`, `scipy.stats`, `scipy.weave`...Together with NumPy, they form a reasonably complete computational replacement for much of MATLAB along with some of its add-on toolboxes.

# Chapter5. Getting Started With pandas
- - -

1. 2 mostly used data types: Series, DataFrame. We can view DataFrame as a dict of Series. So basically you can construct a DataFrame like:
    * `df = DataFrame({'a':[1, 2, 3], 'b' : ['CA', 'NY', 'NV']}`
    * `df = DataFrame({'a': {1: 1, 3:3}, 'b': {1: 'CA', 2: 'NY', 3: 'NV'}})` the outer key is the column and inner one is row

2. Retrieve rows/columns: `row = df.ix['a']` or ``

3. For code like `df[df['Name'] == 'Bob', 'Sex'] = 1` can index using boolean array like `{False, True, True...}`. This is how this kind of expression indices  

4. Apply function and mapping: 

        :::python 
        f = lambda x: x.max() - x.min()
        df.apply(f, axis = 0) # axis = 0(column-wise, 1 is row-wise) is default, you can omit it in your practice 
        df['animals'] = df['food'].map(lambda x: meat_to_animal[x.lower()])

5. Confusion about the axis definition:
    
        :::python
        df.mean(axis=1) # apply the mean method on each row, and get the value to show on screen
        df.drop(['Name', 'ID', 'Fare'], axis=1) # apply the drop action on each row, i.e., for each row, drop the corresponding labels.

6. Some tips on indexing into DataFrame:
   
        :::python
        data = df['Age'].iloc[i] # is used to retrieve ith row, 'Age' column
        data = df[i, 'Age'] # Wrong, illegal.
        data = df.loc[i, 'Age'] # Correct

