Title: Coursera Logisitic Regression Notes
Date: 2015-11-21 4:09
Slug: coursera-logistic-regression-notes
Status: draft
Authors: Liwen Wen

[TOC]

#Logistic Regression

* No linear regression for classification

* Decision Boundary is drawn from hypothesis function after fitting the $\theta$ parameters

* Hypothesis Function:

   $$h(x) = \frac{1}{1+e^{-\theta^Tx}}$$

* Cost Function: convex is important->that is why we use log()
   
   $$Cost(h_{\theta}(x), y) =\frac{1}{m}\sum\limits_{i}^{m} (-y_ilog(h_\theta(x_i)) - (1-y_i)log(1-h_{\theta}(x_i))$$

  if $y = 0$:
   
   $$Cost(h_{\theta}(x), y) = -log(1-h_{\theta}(x))$$
   
  so, if $h_{\theta}(x) = 0$, the cost function will be close to zero; if $h_{\theta}(x) = 1$, the cost function will be go infinitiy.
   
  if $y = 1$:
   
   $$Cost(h_{\theta}(x), y) = -log(h_{\theta}(x))$$
   
  so if $h_{\theta}(x) \sim 0$, the cost function would be infinity while it will be zero if $h_{\theta}(x) \sim 1$
   
  if we plot the plot for y=1/0, its convex and intuitive.

3. Advanced Optimization instead of Gradient Descent
   - Gadient descent
   - Conjugate gradient
   - BFGS
   - L-BFGS

   Advantages:
   
   * No need to manually pick alpha
   * faster than GD(gradient descent)

   Disadvantage:
    
   * More complex

4. Multiple-Classification:

   One vs all method, make one against the remainder 
   max over i for $\max\limits_{i}h_{\theta}^i(x)$
   
5. Regulization: 
   - why? To deal with overfitting problemn(e.g.$J_\theta = \frac{1}{2m}\sum\limits_{i=1}^m(h_\theta(x_i)- yi)^2+1000\theta_3^2+1000\theta_4^2$))
   - Intuition: small values for all parameters;
       - "simpler" hypothesis;
       - less prone to overfitting;
   - General form:
   $$J_\theta = \frac{1}{2m}\sum\limits_{i=1}^m((h_\theta(x_i)- yi)^2+\lambda\sum\limits_{i=1}^{m}\theta_{i}^2)$$(no $\theta_0$) where $\lambda$ is the regularization parameter, which stands for the tradoff between two goals:
   
      - fit the training data;
      - make paramters small(prevent overfitting);
   - Normal Equation:

   ![](http://i.imgur.com/64qtYj8.png)
       - invertibility:

   ![](http://i.imgur.com/Z2YQOzK.png)

6. Decision Boundary Plotting:
   - only 2 parameters: $\theta^Tx = 0$

7. Pratical Usage:

   Though it is called "Regression", it is used to classification rather than regression. In scikit-learn implementation, the difference from above is its cost function:

   * L2 regularization:

   $$min_{w, c}\frac{1}{2}w^Tw + C\sum_{i}^{n}log(exp{-y_i(X_i^Tw+c)}+1)$$

   * L1 regularization:

   $$min_{w, c}||w||_1 + C\sum_{i}^{n}log(exp{-y_i(X_i^Tw+c)}+1)$$

Observing this expression, we can find, if the hypothesis function is the same($h(\theta, x) = \frac{1}{1+e^{-\theta^Tx}}$), if $y_i = 1$, the second part is going to be huge if $h=0$, because $h=0$ means $\theta^Tx$ is negatively huge, but zero if $h=1$; if $y_i=-1$: 1. $h=1$-> $\theta^Tx$ is huge, cost is huge; 2. $h=0$, $\theta^Tx$ is negatively huge, so cost is zero.   

Take home messages:

   * Example: `sklearn.linear_model.LogisticRegression(penalty='l2', C=1.0, fit_intercept=True, solver='liblinear', max_iter=100, multi_class='ovr', n_jobs=1)`:

      1. penalty: l1 may fit sparse weights;
 
      2. C: iverse of the regulization term;

      3. fit_intercept: $w_0$, the constant term;

      4. solver: 'liblinear'-l1 and l2 penalty and suits for small dataset, and two class classification; 'lbfgs' or 'newton-cg' can be used for multiple classification but only l2 regularization; 'sag' suits for large dataset(stochastic average gradient descent)

      5. max_iter: used to set the maximum iteration required to get the minimal of cost function;

      6. multi_calss: 'ovr' and 'multinomial', works only for 'lbfgs'.  
   
   * The cost function is assumming the labels are -1 and 1, but you dont have to provide your targets by converting them to -1/1. When you are running 'clf.fit(x, y)', this job will be done under the hood. 

   * Stochastic gradient descent can be done by using `sklearn.linear_model.SGDClassifier(loss='log')`, this is suitable for large dataset. Why this is the same, the secret is hidding behind `\theta^Tw`, two label will be converging to two infinities both for svm(`loss='hinge'`) or logistic
