import json

def readCFG(file="/workspaces/portfolio/Anac-ETL/Project/config/config.json"):
    with open(file, "r") as cfg:
        return json.load(cfg)

