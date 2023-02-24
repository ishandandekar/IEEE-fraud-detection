# IEEE Fraud Detection

Imagine standing at the check-out counter at the grocery store with a long line behind you and the cashier not-so-quietly announces that your card has been declined. In this moment, you probably aren’t thinking about the data science that determined your fate.

Embarrassed, and certain you have the funds to cover everything needed for an epic nacho party for 50 of your closest friends, you try your card again. Same result. As you step aside and allow the cashier to tend to the next customer, you receive a text message from your bank. “Press 1 if you really tried to spend $500 on cheddar cheese.”

## Problem Statement

According to given competition data, we have to predict that an online transaction is fraudulent, as denoted by the binary target variable.

> "In this competition, you’ll benchmark machine learning models on a challenging large-scale dataset. The data comes from Vesta's real-world e-commerce transactions and contains a wide range of features from device type to product features. You also have the opportunity to create new features to improve your results."

## Data

In this competition you are predicting the probability that an online transaction is fraudulent, as denoted by the binary target **`isFraud`**.

The data is broken into two files identity and transaction, which are joined by `TransactionID`. Not all transactions have corresponding identity information.

#### Categorical Features - Transaction

- ProductCD
- card1 - card6
- addr1, addr2
- P_emaildomain
- R_emaildomain
- M1 - M9

#### Categorical Features - Identity

- DeviceType
- DeviceInfo
- id_12 - id_38

The `TransactionDT` feature is a timedelta from a given reference datetime (not an actual timestamp).

#### Files

- **train\_{transaction, identity}.csv** - the training set
- **test\_{transaction, identity}.csv** - the test set (you must predict the isFraud value for these observations)

> **Note** : To know more about data, go to [Kaggle.com](https://www.kaggle.com/competitions/ieee-fraud-detection/discussion/101203)

## Modelling experiments

The data had various numerical and categorical features. They were filled with null values (_irony_). Using various feature transformation and imputation methods I achieved **0.9227 test ROC AUC score** using a Random Forest model. To see more about the data analysis, preprocessing steps, head over to [notebooks](notebooks).

## References

- https://github.com/KaustuvDash/IEEE-Fraud-Detection
- https://www.kaggle.com/competitions/ieee-fraud-detection/discussion/101203
- https://www.kaggle.com/competitions/ieee-fraud-detection/discussion/111308
