import requests

'''
Test Script 

'''

# Sample data
sample_data = {
        'adm_type':'shift_from',
        'shift_from':'er',
        'ssc':'no',
        'yr_nae':1006,
        'm_no':46,
        'sex':'f',
        'disease':'mi',
        'status':'discharge',
        'consultant':'tariq_nawaz',
        'doa':'1-Sep-25'
    }

customer = {
    'age': 30,
    'job': 'admin_',
    'marital': 'single',
    'education': 'university_degree',
    'default': 'no',
    'housing': 'no',
    'loan': 'yes',
    'contact': 'cellular',
    'month': 'oct',
    'day_of_week': 'tue',
    'campaign': 1,
    'pdays': 0,
    'previous': 0,
    'poutcome': 'success',
    'emp_var_rate': 1.4,
    'cons_price_idx': 93.444,
    'cons_conf_idx': -36.1,
    'euribor3m': 4.966,
    'nr_employed': 5228.1
}

url = 'http://0.0.0.0:9696/predict'

#result = requests.post(url, json=sample_data).json()

result = requests.post(url, json=sample_data).json()

print(result)



