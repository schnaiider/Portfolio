import json

def readCFG(file="/workspaces/portfolio/config/config.json"):
    with open(file, "r") as cfg:
        return json.load(cfg)

