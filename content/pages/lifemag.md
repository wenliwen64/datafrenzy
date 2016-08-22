Title: Task Management
Date: 2015-12-01 19:26
Slug: task-magnagement
Authors: Liwen Wen

[TOC]
# Questions to Answer: 
---
1. How to handle exceptions in C++ and python? ([link](https://www.youtube.com/watch?v=P_Kx0i7yXhU&list=PLfVsf4Bjg79Cx42Myce8bIg1nVBVSFKyx))

2. How to design good/reusable software? (design patterns)

3. How to properly use `const` key word in C++? 

      * 2016-03-20:
    
          1. In class definition, if you want this function not to change any data member, you should declare this function like `bool function(int i, int j) const;`     
 
          2. In function declaration, `const string&` will enable you to pass in not only a regular string variable but also the string literal. If you dont add `const` before `string`, it implicitly tells the compiler that the value will be changed so temporal object cannot be accepted(changes cannot be strored anywhere).  
       
          3. If you want a local variable not to be changed by any way.

4. Flow-related questions.(why 2nd order event plane can only be used for even correlation)

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

   8. Dynamic programming and greedy algorithms?(Take notes and practice)(MIT CS6.006 videos 4 lectrues on dynamic programming)

   9. How to develop unit-test code in Python and C++. Need examples and practice and interview questions.

   10. Know the fundamental concepts in Computer Operating Systems.

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

   22. VM usage

   23. Visulization.

# Books to read:
---
1. Quick view: Data Science from scratch

2. Machine learning in python(\*)

3. [Heads up design pattern(for interview preparation)](https://drive.google.com/file/d/0B3ZmSZ7JPYZ6RGtCa0hSSnRuVWc/view?usp=sharing)

4. Cracking the code interview

5. [Beauty of coding])(https://drive.google.com/file/d/0B3ZmSZ7JPYZ6anBjM2ZjU0ZLdGs/view?usp=sharing)

6. [Data structure and algorithms in C++](https://drive.google.com/file/d/0B3ZmSZ7JPYZ6LWxTUGY3X0JkVUk/view?usp=sharing)

# Courses to take:
---
0. CS32: Introduction to Computer ScienceII(project3/4 could be put on resume; webpages needed)

1. <del>Stochastic Process. Math171(2017 Spring)</del>Stochastic Process Math275C(2016 Spring)

2. CS33: Introduction to computer system(Open every quarter?)

3. Stat231: Machine Learning(2016-1017 Fall)(could be put on resume)

3. Stat202C: Monte Carlo for Optimization.(2017 Spring)(could be put on resume)

4. U. of Washington Specialization in Data Science. (2017 Spring to Summer, 6 courses)(could be put on resume)

5. C183: Statistical models in finance(2017 Spring)

# Logs:
---
* 2016-03-25: I want to learn(by the end of April): unitest in python for my framework; document my kaggle pipline; Greedy Algorithms([a quick view](https://www.youtube.com/watch?v=cu7TMYj0dBg)); Dynamic Programming...  

* 2016-03-27: Add code to normalize our feature data; how to organize the categorical data in svm application, normalization, like embark location in Titanic(1, 2, 3 for south ampton, ...)?

* 2016-04-04: Furbished my resume for two versions(quant/SE/DS).

* 2016-05-20: [blog](http://coolshell.cn/articles/12052.html); Backtracing(videos); On wechat, I saved a bookmark which tells about howto improve your python step by step.
