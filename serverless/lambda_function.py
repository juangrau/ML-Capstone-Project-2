import pickle
import pandas as pd
import pickle
import numpy as np

model_file = 'ridge_regression_model_v1.pkl'
with open(model_file, 'rb') as file:
    loaded_model = pickle.load(file)

def prepare_data(data):
    # Create a Pandas DataFrame from the dictionary
    input_df = pd.DataFrame([data])
    input_df['doa'] = pd.to_datetime(input_df['doa'], format='mixed')
    input_df['doa_month'] = input_df['doa'].dt.month
    input_df['doa_day_of_month'] = input_df['doa'].dt.day
    input_df['doa_day_of_week'] = input_df['doa'].dt.day_of_week
    input_df['doa_isweekend'] = input_df['doa'].dt.day_of_week>5
    input_df['doa_quarter'] = input_df['doa'].dt.quarter
    del input_df['doa']
    return input_df

def predict(data):
    # using the same test_df we used before
    y_pred_log = loaded_model.predict(prepare_data(data))

    # Convert the predictions back to the original scale
    y_pred_original = np.expm1(y_pred_log)

    result = {
        'days': float(y_pred_original[0])
    }

    return result

def lambda_handler(event, context):
    data = event['data']
    result = predict(data)
    return result