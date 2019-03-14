"""
是个重复造的轮子，没错了
功能十分简单 懒得写文档

非异步版本
"""
import requests,base64,asyncio,aiohttp,requests_oauthlib

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
    def fetchTimeline(self,
        scrname=None,userid=None,
        count=1,returnRaw=False,*args,**kwargs):
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
    async def AFetchTimeline(self):
        pass