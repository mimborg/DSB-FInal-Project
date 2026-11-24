import requests
import json


def bls_api(payload):
    '''
    This function is for making the API call to public BLS data
    
    series_ids: list of series id's being called from BLS website (ex. ['CUUR0000SA0','SUUR0000SA0'])
    start_year: starting year for desired data
    end_year: ending year for desired data
    '''

    headers = {'Content-type': 'application/json'}
    data = json.dumps(payload)
    p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
    json_data = p.json()

    return json_data



