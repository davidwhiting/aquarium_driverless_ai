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

### Amaxon Reviews

dataPath = '/data/Training/AmazonFineFoodReviews.csv'
basename = 'Reviews'
target = 'PositiveReview'
ratio = 0.8

reviews_data = h2oai.create_dataset_sync(dataPath)

# Split the data
reviews_split_data = h2oai.make_dataset_split(
    dataset_key = reviews_data.key
    , output_name1 = basename + "_train"
    , output_name2 = basename + "_test"
    , target = target
    , fold_col = ""
    , time_col = ""
    , ratio = ratio
    , seed = 1234
)

train_key = h2oai.get_dataset_split_job(reviews_split_data).entity[0]
test_key  = h2oai.get_dataset_split_job(reviews_split_data).entity[1]

# Reviews Default

dropped = ['UserID', 'ProductId', 'Id', 'Summary', 'Score', 'HelpfulnessDenominator', 'HelpfulnessNumerator', 'ProfileName', 'Time']
knobs = [8, 2, 7]
reviews1 = h2oai.start_experiment_sync(
      experiment_name = "Reviews NLP Big"
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

reviews1a = h2oai.start_experiment_sync(
      experiment_name = "Reviews NLP Big TF"
    , dataset_key = train_key
    , testset_key = test_key
    , target_col = target
    , is_classification = True
    , accuracy = knobs[0]
    , time = knobs[1]
    , interpretability = knobs[2]
    , enable_gpus = True
    , cols_to_drop = dropped
    , config_overrides = """
        recipe = 'TextCNNTransformer'
        recipe = 'TextBiGRUTransformer'
    """
)

knobs = [6, 2, 7]
reviews2 = h2oai.start_experiment_sync(
      experiment_name = "Reviews NLP"
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

dropped = ['UserID', 'ProductId', 'Id', 'Score', 'HelpfulnessDenominator', 'HelpfulnessNumerator', 'ProfileName', 'Time']
reviews3 = h2oai.start_experiment_sync(
      experiment_name = "Reviews NLP+"
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

dropped = ['Score', 'ProfileName', 'Time']
reviews4 = h2oai.start_experiment_sync(
      experiment_name = "Reviews NLP++"
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

dropped = ['Summary', 'Score', 'Description', 'ProfileName', 'Time']
reviews5 = h2oai.start_experiment_sync(
      experiment_name = "Reviews -NLP"
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
