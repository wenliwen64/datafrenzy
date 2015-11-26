Title: Flow Analysis in Heavy Ion Collisions
Date: 2015-11-24 12:15
Modified: 2015-11-24 12:15
Status: draft
Slug: flow
Authors: Liwen Wen

[TOC]

This article is based on the classic paper by Art&Sergei 1998. `/Users/lwen/gdrive/cve_papers/art_sergei.pdf` 

## What is flow?
----

Collective motion of produced particles in ultrarelativistic heavy ion collisions. It can refer to logitudinal expansion, radial transverse flow, transverse anisotropic transverse flow: directed flow, elliptic flow.  

## Why flow is imporatant? 
----

* relationship between appearance and development.  

## How to study flow?
----

### What we are going to observe?

Anisotropic transverse flow from particle azimuthal distribution withn fixed pseudorapidity/rapidity. The anisotropic particle distribution in the transverse plane can be expanded by Fourier series like below:

$$\frac{Ed^3N}{d^3p} = \frac{d^2N}{2\pi p_tdp_td\phi}(1 + \sum_{n=1}^{+\infty}2v_ncos(n(\phi-\Phi_r))$$($\Phi_r$ is the real reaction plane orientation)

The first order and second order coefficients are refered to as "directed flow" and "elliptic flow". Basic steps to study the flow phenomenon in heavy ion collisions are:

   1. Estimate the reaction plane orientation, the estimated one is called event plane;

   2. Evaluate the Fourier expansion coefficients with respect to the estimated event plane;

   3. Corrected the estimated coefficients by event plane resolution; (The finite particle number used to estimate the event plane introduces fluctuations("resolution") into the calculation which can be corrected by some tricks(by dividing the coefficient by event plane resolution), I will discuss this later.)

Notes: the resolution correction always makes the coefficients bigger since only along the real event plane direction the projection is the largest; another reason why this is of great importance is the corrected value can be used to compare with full phase-space theoretical prediction. 

### How to obtain the reaction plane orientation($\Phi_r$)?

So basically we use the anisotropic flow itself to estimate the event plane. In other words, it can be determined independently for each harmonic of the anisotropic flow.   

$$Q_n cos(n\Phi_n) = X_n = \sum_{i}w_i cos(n\phi_i),$$
$$Q_n sin(n\Phi_n) = Y_n = \sum_{i}w_i sin(n\phi_i),$$

So $X_n$ and $Y_n$ composes a event flow vector $\vec{Q_n}$. We can solve the $\Phi_n$ by:

$$\Phi_n = atan(\frac{\sum_{i}w_i sin(n\phi_i)}{\sum_{i}w_i cos(n\phi_i)}) / n.$$

Some comments on above equations:

   1. $w_i$ are weights, usually we use transverse momentum, the criterion is to make the resolution the best;

   2. Usually the weights for the odd and even harmonic planes are different(if particle azimuthal angle shifted by $\pi$, the distribution should remain the same! You can draw the two ions' peripheral collision, if you rotate $\pi$ you cannot tell the difference from original one. This is called reflection symmetry, so e.g. $cos(3(\phi-\Phi_3)) = - cos(-3(\phi-\Phi_3))$ ) 

   3. $\Phi_n$ is in the range $0\leq\Phi_n\leq2\pi/n$

### Event plane dist. flattening

Biases due to the finite acceptance of the detector which cause the particles to be azimuthally anisotropic in laboratory system. Due the laboratory A couple of methods(???):

   1. Recentering;
    
   2. Use the distribution of the particles themselves as a measure of the acceptance;

   2. Mixed-events;

   3. Fourier expansion of the raw event plane distribution and correct the angle event-by-event;

### Particle distribution with respect to the event plane: Imporatant

To evaluate $v_n$, you need to use the event plane orientation which is determined from any harmoic **m** , with $n\geq m$ and n is multiple of m, why? For example, if m = 2, n = 3, so $0 \leq \Phi_m \leq 2\pi/3$, then the $ -4\pi/3\leq2(\phi-\Phi_3) \leq 4\pi$ the range covered is not a multpile of $2\pi$, otherwise it may introduce some biases in some azimuthal range. 

For the event plane evaluated from the _m_th harmonic the Fourier expansion is:

$$\frac{wN}{d(\phi-\Phi_m)} = \frac{<wN>}{2\pi}(1+\sum_{k=1}^{\infty}2v_{km}cos[km(\phi-\Phi_m)])$$

From this equation, we can easily evaluate the $v_n$ by measuring $<cos[km(\phi-\Phi_m)]>$. One thing to be kept in mind is 

### Event plane resolution

The correction formula can be written as:

$$v_n = v_n^{obs}/<cos[km(\Phi_m - \Phi_r)]>$$

How to calculate the denominator? We better know the pdf of $m(\Phi_m-\Phi_r)$:

$$\frac{dP}{d[m(\Phi_m-\Phi_r)]} = \int\frac{v^{'}_mdv_m^{'}}{2\pi\sigma^2}\times exp(-\frac{v_m^2+v_m^{'2}-2v_mv_m^{'}cos[m(\Phi_m-\Phi_r)]}{2\sigma^2})$$

So from above, we can find there are two parameters involved in the distribution($v_m$, $\sigma$), where: 

$$\sigma^2 = \frac{<w^2>}{2N<w>^2}$$

which is inversely proportional to the square-root of **N**;

![]({attach}/plots/ep_resolution.png)

So pratically, we need to get sub-event plane resolution using:

$$<cos[k(\phi_{east} - \phi_{west})]> = <cos[k(\phi_{east} - \phi_r)]>\dot<cos[k(\phi_{west}-\phi_r)]>$$

Then map out the full event plane resolution by some tricks.
