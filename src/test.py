# import autosklearn.pipeline.components.regression
# regressors = autosklearn.pipeline.components.regression._regressors.keys()
# print(list(regressors))


import autosklearn.pipeline.components.feature_preprocessing
preprocessors = list(autosklearn.pipeline.components.feature_preprocessing._preprocessors.keys())
print(list(preprocessors))


{
  "seed_value": 123,
  "task_time": 300,
  "model_time": 30,
  "include": {
    "regressor": [
      "random_forest",
      "extra_trees",
      "gradient_boosting",
      "k_nearest_neighbors",
      "sgd"
    ]
  }
}