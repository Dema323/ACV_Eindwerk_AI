import json
import pandas as pd
from datetime import datetime
from datetime import date

def calculate_paid_time(filename='data/result.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        for features in file_data['features']:
            if features['type'] == 1:
                # end_time = features['properties']['end_time']
                end_time = pd.to_datetime(features['properties']['end_time'], format='%Y-%m-%d')
                print(end_time)

            if features['type'] == 2:
                start_time = pd.to_datetime(features['properties']['start_time'], format='%Y-%m-%d')
                print(start_time)
    diff = start_time - end_time

    print(diff.total_seconds())
    data = {}
    data['total'] = []
    data['total'].append({
        'seconds' : diff.total_seconds() ,
    })

    with open('data/paid_time.json', 'w') as outfile:
        json.dump(data, outfile)

calculate_paid_time()
