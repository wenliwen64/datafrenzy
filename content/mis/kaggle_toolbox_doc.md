Title: Kaggle Competition Toolbox Documentation
Date: 2016-03-26 17:52
Slug: kaggle-competition-toolbox-documentation
Author: Liwen Wen

[TOC]

# Directories Structure
---

     Kaggle_toolbox
      |
      |- raw_data # raw data and extracted 'y' and 'id'
      |   |
      |   |- test.csv
      |   |
      |   |- train.csv...
      | 
      |- src
      |   |
      |   |- general_to_xgb.py # used to convert genral format(for sklearn) of feature/label to DMatrix
      |   |
      |   |- generate_ens0.py # generate ens0 feature files 
      |   |
      |   |- generate_feature0.py # generate #0 features set
      |   |
      |   |- generate_train_y_and_id.py # generate train y and id 
      |   |
      |   |- train_predict_xgb.py # train and predict using xgb
      |
      |- build # store preprocessed data 
      |   |
      |   |- feature # preprocessed feature files go to this folder
      |   |   |
      |   |   |- feature0.test.feature # feature file for feature set0
      |   |   |
      |   |   |- ens0.train.feature # features used for ens0
      |   |
      |   |- test # predictions from test dataset 
      |   |   |
      |   |   |- xgb_10_0.1_0_0.5_0.4_80_feature0.test.y # predictions for test data set using feature set #0 and xgb algorithm with listed parameters
      |   |   | 
      |   |   |- xgb_10_0.1_0_0.5_0.4_80_feature0.test.soft.y # soft predictions(probability) for test dataset
      |   |
      |   |- val # predictions from training dataset
      |       |
      |       |- xgb_10_0.1_0_0.5_0.4_80_feature0.val.y
      |
      |- tests # test code goes to here
      |
      |- Makefile, Makefile.feature.ens0, Makefile.feature.feature0...
      

# How to Run 
---

1. `$make -f Makefile pre1` to extract `id` and `y`;

2. `$make -f Makefile.feature.feature0 feature0` to extract feature0 set for `xgb`, `sklearn`, `fm` and other different algorithms interfaces

3. `$make -f Makefile.xgb param_tuning_grid/param_tuning_rand/submission/train_predict` to do the prediction, you have to change the parameters at the beginning and the feature name in the `include` statement

# Logs:
---

1. 2016-03-26: Implement SVM and other algorithms
