#!/usr/bin/python3
import json
import csv


def convert_csv_to_json(filename):
    try:
        with open(filename, mode='r') as csvfile:
            data = list(csv.DictReader(csvfile))
    
        with open('data.json', 'w') as jsn:
            json.dump(data, jsn)
        
        return True    
    except:
        return False
