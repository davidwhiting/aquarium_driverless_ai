
import h2oai_client
import numpy as np
import pandas as pd
# import h2o
import requests
import math
from h2oai_client import Client, ModelParameters, InterpretParameters

address = 'http://18.234.58.12:12345'

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
