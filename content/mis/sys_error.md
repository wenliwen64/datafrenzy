Title: Treatment of systematic error in high energy physics and astrophysics
Date: 2016-05-23 13:13
Slug: systematic-error
Authors: Liwen Wen
---
[TOC]

# Papers:
---
1. Pekka K. Sinervo: Definition and treatment of systematic uncerntainties in high energy physics and astrophysics

2. Robert Cousins: Probability density functions for positive nuisance parameters. 

# Drive home message:
---

## Systematic Error Taxonomy:

TypeI: essencially statistical error(like acceptance of a detector which could be determined by other measturement which is dominated by statistics)

TypeII: like background events: we can assume a $p(x_i|\theta)$(and then the maximum likelihood result, $L(\theta) = \times p(x_i|\theta)$), here theta could be the mass of a new particle or cross-section of a given interaction, then sometime we may have background counts whichcould be represented effectively by nuisance parameter $$\lambda$$, so the pdf becomes $p(x_i|\theta, \lambda)$(and then $L(\theta, \lamba)$), if we assume $\lambda$'s pdf is gamma or lognormal(see Robert's paper, he suggest try all of the methods), we can get marginal pdf of $\theta$ in form of maximum likelihood function. (Also you can assume prior of $\theta$ then you are using pure baysian)

TypeII: theoretical assumptions(I don't really understand or have no picture in my head)
