Title: sklearn Note
Date: 2015-12-09 00:23
Slug: sklearn-note
Authors: Liwen Wen

[TOC]
# Preprocessing

## Standarlization
SVM/L1, L2 regularizers of linear models assume that all features are centered around zero and have variance in the same order. 

Two approaches:

1. `sklearn.preprocessing.scale` and `sklearn.StandardScaler()`

The firest one will transform data to center around zero with unit variance.

The latter can reapply the same transformation to test dataset if tyou fit it to train data first.
# Regression

1. LassoCV 

    :::python
