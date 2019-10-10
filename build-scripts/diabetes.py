import h2oai_client
import numpy as np
import pandas as pd
import requests
import math
from h2oai_client import Client, ModelParameters, InterpretParameters

ip = '35.175.227.14'
address = 'http://' + ip + ':12345'
username = 'training'
password = 'training'

h2oai = Client(address = address
               , username = username
               , password = password)


### Diabetes Models
dataPath = '/data/Training/PimaDiabetes.csv'
basename = 'Diabetes'
target = 'Outcome'
ratio = 0.8

diabetes_data = h2oai.create_dataset_sync(dataPath)

# Split the data
diabetes_split_data = h2oai.make_dataset_split(
    dataset_key = diabetes_data.key
    , output_name1 = basename + "_train"
    , output_name2 = basename + "_test"
    , target = target
    , fold_col = ""
    , time_col = ""
    , ratio = ratio
    , seed = 1234
)

train_key = h2oai.get_dataset_split_job(diabetes_split_data).entity[0]
test_key  = h2oai.get_dataset_split_job(diabetes_split_data).entity[1]
dropped = []

# Diabetes Default
knobs = [8, 2, 8]
diabetes1 = h2oai.start_experiment_sync(
      experiment_name = "Diabetes"
    , dataset_key = train_key
    , testset_key = test_key
    , target_col = target
    , is_classification = True
    , accuracy = knobs[0]
    , time = knobs[1]
    , interpretability = knobs[2]
    , enable_gpus = True
    , cols_to_drop = dropped
)

# Diabetes GLM
diabetes2 = h2oai.start_experiment_sync(
      experiment_name = "Diabetes GLM"
    , dataset_key = train_key
    , testset_key = test_key
    , target_col = target
    , is_classification = True
    , accuracy = knobs[0]
    , time = knobs[1]
    , interpretability = knobs[2]
    , enable_gpus = True
    , cols_to_drop = dropped
    , config_overrides = "included_models = ['GLM']"
)
