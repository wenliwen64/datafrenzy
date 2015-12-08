Title: matplotlib Cheatsheet
Date: 2015-12-07 13:55
Slug: matplotlib-cheatsheet
Authors: Liwen Wen

[TOC]

# Primer
---

# python Visualization Ecosystem
---

1. Chaco: build interactive applications

2. For those familiar with ROOT, fig is like `TCanvas` object and axis is like `TH1D`

        :::python
	fig = plt.figure()
        fig, axes = plt.subplots(2, 2) 
        for axis in axes:
            axis.hist(np.random(50), nbins=20, color='black', alpha=.3)


