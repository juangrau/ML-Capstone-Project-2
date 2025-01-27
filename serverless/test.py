import requests

url = 'http://0.0.0.0:8080/2015-03-31/functions/function/invocations'

#data = {'url': 'http://bit.ly/mlbookcamp-pants'}

data = {
        'data': {
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
    }

result = requests.post(url, json=data).json()
print(result)