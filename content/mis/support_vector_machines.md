Title: Support Vector Machine
Date: 2015-12-25 17:38
Slug: support-vector-machine
Authors: Liwen Wen

[TOC]

# Support Vector Machines
- - -

1. Hypothesis: 
    $$h_\theta(x) = 1 \text{ if } \theta^Tx\geq 0; 0 \text{ otherwise}$$

2. Two new functions:
   
   ![](http://i.imgur.com/zT5H5pv.png)

1. Optimization Objective:

    $$\min\limits_{\theta}C\sum\limits_{i=1}^{m}[y^i\text{cost1}(\theta^Tx)+(1-y^i)\text{cost0}(\theta^Tx)] + \frac{1}{2}\sum\limits_{i=1}^{n}\theta_i^2$$

# SVM with Kernels
- - -

Usually we choose Gaussian kernel and use training data points as landmarks to compute feature $f_i = e^{-\frac{||x-l_i||}{2\sigma^2}}$
1. Hypothesis: Given x, compute features $f \in R^{m+1}$, predict $y_i=1$ if $\theta^Tf \geq0$

2. Loss Function: 

    $$\min\limits_{\theta}C\sum\limits_{i=1}^{m}[y^i\text{cost1}(\theta^Tf)+(1-y^i)\text{cost0}(\theta^Tf)] + \frac{1}{2}\sum\limits_{i=1}^{m}\theta_i^2$$

3. Poly kernel： $k(x, l) = (x^Tl+constant)^degree$ so two parameters.

4. More kernels: String kernel(string classification), chi-square kernel, chi-square kernel, histogram intersection kernel chi-square kernel, histogram intersection kernel...

# SVC(Support Vector Classifier) in scikit-learn

Example:

Takehome message:

    1. Tune gamma(if 'rbf' kernel is set);

    2. Tune C(regularization);

    3. Preprocessing your data to [0, 1] or [-1, 1] or {$\mu$: 0, $\sigma$: 1} 

    4. 'class_weight'(SVC only): used for unbalanced data(way more positives than negatives)
2. Large Margin Classifier(SVM)(C is very large, emphasize the first term in cost function, may overfit for outlier)

    5. Before passing your data to SVC, make sure your array is C-ordered contiguous by `nparray.types`
    - how to represent the decision boundary on two features plots(linearly separatable)

    ![](http://i.imgur.com/k172HG8.png)

    - why this optimization leads to large margin classifier?
3. MATH behind tlarge margin classification
    - vector inner product:
    - imagine, if C is large(less likely to be biased, but high variance), the optimization is becoming obj = $$\min\limits_{\theta}\frac{1}{2}\sum\limits_{j=1}^n\theta_j^2 = \frac{1}{2}||\theta||$$, s.t. $$\theta^Tx^i\geq1, if y^i=1$$ and $$\theta^Tx^i\leq-1 if y^i = 0$$, i means the condition should be satisfied by each data point(x, y), see how svm choose decision boundary
    - how svm choose decision boundary:

    ![](http://i.imgur.com/eskggHA.png)
    
4. Kernels I
   - Non-linear decision boundary:
   - Kernel: given x, compute new feature depending on proximity to landmarks($$l^1, l^2, l^3$$):
   
   Given x: $$f_1 = exp(-\frac{||x-l^1||^2}{2\sigma^2})$$....similarity function, kernel(k(x, $$l^i$$)), Gaussian kernels
   
   Example: ![](http://i.imgur.com/R4m0zTX.png)
   
5. Kernel with SVM
   - use training point as landmarks,
   - for each training data point , get a new set of coordinates($$\vec{f}$$)
   ![](http://i.imgur.com/36gqgFW.png)
   - Hypothesis: Given x, compute features f(m+1 dimensions), predict positive if $$\theta^Tf\geq0$$$\
   - Training: $$\min\limits_{\theta}C\sum\limits_{i=1}^{m}y^icost_1(\theta^Tf^i)+(1-y^i)cost_0(\theta^Tf^i) + \frac{1}{2}\sum\limits_{i=1}^{m}\theta_i^2$$
   - kernels for logitics regression lack tricks in SVM
   - SVM parameters:
       - C(1/lambda): large C-low bias and high variance; small C-higher bias, low variance
       - $$\sigma^2$$: large-vary more smoothly, higher bias, lowervariance and verse visa
6. Using an svm:
   - need to specify: choice of parameterC; choice of kernel(no kernel = linear kernel, n large, m small, nolinear may overfit):
       - if Gaussian kernel, you should choose sigma squre(n small, m large): do perform feature scaling before using the Gaussian kernel;
       - other choice of kernel: need to satisfy called Mercer's Theorem to make SVM packages' optimizations run correctly;
       - very rare to use other kernels: polynomial kernal($$k(x, l) = (x^Tl+c)^n$$, two parameters, c and n, only when x, l non-negative); more esoteric(string kernel, chi-square, histogram intersection kernel)
   - Multi-class classification: many svm packages already have built-in mc classification functionality, otherwise, use one-vs.-all, pick classi with larges $$(\theta^i)^Tx$$
   - Logistic regression vs. SVMs:
       - n= no. of features, m = no. of training examples:
       - n is small, m is intermediate, use svm with Gaussian kernel(up to 50000), if n is small, m is large, /add more features , then use l-r or svm or svm with linear kernel(convex optimization for all svm but not for neural network)
       - otherwise(n is large) neural network works in most settings, but slow
