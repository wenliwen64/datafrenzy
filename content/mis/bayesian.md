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

Likelihood: $L(m_0|m_t) = \frac{1}{\sqrt{2\pi\sigma^2}}exp(\frac{-(m-m_t)^2}{2\sigma^2})$

The likelihood is differing from pdf is it considers $m_t$ is changeing given the particular datum $m = m_0$. So usually the measured value is take as the value maximizing the likelihood $L$ or equivelently $ln L$. So rub comes in chossing how to extract errors(C.L.), especially when it is not parabolic.

Classical take: 
__Standard Deviation is only meaningful to normal distribution!__

Since our goal is to estimate the parameters($m_t, \sigma$) of function $g(m_t, \sigma_{50}) = \frac{1}{\sqrt{2\pi\sigma_{50}^2}}exp(-\frac{(m-m_t)^2}{2\sigma_{50}^2})$ 

Note the difference between above equation and the single observation p.d.f., basically, we are assuming the mean value is obeying the normal distribution, so if we can get the optimal variance $\sigma$ for one-time observation, we can get the $\sigma_{50} = \frac{\sigma}{\sqrt{50}}$ which is accounting for the standard deviation of the results we repeat this experiment with 50 observations many times again. So basically if we report our result like: $m_t = 40.0 \pm 0.5$ with many many observations per experiment, we are equally saying if we repeat this experiment 1000 times, about 680 out of them will yield results falling within that range. This is also why we may increase statistics to make our result more precise(decrease the standard deviation). All of these are based on Gaussian distribution assuption. 
Take home message: no matter what p.d.f. it is for single observation, the experiment results will bedistributed normally, and the mean value is the Maximum Likelihood estimator distribution, and $\sigma$ is the variance estimator $E[x^2] - E[x]^2$, since likelihood function is the estimator p.d.f which will coverges to normal distribution. Refer to Cowan's Statistical Data Analysis page 75(exponential decay example's variance computation).. 

$$ln L(\hat{\theta}\pm N\sigma_{\hat{\theta}}) = ln L_{max} - N/2$$ Central Limit Theorem
# Classical vs. Bayesian approach to represent confidence level


# Example I. Neutrino Mass Measurement

Some collaboration reported result like "$m^2 = -56\pm$"

