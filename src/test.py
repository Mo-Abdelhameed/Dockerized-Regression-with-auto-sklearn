from autogluon.core import TabularDataset

from config import paths
from Regressor import Regressor, predict_with_model
from schema.data_schema import load_json_data_schema
from utils import read_csv_in_directory, read_json_as_dict

x_train = read_csv_in_directory(paths.TRAIN_DIR)
x_test = read_csv_in_directory(paths.TEST_DIR)
x_train = TabularDataset(x_train)
schema = load_json_data_schema(paths.INPUT_SCHEMA_DIR)

r = Regressor(x_train, schema)
r.train()
r.save(paths.PREDICTOR_DIR_PATH,)
predictions_df = predict_with_model(r, x_test)

print(predictions_df)
