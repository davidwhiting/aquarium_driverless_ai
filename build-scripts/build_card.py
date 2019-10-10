dataPath = '/data/Training/CreditCard.csv'
basename = 'Card'
target = 'Default'
ratio = 0.8
dropped = []

card_data = h2oai.create_dataset_sync(dataPath)

# Split the data
card_split_data = h2oai.make_dataset_split(
    dataset_key = card_data.key
    , output_name1 = basename + "_train"
    , output_name2 = basename + "_test"
    , target = target
    , fold_col = ""
    , time_col = ""
    , ratio = ratio
    , seed = 1234
)

train_key = h2oai.get_dataset_split_job(card_split_data).entity[0]
test_key  = h2oai.get_dataset_split_job(card_split_data).entity[1]

# Card Default
knobs = [6, 4, 6]
card_default = h2oai.start_experiment_sync(
      experiment_name = "Card Default"
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

# Card Monotonic
knobs = [6, 4, 7]
card_monotonic = h2oai.start_experiment_sync(
      experiment_name = "Card Monotonic"
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

# Card Big
knobs = [8, 6, 7]
card_big = h2oai.start_experiment_sync(
      experiment_name = "Card Big"
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

# Card GLM
knobs = [6, 4, 7]
card_glm = h2oai.start_experiment_sync(
      experiment_name = "Card GLM"
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

# Card Compliant
knobs = [6, 4, 7]
card_compliant = h2oai.start_experiment_sync(
      experiment_name = "Card Compliant"
    , dataset_key = train_key
    , testset_key = test_key
    , target_col = target
    , is_classification = True
    , accuracy = knobs[0]
    , time = knobs[1]
    , interpretability = knobs[2]
    , enable_gpus = True
    , cols_to_drop = dropped
    , config_overrides = "recipe = 'compliant'"
)

