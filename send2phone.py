#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests
import json
import os
import codecs
import io

class send2phone:
    def __init__(self, *args, **kwargs):
        self.barklink = kwargs["barkurl" ] if ("barkurl" in kwargs) else ""            
        self.skey = kwargs["skey" ] if ("skey" in kwargs) else ""  
        if ("wxpusher_token" in kwargs) and ("wxpusher_uid"):         
            self.wxpusher_token = kwargs["wxpusher_token"]
            self.wxpusher_uid = kwargs["wxpusher_uid"]
        else:
            self.wxpusher_token = ""
            self.wxpusher_uid = ""

            
    def send2bark(self, title, content):
        if (self.barklink):
            try:
                if (self.barklink[-1:] == u"/"):
                    self.barklink = self.barklink[0: len(self.barklink)-1]
                msg = u"{0}/推送标题/{1}/'{2}'".format(self.barklink, title, content)
                res = requests.get(msg,verify=False)
            except Exception as e:
                print('Reason:', e)
        return
        
    def send2s(self, title, content):
        if (self.skey != ""):
            try:
                self.skey = self.skey.replace(".send", "")
                link = u"https://sc.ftqq.com/{0}.send".format(self.skey)
                d = {'text': title, 'desp': content}
                res = requests.post(link, data=d , verify=False)
            except Exception as e:
                print('Reason:', e)
        return    
    
    def send2wxpusher(self, content):
        if (self.wxpusher_token != "") and (self.wxpusher_uid != ""):
            try:
                self.wxpusher = self.skey.replace(".send", "")
                link = "http://wxpusher.zjiecode.com/api/send/message"
                d = {
                        "appToken":self.wxpusher_token,
                        "content":content,
                        "contentType":3,
                        "uids":[
                            self.wxpusher_uid
                        ]
                    }
                res = requests.post(link, json=d , verify=False)
            except Exception as e:
                print('Reason:', e)
        return    
    
if __name__ == "__main__":
    pushno.send2wxpusher("签到任务 {0} 失败 任务已禁用".format('test') )
    pushno.send2bark("签到任务 {0} 失败".format('test'), "任务已禁用")
    pushno.send2s("签到任务 {0} 失败".format('test'), "任务已禁用")
