"""
是个重复造的轮子，没错了  
功能十分简单  
"""
import requests,base64,asyncio,aiohttp,requests_oauthlib
import os,sys

api = 'https://api.twitter.com/'

class CamTweetUtil(object):
    @classmethod
    def getOauth(cls,user,pswd):
        assert type(user)==str and type(pswd)==str
        ret = requests.post(api+'oauth2/token',
            auth = (user,pswd),data = {'grant_type':'client_credentials'})
        ret.raise_for_status()
        return ret.json()['access_token']

class CamTweetBase(object):
    def __init__(self,auth,*args,**kwargs):
        self.auth=auth

class CamTweet(CamTweetBase):
    def __init__(self,*args,**kwargs):
        try:
            if len(args)==2: auth=CamTweetUtil.getOauth(args[0],args[1])
            else: auth = args[0]
        except:
            auth = kwargs.get('auth',d=-1)
            if auth==-1:
                auth = CamTweetUtil.getOauth(
                    kwargs.get('user'),kwargs.get('pswd')
                )
        super().__init__(auth)

    def fetchTimeline(self,scrname=None,userid=None,
        count=1,returnRaw=False,*args,**kwargs):
        """拉取时间线的同步实现"""
        assert scrname!=None or userid!=None
        url= api+"1.1/statuses/user_timeline.json"
        headers={
            "Authorization":"Bearer "+self.auth
        }
        params={}
        if userid!=None:params["userid"]=userid
        else:params["screen_name"]=scrname
        params['count']=count
        ret = requests.get(url,headers=headers,params=params)
        if returnRaw: return ret
        ret.raise_for_status()
        return ret.json()

    async def AfetchTimeline(self,scrname=None,userid=None,
        count=1,returnRaw=False,*args,**kwargs):
        """拉取时间线的异步实现"""
        assert scrname!=None or userid!=None
        url= api+"1.1/statuses/user_timeline.json"
        headers={
            "Authorization":"Bearer "+self.auth
        }
        params={}
        if userid!=None:params["userid"]=userid
        else:params["screen_name"]=scrname
        params['count']=count
        async with aiohttp.ClientSession() as sess:
            async with sess.get(url,headers=headers,params=params) as ret:
                ret.raise_for_status()
                return await ret.json()
        pass
    