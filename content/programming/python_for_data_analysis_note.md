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
    * `df = DataFrame({'a':[1, 2, 3], 'b':['CA', 'NY', 'NV']}`
    * `df = DataFrame({'a': {1: 1, 3: 3}, 'b': {1: 'CA', 2: 'NY', 3: 'NV'}})` the outer key is the column and inner one is row

2. Retrieve rows/columns: `row = df.ix['a']` or ``

3. For code like `df.loc[df['Name'] == 'Bob', 'Sex'] = 1`, we can understand this in python.pandas to reference elements. can exploit boolean array like `{False, True, True...}`.

4. Apply function and mapping: 

        :::python 
        f = lambda x: x.max() - x.min()
        df.apply(f, axis = 0) # axis = 0(column-wise, 1 is row-wise) is default, you can omit it in your practice 
        df['animals'] = df['food'].map(lambda x: meat_to_animal[x.lower()])

        #Another example is 
        df_train_age['Sex'] = df_train_age['Sex'].map({'female': 0, 'male': 1}).astype(int)

        #Below is less professional
        #df_train_age.loc[df_train_age['Sex'] == 'femal', 'Sex'] = 0

5. Confusion about the axis definition:
    
        :::python
        df.mean(axis=1) # apply the mean method on each row, and get the value to show on screen
        df.drop(['Name', 'ID', 'Fare'], axis=1) # apply the drop action on each row, i.e., for each row, drop the corresponding labels.

6. Some tips on indexing into DataFrame:
   
        :::python
        data = df['Age'].iloc[i] # is used to retrieve ith row, 'Age' column
        data = df[i, 'Age'] # Wrong, illegal.
        data = df.loc[i, 'Age'] # Correct

7. To distinguish axis in pandas, you should consider below examples:
  
        :::python
        In [0]: df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]})
     
        In [1]: np.mean(df, axis=0)
        Out[0]:
        col1    2
        col2    5
        col3    8
        dtype: float64
     
        In[2]: df.mean(axis=1) 
        Out[9]: 
        0    4
        1    5
        2    6
        dtype: float64

        In[3]: df.drop('col3', axis=1) 
        Out[11]: 
       	   col1  col2
        0     1     4
        1     2     5
        2     3     6

    So basically, you can understand this way: if `axis = 0`, you apply the
    actions to each column(it will not succeed if the action is not legal),
    if `axis = 1`, then the action will be applied on each row. 

8. Let's still take 7th item as an example:

        :::python
        In [20]: df[df['col1'] == 1]
        Out[20]: 
              col1  col2  col3
        0     1     4     7

    So `df['col1'] == 1` is like a `pandas.Series` of booleans:
    
        :::python
        n [21]: df['col1'] == 1
        Out[21]: 
        0     True
        1    False
        2    False
        Name: col1, dtype: bool

9. Binary logical operations:

        :::python
        df_train_age = df_final[~np.logical_or(df_final['Age'].isnull(), df_final['Fare'].isnull())].copy()
        # Not  below
        df_train_age = df_final[~(df_final['Age'].isnull() or df_final['Fare'].isnull())].copy()

10. `df.values` will return a numpy array([[row]]). If followed by a `tolist()` method, you will get a nested list
