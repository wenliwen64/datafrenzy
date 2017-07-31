Title: Coding Interview Preparation
Date: 2017-07-31 12:20
Slug: leetcode-preparation
Authors: Liwen Wen

[TOC]

This blog entry will be used to record the lessons I learn through my preparation process for coding interview.

### 2017-07-30

1. Palindrome Partitioning II (132):

The problem I met is the TLE if I used a two dimension table. The solution is create isPalindrome table before fill the main dp table.

2. Distinct Subsequences (115):

The return value should be considered more carefully. Of course this is based on the dp table design.

3. 2 Keys Keyboard (650): 

This problem is hard for me. The key is understand in each cell of dp table, the cache should be the divisor of the cell number. This is the key.

4. Find Duplicate Subtrees (652):

The key is use the (post-order) serialization of the tree to represent and compare the trees. Recursion. 

5. Binary Tree Zigzag Level Order Traversal (103)

A lot errors: a. push and push\_back for stack and queue; b. pointer or instance use `.` or `->`, be careful!; c. return;  d. better solution is you can pop until the levelis totally out, then count the size of the queue to determine how many to pop. 
