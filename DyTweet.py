# <TODO>改写为异步操作
# 先写同步的

from Modules import CamTweet,CamTG
import json,logging,requests,time,asyncio
import aiogram

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
TGBot = pass
TwApp = CamTweet.CamTweet()

async def poll(pollList:list,
    twapp:CamTweet.CamTweet,
    tgbot):
    pass

async def main():
    

loop = asyncio.get_event_loop()
loop.run_forever()