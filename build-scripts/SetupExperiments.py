## Set up all of the training experiments

import h2oai_client
import numpy as np
import pandas as pd
import requests
import math
from h2oai_client import Client, ModelParameters, InterpretParameters

address = 'http://52.90.67.220:12345'

username = 'training'
password = 'training'

h2oai = Client(address = address
               , username = username
               , password = password)

def splitTrainingData(dataPath, basename, target, ratio = 0.8, time=''):
	data = h2oai.create_dataset_sync(dataPath)
	# Split the data
	split_data = h2oai.make_dataset_split(
    	dataset_key = data.key
    	, output_name1 = basename + '_train'
    	, output_name2 = basename + '_test'
    	, target = target
    	, fold_col = ''
    	, time_col = time
    	, ratio = ratio
	)
	# key[0] is train, key[1] is test
	key = h2oai.get_dataset_split_job(split_data).entity
	return key

def makeTrainingModel(key, target, knobs, classify=True, scorer='AUC', drop=[]):
	experiment = h2oai.start_experiment_sync(
    	dataset_key = key[0]
    	, testset_key = key[1]
	    , target_col = target
	    , accuracy = knobs[0]
    	, time = knobs[1]
    	, interpretability = knobs[2]	
    	, is_classification = classify
    	, scorer = scorer
    	, enable_gpus = True
    	, cols_to_drop = drop
	)
	return experiment

### Titanic Models
dataPath = '/data/Training/Titanic.csv'
basename = 'Titanic'
target = 'survived'

TitanicKey = splitTrainingData(dataPath, basename, target)

## Runtime for Titanic1: 18 minutes
dropped = ['name2', 'cabin', 'embarked', 'boat', 'body', 'home.dest']
knobs = [8, 2, 8]
Titanic1 = makeTrainingModel(TitanicKey, target, knobs, drop=dropped)

## Runtime for Titanic2: 20 minutes
dropped = ['name', 'name2', 'cabin', 'embarked', 'boat', 'body', 'home.dest']
Titanic2 = makeTrainingModel(TitanicKey, target, knobs, drop=dropped)

## Runtime for Titanic3: 5 minutes
knobs = [6, 2, 8]
Titanic3 = makeTrainingModel(TitanicKey, target, knobs, drop=dropped)

### Boston Housing Models
## [6, 2, 8]: 7 minutes
## [8, 2, 8]: 26 minutes

dataPath = '/data/Training/BostonHousing.csv'
basename = 'Housing'
target = 'VALUE'

BostonKey = splitTrainingData(dataPath, basename, target)

knobs = [8, 2, 8]
Boston1 = makeTrainingModel(BostonKey, target, knobs, classify=False, scorer='RMSE')

knobs = [6, 2, 8]
Boston2 = makeTrainingModel(BostonKey, target, knobs, classify=False, scorer='RMSE')


### Diabetes
## 8 / 2 / 8 takes 8 minutes on big

dataPath = '/data/Training/DiabetesNA.csv'
basename = 'Diabetes'
target = 'Outcome'

DiabetesKey = splitTrainingData(dataPath, basename, target)

dropped = ['Pregnancies']
knobs = [6, 2, 8]
Diabetes1 = makeTrainingModel(DiabetesKey, target, knobs, drop=dropped)

knobs = [8, 2, 8]
Diabetes2 = makeTrainingModel(DiabetesKey, target, knobs, drop=dropped)

### Amaxon Reviews

dataPath = '/data/Training/AmazonFineFoodReviews.csv'
basename = 'Reviews'
target = 'PositiveReview'

ReviewsKey = splitTrainingData(dataPath, basename, target)

## Description only / 8,3,7 / 40 minutes on 8 GPU

dropped = ['UserID', 'ProductId', 'Id', 'Summary', 'Score', 'HelpfulnessDenominator', 'HelpfulnessNumerator', 'ProfileName', 'Time']
knobs = [6, 2, 7]
Reviews1 = makeTrainingModel(ReviewsKey, target, knobs, drop=dropped)

knobs = [8, 2, 7]
Reviews2 = makeTrainingModel(ReviewsKey, target, knobs, drop=dropped)

dropped = ['UserID', 'ProductId', 'Id', 'Score', 'HelpfulnessDenominator', 'HelpfulnessNumerator', 'ProfileName', 'Time']
knobs = [6, 2, 7]
Reviews3 = makeTrainingModel(ReviewsKey, target, knobs, drop=dropped)

dropped = ['Score', 'ProfileName', 'Time', 'Description']
knobs = [6, 2, 7]
Reviews4 = makeTrainingModel(ReviewsKey, target, knobs, drop=dropped)

dropped = ['Summary', 'Score', 'ProfileName']
knobs = [6, 2, 7]
Reviews5 = makeTrainingModel(ReviewsKey, target, knobs, drop=dropped)

### Cannabis Time Series
##
##  4/2/6, seed=212507590 120 days 0 gap : 7, 7, 7 minutes
## 4 / 2 / 6 , 28 days, 1 gap 7 minutes

experiment = h2oai.start_experiment_sync(dataset_key=train_dai.key,
                                         testset_key = test_dai.key,
                                         target_col="Weekly_Sales",
                                         is_classification=False,
                                         cols_to_drop = ["sample_weight"],
                                         accuracy=5,
                                         time=3,
                                         interpretability=1,
                                         scorer="RMSE",
                                         enable_gpus=True,
                                         seed=1234,
                                         time_col = "Date",
                                         time_groups_columns = ["Store", "Dept"],
                                         num_prediction_periods = 1,
                                         num_gap_periods = 0)
