from Modules import CamTweet,CamTG
import json,logging

def readJSON(path='config.json'):
    with open(path,'rb') as f:
        return json.load(f)
    return None

def dumpJSON(cfg,path='config.json'):
    with open(path,'wb') as f:
        f.truncate()
        return json.dump(cfg,f)
    return None

config = readJSON()
