# import autosklearn.pipeline.components.regression
# regressors = autosklearn.pipeline.components.regression._regressors.keys()
# print(list(regressors))


import autosklearn.pipeline.components.feature_preprocessing
preprocessors = list(autosklearn.pipeline.components.feature_preprocessing._preprocessors.keys())
print(list(preprocessors))
