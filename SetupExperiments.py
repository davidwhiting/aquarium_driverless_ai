## Set up all of the training experiments

import h2oai_client
import numpy as np
import pandas as pd
# import h2o
import requests
import math
from h2oai_client import Client, ModelParameters, InterpretParameters

address = 'http://54.80.1.64:12345'

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

