import json

def readCFG(file="config.json"):
    with open(file, "r") as cfg:
        return json.load(cfg)

