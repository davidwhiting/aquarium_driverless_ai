dataPath = '/data/Training/Glass.csv'
basename = 'Glass'
target = 'Type'
ratio = 0.8

glass_data = h2oai.create_dataset_sync(dataPath)

# Split the data
glass_split_data = h2oai.make_dataset_split(
    dataset_key = glass_data.key
    , output_name1 = basename + "_train"
    , output_name2 = basename + "_test"
    , target = target
    , fold_col = ""
    , time_col = ""
    , ratio = ratio
    , seed = 1234
)

train_key = h2oai.get_dataset_split_job(glass_split_data).entity[0]
test_key  = h2oai.get_dataset_split_job(glass_split_data).entity[1]

# Glass Experiment #1
knobs = [7, 5, 8]
glass1 = h2oai.start_experiment_sync(
      experiment_name = "Glass Big"
    , dataset_key = train_key
    , testset_key = test_key
    , target_col = "Type"
    , is_classification = True
    , accuracy = knobs[0]
    , time = knobs[1]
    , interpretability = knobs[2]
    , enable_gpus = True
    , cols_to_drop = ["SuperType"]
)

# Glass Experiment #2
knobs = [7, 2, 8]
glass2 = h2oai.start_experiment_sync(
      experiment_name = "Glass Quick"
    , dataset_key = train_key
    , testset_key = test_key
    , target_col = "Type"
    , is_classification = True
    , accuracy = knobs[0]
    , time = knobs[1]
    , interpretability = knobs[2]
    , enable_gpus = True
    , cols_to_drop = ["SuperType"]
)

# Glass Experiment #3
knobs = [7, 5, 8]
glass3 = h2oai.start_experiment_sync(
      experiment_name = "Glass3 Big"
    , dataset_key = train_key
    , testset_key = test_key
    , target_col = "SuperType"
    , is_classification = True
    , accuracy = knobs[0]
    , time = knobs[1]
    , interpretability = knobs[2]
    , enable_gpus = True
    , cols_to_drop = ["Type"]
)

# Glass Experiment #3
knobs = [7, 2, 8]
glass4 = h2oai.start_experiment_sync(
      experiment_name = "Glass3 Quick"
    , dataset_key = train_key
    , testset_key = test_key
    , target_col = "SuperType"
    , is_classification = True
    , accuracy = knobs[0]
    , time = knobs[1]
    , interpretability = knobs[2]
    , enable_gpus = True
    , cols_to_drop = ["Type"]
)

