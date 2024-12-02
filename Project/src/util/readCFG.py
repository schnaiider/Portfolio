import json

def readCFG(file=r"C:\\Users\\xuzik\\Desktop\\Anac ETL\\Anac-ETL\\config\\config.json"):
    with open(file, "r") as cfg:
        return json.load(cfg)

