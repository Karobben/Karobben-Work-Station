#!/usr/bin/env python3
import itchat, random, time
import urllib.request
import urllib.parse
import json

'''
This script is for embeding an auto-responding bot in Wechat based on Qingyunke Api.
'''
class airoot(object):
    def __init__(self):
        self.url = r'http://api.qingyunke.com/api.php?%s'
        self.data = {
            'key':'free',
            'appid':0,
            'msg':''
        }
    def getword(self, word=''):
        self.data['msg'] = word
        if self.data['msg'] == '':
            self.data['msg'] = '你不说话, 我来撩你吧'
        self.params = urllib.parse.urlencode(self.data)
        self.url = self.url % self.params
        self.page = urllib.request.urlopen(self.url).read()
        self.res = json.loads(self.page)
        self.res['content'] = self.res['content'].replace('{br}',' ')
        return self.res
        #This function is original from:https://blog.csdn.net/qq_29129381/article/details/82865617

# A dictionary for personalize some information
Switch_dic = {  "女菲菲":"男",
                "我是女的啦":"我是男的啦",
                "反正不是男的":"你说呢？",
                "菲菲":"凯哥",
                "我是聪明与智慧并存的美女":"我是聪明与智慧并存的美少男",
                "菲菲老婆":"凯哥老公",
                '讨厌，不要随便问女生年龄知道不':'比你大一点点的',
                '女生的年龄是不能随便说的，知道不':"怎么，你还会算命？？",
                '网友':'亲爱哒～',
                '提示：按分类看笑话请发送“笑话分类”':'ಥ‿ಥ'
}

def Switch(Sentence,Switch_dic):
    for i in list(Switch_dic.keys()):
        if i in Sentence:
            Sentence = Sentence.replace(i,Switch_dic[i])
    return Sentence

# User ID, for avoiding Doble postpone time
My_ID = "@5ac17e248d8a6cd444b32b6ffee139386a599c28a60280d970e8222cf440e81e"
# Varying the responding time basd on the length of massages
def Lag_time(User,S1,S2,Time_request):
    if User != My_ID:
        Time_Reading = 0
        for i in range(len(S1)):
            Time_Reading += random.choice(range(1,2))*0.1
        Time_Pondering = random.choice(range(0,10))*0.1
        Time_Typing    = 0
        for i in range(len(S2)):
            Time_Typing += random.choice(range(0,5))*0.1
        Time_lag = Time_Reading + Time_Pondering + Time_Typing
        if Time_request > Time_lag:
            print(Time_request,Time_lag)
        else:
            print(Time_Reading,Time_Pondering,Time_Typing)
            time.sleep(Time_lag-Time_request)

#auto-response
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    Time_A = time.time()
    B = Switch(airoot().getword(msg['Text'])['content'],Switch_dic)
    if B == "女的":
        B == "纯爷们！！"
    Time_request = time.time() - Time_A
    Lag_time(msg['FromUserName'],msg['Text'],B,Time_request)
    print(msg)
    return B

#login
itchat.auto_login(enableCmdQR=2,hotReload=True)

#keeping running
itchat.run()
