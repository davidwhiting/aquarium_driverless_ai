## Glass Experiments
glass <- dai.create_dataset('/data/Training/Glass.csv')

glass_split <- 
  dai.split_dataset(glass,
                    output_name1 = 'Glass_train',
                    output_name2 = 'Glass_test',
                    target = 'Type',
                    ratio = .8,
                    seed = 1234)
### Glass Models

glass_big <- 
  dai.train(experiment_name = "Glass Big",
            training_frame = glass_split$Glass_train,
            testing_frame  = glass_split$Glass_test,
            target_col = 'Type',
            is_classification = TRUE,
            is_timeseries = FALSE,
            accuracy = 7, time = 5, interpretability = 8
  )

glass_quick <- 
  dai.train(experiment_name = "Glass Quick",
            training_frame = glass_split$Glass_train,
            testing_frame  = glass_split$Glass_test,
            target_col = 'Type',
            is_classification = TRUE,
            is_timeseries = FALSE,
            accuracy = 7, time = 2, interpretability = 8
  )

glass3_big <- 
  dai.train(experiment_name = "Glass 3 Big",
            training_frame = glass_split$Glass_train,
            testing_frame  = glass_split$Glass_test,
            target_col = 'SuperType',
            is_classification = TRUE,
            is_timeseries = FALSE,
            accuracy = 7, time = 5, interpretability = 8
  )

glass3_quick <- 
  dai.train(experiment_name = "Glass 3 Quick",
            training_frame = glass_split$Glass_train,
            testing_frame  = glass_split$Glass_test,
            target_col = 'SuperType',
            is_classification = TRUE,
            is_timeseries = FALSE,
            accuracy = 7, time = 2, interpretability = 8
  )

## Boston Housing Experiments

housing <- dai.create_dataset('/data/Training/BostonHousing.csv')

housing_split <- 
  dai.split_dataset(housing,
                    output_name1 = 'Housing_train',
                    output_name2 = 'Housing_test',
                    ratio = .8,
                    seed = 1234)

### Housing Models

housing_default <- 
  dai.train(experiment_name = "Housing",
            training_frame = housing_split$Housing_train,
            testing_frame  = housing_split$Housing_test,
            target_col = 'VALUE',
            is_classification = FALSE,
            is_timeseries = FALSE,
            accuracy = 7, time = 2, interpretability = 8
  )

housing_quick <- 
  dai.train(experiment_name = "Housing Quick",
            training_frame = housing_split$Housing_train,
            testing_frame  = housing_split$Housing_test,
            target_col = 'VALUE',
            is_classification = FALSE,
            is_timeseries = FALSE,
            accuracy = 4, time = 2, interpretability = 8
  )

housing_glm <- 
  dai.train(experiment_name = "Housing GLM",
            training_frame = housing_split$Housing_train,
            testing_frame  = housing_split$Housing_test,
            target_col = 'VALUE',
            is_classification = FALSE,
            is_timeseries = FALSE,
            accuracy = 7, time = 2, interpretability = 8
            config_overrides = "included_models = ['GLM']"
  )

## Diabetes Experiments

diabetes <- dai.create_dataset('/data/Training/PimaDiabetes.csv')

diabetes_split <- 
  dai.split_dataset(diabetes,
                    output_name1 = 'Diabetes_train',
                    output_name2 = 'Diabetes_test',
                    target = 'Diabetes',
                    ratio = .8,
                    seed = 1234)

### Diabetes Models

diabetes_default <- 
  dai.train(experiment_name = "Diabetes",
            training_frame = diabetes_split$Diabetes_train,
            testing_frame  = diabetes_split$Diabetes_test,
            target_col = 'Diabetes',
            is_classification = TRUE,
            is_timeseries = FALSE,
            accuracy = 7, time = 2, interpretability = 8
  )

## Credit Card Default Experiments


creditcard <- dai.create_dataset('/data/Training/CreditCard.csv')

cardsplit <- 
  dai.split_dataset(creditcard,
                    output_name1 = 'CreditCard_train',
                    output_name2 = 'CreditCard_test',
                    target = 'Default',
                    ratio = .8,
                    seed = 1234)

### Card Models

cardmodel_default <- 
  dai.train(experiment_name = "Card Default",
            training_frame = cardsplit$CreditCard_train,
            testing_frame  = cardsplit$CreditCard_test,
            target_col = 'Default',
            is_classification = TRUE,
            is_timeseries = FALSE,
            accuracy = 6, time = 4, interpretability = 6
  )

cardmodel_monotonic <- 
  dai.train(experiment_name = "Card Monotonic",
            training_frame = cardsplit$CreditCard_train,
            testing_frame  = cardsplit$CreditCard_test,
            target_col = 'Default',
            is_classification = TRUE,
            is_timeseries = FALSE,
            accuracy = 6, time = 4, interpretability = 7
  )

cardmodel_big <- 
  dai.train(experiment_name = "Card Big",
            training_frame = cardsplit$CreditCard_train,
            testing_frame  = cardsplit$CreditCard_test,
            target_col = 'Default',
            is_classification = TRUE,
            is_timeseries = FALSE,
            accuracy = 8, time = 6, interpretability = 7
  )

cardmodel_compliant <- 
  dai.train(experiment_name = "Card Compliant",
            training_frame = cardsplit$CreditCard_train,
            testing_frame  = cardsplit$CreditCard_test,
            target_col = 'Default',
            is_classification = TRUE,
            is_timeseries = FALSE,
            accuracy = 6, time = 4, interpretability = 7,
            config_overrides = "recipe = 'compliant'"
  )

cardmodel_glm <- 
  dai.train(experiment_name = "Card GLM",
            training_frame = cardsplit$CreditCard_train,
            testing_frame  = cardsplit$CreditCard_test,
            target_col = 'Default',
            is_classification = TRUE,
            is_timeseries = FALSE,
            accuracy = 6, time = 4, interpretability = 7,
            config_overrides = "included_models = ['GLM']"
  )

#cardmodel_retrain <- 
#  dai.train(experiment_name = "Card GLM",
#            training_frame = cardsplit$CreditCard_train,
#            testing_frame  = cardsplit$CreditCard_test,
#            target_col = 'Default',
#            is_classification = TRUE,
#            is_timeseries = FALSE,
#            accuracy = 6, time = 4, interpretability = 7,
#            config_overrides = "included_models = ['GLM']"
#            )

