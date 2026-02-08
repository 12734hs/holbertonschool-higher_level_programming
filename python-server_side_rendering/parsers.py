import csv, json

def parse_csv(file):
    result = []
    with open(file, 'r') as fl:
        lol = csv.DictReader(fl)
        for row in lol:
            result.append(row)
    return result


def parse_json(file):
    with open(file, 'r') as fl:
        dct = json.load(fl)
    return dct