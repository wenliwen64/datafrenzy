Title: Frequencist or Bayesian for a nuclear experimentalist
Date: 2015-12-11 17:50
Slug: frequencist-or-bayesian-for-a-nuclear-experimentalist
Authors: Liwen Wen

[TOC]

What problem is this note aiming to answer?

__Problem__: How to construct confidence level for measured quantities? 

This note is based on the paper written by Robert Cousins`$/home/lwen/gdrive/ml_particle/bayesian.pdf`

# Problem of measuring mass
When we measure an elementary particle's mass, the measuring aparatus yields values($m$) normally distributed around true mass $m_t$, the pdf can be expressed this way:

$$p(m|m_t) = \frac{1}{\sqrt{2\pi\sigma^2}}exp(\frac{-(m-m_t)^2}{2\sigma^2})$$

So normally, we want to construct a confidence interval $(m_1, m_2)$ at a specified confidence level(C.L.). In this note, we take it to be 68%.

## Classical C.L.(Neyman, 1937): 

No matter what $m_t$ is , __if we do many many same experiments and construct C.L. each time, 68% of the those C.L.s will cover the true value.__ 

If we assume $m$ follows p.d.f. of normal distribution with mean $m_t$ and standard variance $\sigma$, the likelihood function will be like: $L(m_0, m_1, ...m_n|m_t) = \prod_{i=0}^{n}\frac{1}{\sqrt{2\pi\sigma^2}}exp(\frac{-(m_i-m_t)^2}{2\sigma^2})$

The likelihood is differing from pdf is it considers $m_t$ is changing given the particular data set $m_i$. Usually the measured value is taken as the value maximizing the likelihood $L$ or equivelently $ln L$. So the rub comes in chossing how to extract errors(C.L.), especially when it is not parabolic.

##Classical take: 

Two Case Studies:

###Case I. Exponential Distribution
Actually, if we measure the isotope decay rate, we can find the distribution is exponential decay $f(t) = e^{-t/\tau}$, and the likelihood function finally will yield $\frac{\sum t_i}{n}$ for the estimate of parameter $\tau$:

$$ln L(t_i|\tau) = ln(\frac{1}{\tau^n}e^{-\frac{\sum t_i}{\tau}}) = -nln(\tau) - \frac{\sum t_i}{\tau}$$

If we compute the derivative of this function we can find the maximum is reached when $\tau = \frac{\sum t_i}{n}$. Similarly, if the mean value of $t_i$ is obeying Gaussian distribution and it's variance also can be compute analytically by $var[\tau] = E[\tau^2] - E[\tau]^2$, since we know the likelihood function, this expression can be evaluated exactly and it turns out $\tau^2/n$, so use the prevously measured $\tau$, we can get 68% C.L. interval. The normal question regarding this precedure is why this variance is correct? Because the mean value is following Gaussian distribution, so we can think this way: the likelihood function is the approximation of final Gaussian function, we use analytical expression to get the relationship between the know parameter$\tau$ and invisible parameter $\sigma$. 

###Case II. Gaussian Distribution
Assuming the measured mass $m$ from this experiment(from likelihood method) is obeying Gaussian distribution, our goal transforms to estimate the parameters($\sigma_mean$) of function:

$$g(m_{mean}) = \frac{1}{\sqrt{2\pi\sigma_{mean}^2}}exp(\frac{-(m_{mean}-m_t)^2}{2\sigma_{mean}^2})$$

The likelihood method yields results $\hat{m_t} = \sum m_i/Nobs$ and $\sigma_{mean} = \sum(m_i-\hat{m_t})^2 / n$. This case differs from last one in computation of variance of result. In this example, the sigma value is obtatined by maximizing the likelihood function while last one used analytical calculation. In most cases, a p.d.f.'s variance is not a separate parameter to be estimated, so analytical approach is a more comman way to evaluate the result's standard deviation(error) by assuming it's following Gaussian distribution.  

Note the difference between above equation and the single observation p.d.f., basically, we are assuming the mean value is obeying the normal distribution, so if we can get the optimal variance $\sigma$ for one-time observation, we can get the $\sigma_{50} = \frac{\sigma}{\sqrt{50}}$ which is accounting for the standard deviation of the results we repeat this experiment with 50 observations many times again. So basically if we report our result like: $m_t = 40.0 \pm 0.5$ with many many observations per experiment, we are equally saying if we repeat this experiment 1000 times, about 680 out of them will yield results falling within that range. This is also why we may increase statistics to make our result more precise(decrease the standard deviation). All of these are based on Gaussian distribution assuption. 
Take home message: no matter what p.d.f. it is for single observation, the experiment results will bedistributed normally, and the mean value is the Maximum Likelihood estimator distribution, and $\sigma$ is the variance estimator $E[x^2] - E[x]^2$, since likelihood function is the estimator p.d.f which will coverges to normal distribution. Refer to Cowan's Statistical Data Analysis page 75(exponential decay example's variance computation).. 

$$ln L(\hat{\theta}\pm N\sigma_{\hat{\theta}}) = ln L_{max} - N/2$$ Central Limit Theorem
## Bayesian take: 
We can construct posterior(to-estimate parameter's distribution):

$$P(m_t|m) = L(m|m_t)\times P(m_t)/\int L(m|m_t)P(m_t)dm_t$$

So if we take prior as uniform distribution, we can simplify the expression like: 

$$P(m_t|m) \sim L(m|m_t)$$

So we can construct C.L. from this posterior. 

![](http://i.imgur.com/npYKraF.png)

From the above plots, we can find if we are measuring a mass which in no way to be negative, we can construct the posterior as shown in plot3, so that we can normalize that function to get final distribution. Then the C.L. can be constructed easily, since posterior is already the p.d.f. of the measuring parameters.  

# Example I. Neutrino Mass Measurement

Some collaboration reported result like "$m^2 = -56\pm$"

