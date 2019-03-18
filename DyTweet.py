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
TGBot = aiogram.Bot(token="")
TwApp = CamTweet.CamTweet()

async def poll(pollList:list):

    while(true):
        asyncio.wait()
async def _poll(search:str,):
    
    if True:
        await TGBot.send_message()

async def reg():

    pass

loop = asyncio.get_event_loop()

#让异步脚本跑起来
loop.create_task([poll(),reg()])
print("OnRunning...")

#防止死掉
loop.run_forever()