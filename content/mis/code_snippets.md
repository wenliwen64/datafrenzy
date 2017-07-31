Title: LeetCode Notes
Date: 2015-12-21 17:01
Slug: leetcode-notes
Authors: Liwen Wen

[TOC]

# ## Binary Search Code

* Prob. 33

```cpp
// binary search to find the target in a array without duplicates
while(lo <= hi){
  mid = (lo + hi) / 2;
  if(target == array[mid]) return mid;
  else if(target > arry[mid]) lo = mid + 1;
  else hi = mid - 1;
}
```

