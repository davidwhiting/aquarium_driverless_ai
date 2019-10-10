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


### Titanic Models
dataPath = '/data/Training/Titanic.csv'
basename = 'Titanic'
target = 'survived'
ratio = 0.8

titanic_data = h2oai.create_dataset_sync(dataPath)

# Split the data
titanic_split_data = h2oai.make_dataset_split(
    dataset_key = titanic_data.key
    , output_name1 = basename + "_train"
    , output_name2 = basename + "_test"
    , target = target
    , fold_col = ""
    , time_col = ""
    , ratio = ratio
    , seed = 1234
)

train_key = h2oai.get_dataset_split_job(titanic_split_data).entity[0]
test_key  = h2oai.get_dataset_split_job(titanic_split_data).entity[1]

knobs = [8, 2, 8]

# Titanic Default

dropped = ['no.title', 'cabin', 'embarked', 'boat', 'body', 'home.dest']
titanic1 = h2oai.start_experiment_sync(
      experiment_name = "Titanic"
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

# Titanic No Name
dropped = ['name', 'no.title', 'cabin', 'embarked', 'boat', 'body', 'home.dest']
titanic2 = h2oai.start_experiment_sync(
      experiment_name = "Titanic no Name"
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

# Titanic Leak
dropped = ['no.title']
titanic3 = h2oai.start_experiment_sync(
      experiment_name = "Titanic Leak"
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
