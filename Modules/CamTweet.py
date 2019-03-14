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
        ret = requests.post(api+'oauth2/token',
            auth = (user,pswd),data = {'grant_type':'client_credentials'})
        ret.raise_for_status()
        return ret.json()['access_token']

class CamTweetBase(object):
    def __init__(self,auth=None,user=None,cred=None,*args,**kwargs):
        self.auth=auth
        if auth==None:
            self.auth=CamTweetUtil.getOauth(user,cred)
class CamTweet(CamTweetBase):
    def __init__(self,user,cred,*args,**kwargs):
        super().__init__(user=user,cred=cred)

    

