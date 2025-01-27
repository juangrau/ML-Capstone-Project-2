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

url = 'http://0.0.0.0:9696/predict'

#result = requests.post(url, json=sample_data).json()

result = requests.post(url, json=sample_data).json()

print(result)



