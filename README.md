# 🎾 Tennis Prediction 🎾

For those who loves Machine Learning and Tennis, come and see! In this notebook we show how to build from scratch a classifier that predicts the outcome of a Tennis match.

To perform this task we use Tennis data from 2000 to 2016 in order to predict macthes' outcome of 2017. Here are all the information about the scraped raw data we used to build this tennis predictor: [dataset description](http://www.tennis-data.co.uk/notes.txt)

Our final purpose is to build a betting strategy that can have a positive ROI 👑. We explored 2 betting strategies and were able to find a lucrative one.

![](https://github.com/Matyyas/Tennis-Prediction/blob/main/img/cumulative_profit.png)


## Installation

```
git clone git@github.com:Matyyas/Tennis-Prediction.git
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

## Table of Contents of the notebook

<a name="desc"></a>
#### I. 🏗️ Data Preparation Process

<a name="usage"></a>
#### II. 🤖 Modeling Phase

<a name="usage"></a>
#### III. 🔎 Observation

<a name="usage"></a>
#### IV. 💰 Trying to make some € out of our predictions

<a name="usage"></a>
#### V. 🚀 Further improvements


## Reproduce best results
Our best models and training datasets can be found in the resources folder.

**Datasets**:
- **normalize_data_2016.csv**: normalized dataset for an evaluation on 2016
- **normmalize_data_2017.csv**: normalized dataset for an evaluation on 2017

**Models**:
- **best_model**: best found model during the Training/Validation phase on the data from 2000-2015
- **final_model**: final model trained during the Training/Evaluation phase with the parameters of our best_model on the data from 2000-2016

## References
[1] [Machine Learning for the Prediction of Professional Tennis Matches](https://www.doc.ic.ac.uk/teaching/distinguished-projects/2015/m.sipko.pdf) from Michal Spiko

[2] [Machine Learning for Professional Tennis Match Prediction and Betting](http://cs229.stanford.edu/proj2017/final-reports/5242116.pdf) from Andre Cornman, Grant Spellman, Daniel Wright

[3] [Kaggle: Beat the bookmaker](https://www.kaggle.com/edouardthomas/beat-the-bookmakers-with-machine-learning-tennis/notebook) from Edouard Thomas
