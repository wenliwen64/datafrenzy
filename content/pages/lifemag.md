Title: Task Management
Date: 2015-12-01 19:26
Slug: task-magnagement
Authors: Liwen Wen

[TOC]
# Questions to Answer: 
---
1. How to handle exceptions in C++ and python? (try catch...)

2. How to design good/reusable software? (design patterns)

3. How to properly use `const` key word in C++? 

      *2016-03-20
    
      1. In class definition, if you want this function not to change any data member, you should declare this function like `bool function(int i, int j) const;`     
 
      2. In function declaration, `const string&` will enable you to pass in not only a regular string variable but also the string literal. If you dont add `const` before `string`, it implicitly tells the compiler that the value will be changed so temporal object cannot be accepted(changes cannot be strored anywhere).  
       
      3. If you want a local variable not to be changed by any way.

4. Flow-related questions.

5. Chiral symmetry broken?

6. How to write a solver(analysis pipline and kaggle solver)

7. How to exercise my database skills(SQL)? 

8. Figure out how SU(3) is related to QCD, etc. 

# Skills to develop:
---
## Coding: 
---

   1. Data analysis in python.pandas?? (work through Python for data analysis exercise, 45 mins every day)

      * 2016-03-20: will do in next quater with Kaggle examples.

   2. C++ development knowledge?(work through the thinking in C++ exercise, 45 mins every day)

      * 2016-03-20: no need. Just pick some time to read it through. Finished CS32, which is great, check out some notes of that course on this site.

   3. Develop Algorithms understanding, and start coding leet code.

      * 2016-03-20: need to check algorithm course on coursera(Prof. Roughgarden, Standford), but we still can go through old videos.       

   4. Develop my own bash shell script cheatsheet.(shell_script_cheatsheet.md)  

   5. Develop a database server for chiral effects data points. 

   6. How to do parallel computing in sckit-learn? Multithreaded?

      * 2016-03-20: need to look into it soon.

   7. Read through XGB python test framework and [this](http://docs.python-guide.org/en/latest/writing/tests/)

## Machine Learning:
---
  
   1. Reading book in physics machine learning, and write notes about the examples. (odd weekday, 45 mins before bed) 

   2. Review and reformat the previous notes on Introduction to Machine Learning. (Fridays, 1 hr)

   3. Long term goal is to read through the Elements of Statistical Learning / Pattern Reconigtion, take notes() 

   4. Learn to use KDE,

   5. `itemgetter()`

   6. `sklearn.GridSearchCV(clf, param_grid, nfold = 20); grid_search.fit; grid_search.grid_scores_` can be used for grid search. But, random search may result in same result(60 times).: The moral of the story is: if the close-to-optimal region of hyperparameters occupies at least 5% of the grid surface, then random search with 60 trials will find that region with high probability. 

   7. Learn to use `os` module

   8. write note on how to install sklearn-neuralnetwork

   9. How to use OneHotEncoder in practice

   10. How to use multi-thread feature of scikit-learn

   11. xgb early stopping

   12. Pearson correlation

   13. Randomize predictor selection to see the effect*

   15. Center and normalize your data

   16. Left-out-one encoding

   17. When to use standardlization

   18. Keras/Theano/Lasagne/FM algorithm/

   19. Regularized greedy tree.(Tong Zhang's)

   20. Two talks on data science: Owen Zhang's Linkedin and Jeon-yoon Lee's Kaggler.com
 
   21. Feature importance selection

# Books to read:
---
1. Quick view: Data Science from scratch

2. Machine learning in python(\*)

# Courses to take:
---
1. Stochastic Process. Math171(2017 Spring)

2. CS33(...)

3. Stat231(2017 Fall)

3. Stat202C: Monte Carlo for Optimization.

4. U. of Washington Specialization in Data Science. (2017 Spring to Summer, 6 courses)

5. C183: Statistical models in finance
