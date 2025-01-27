'''
This script builds and train the model using as the input the original dataset
'''


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
import pickle



df = pd.read_csv('./data/cw_22_23_24.csv')

del df['D.O.D']
del df['mrn']
del df['pt_name']

# lets normalize the columns names
df.columns = df.columns.str.lower().str.replace(' ','_').str.replace('.', '')

categorical_features = list(df.dtypes[df.dtypes == 'object'].index)

for c in categorical_features:
    df[c] = df[c].str.lower().str.replace(' ','_')


numerical_features = list(df.dtypes[df.dtypes != 'object'].index)
numerical_features.remove('los')

df['doa'] = pd.to_datetime(df['doa'], format='mixed')
df['doa_month'] = df['doa'].dt.month
df['doa_day_of_month'] = df['doa'].dt.day
df['doa_day_of_week'] = df['doa'].dt.day_of_week
df['doa_isweekend'] = df['doa'].dt.day_of_week>5
df['doa_quarter'] = df['doa'].dt.quarter
del df['doa']

categorical_features.remove('doa')

df['disease'].fillna('missing', inplace=True)


# Define the preprocessing steps
numerical_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_features),
        ('cat', categorical_transformer, categorical_features)
    ])


df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
df_full_train = df_full_train.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_full_train = df_full_train.los.values
y_test = df_test.los.values

y_full_train_log = np.log1p(y_full_train)
y_test_log = np.log1p(y_test)

del df_test['los']
del df_full_train['los']


# from the first train, we got that the best alpha value was 10.0
best_alpha = 10.0

# Create a pipeline that includes the preprocessor and the ridge regression model, intead of LinearRegression
ridge_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                                  ('regressor', Ridge(alpha=best_alpha))])

ridge_pipeline.fit(df_full_train, y_full_train_log)
y_pred = ridge_pipeline.predict(df_test)

mse = mean_squared_error(y_test_log, y_pred)

print(f'Model Trained: Mean Squared Error: {mse}')


# Save the best model to a file
# Save the best model to a file
filename = 'ridge_regression_model_v1.pkl'
with open(filename, 'wb') as file:
    pickle.dump(ridge_pipeline, file)

