import json

import pandas as pd
from datetime import datetime
from datetime import date

def backtracking(filename='data/result.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        
        startx = datetime.timestamp(datetime.strptime(file_data['properties']['start_time'], '%Y-%m-%dT%H:%M:%S'))
            
        endx = datetime.timestamp(datetime.strptime(file_data['properties']['end_time'], '%Y-%m-%dT%H:%M:%S'))
           
        bbb = backtrackingcompare(startx,endx)
#        print(bbb)
    return bbb
        
        
        
        
        #for features in file_data['features']:
            #startx = datetime.timestamp(datetime.strptime(features['properties']['start_time'], '%Y-%m-%dT%H:%M:%S'))
            
            #endx = datetime.timestamp(datetime.strptime(features['properties']['end_time'], '%Y-%m-%dT%H:%M:%S'))
           
            #backtrackingcompare(startx,endx)
        
    
                
    
        
        
        
        
def backtrackingcompare(x,y,filename='data/output.json'):
    headx = 100000
    heady = 100000
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        for features in file_data['gps']:
            
            
            if features['timestamp']//1000 == x:
                
                headx = features['coords']['heading']
            if features['timestamp']//1000 == y:
                
                heady = features['coords']['heading']
            
            
    
            
            
    diff = headx - heady
    
    bool = 170 < abs(diff) <190
    
    
    return bool

backtracking()


