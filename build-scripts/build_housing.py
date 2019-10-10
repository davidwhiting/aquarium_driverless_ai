dataPath = '/data/Training/BostonHousing.csv'
basename = 'Housing'
target = 'VALUE'
ratio = 0.8

boston_data = h2oai.create_dataset_sync(dataPath)

# Split the data
boston_split_data = h2oai.make_dataset_split(
    dataset_key = boston_data.key
    , output_name1 = basename + "_train"
    , output_name2 = basename + "_test"
    , target = target
    , fold_col = ""
    , time_col = ""
    , ratio = ratio
    , seed = 1234
)

train_key = h2oai.get_dataset_split_job(boston_split_data).entity[0]
test_key  = h2oai.get_dataset_split_job(boston_split_data).entity[1]
dropped = []

# Housing Experiment #1
knobs = [7, 2, 8]
housing1 = h2oai.start_experiment_sync(
      experiment_name = "Housing"
    , dataset_key = train_key
    , testset_key = test_key
    , target_col = target
    , is_classification = False
    , accuracy = knobs[0]
    , time = knobs[1]
    , interpretability = knobs[2]
    , scorer = 'RMSE'
    , enable_gpus = True
    , cols_to_drop = dropped
)

# Housing Experiment #2
knobs = [4, 2, 8]
housing2 = h2oai.start_experiment_sync(
      experiment_name = "Housing Quick"
    , dataset_key = train_key
    , testset_key = test_key
    , target_col = target
    , is_classification = False
    , accuracy = knobs[0]
    , time = knobs[1]
    , interpretability = knobs[2]
    , scorer = 'RMSE'
    , enable_gpus = True
    , cols_to_drop = dropped
)

