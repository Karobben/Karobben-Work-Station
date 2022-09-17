#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i','-I','--input',nargs='+')    #输入文件
parser.add_argument('-t','-T','--token')    #输入文件
parser.add_argument('-c','-C','--category', default= "summary.md")    #输入文件

args = parser.parse_args()

INPUT = args.input
Token = args.token
Category = args.category

import threading
import concurrent.futures
import yaml
import requests
import os, re

def Yml_json(yml):
  f = open(yml, 'r')
  ystr = f.read()
  aa = yaml.load(ystr, Loader=yaml.FullLoader)
  return aa

def ReporsID_get(Identity):
  url = 'https://www.yuque.com/api/v2/users/' + Identity['repo'].split('/')[0]+"/repos"
  header = {"X-Auth-Token": Identity['Token']}
  List =   requests.get(url, headers = header).json()['data']
  for i in List:
    if Identity['repo'].split('/')[1] == i['slug']:
      Repos_ID = i['id']
  return Repos_ID

def DocList_get(Repos_ID):
  header = {"X-Auth-Token": Identity['Token']}
  url = 'https://www.yuque.com/api/v2/repos/'+str(Repos_ID)+'/docs'
  Doc_Result = requests.get(url, headers = header).json()['data']
  return Doc_Result

def MDbody_clean(MD_body):
  MD_body = MD_body[MD_body.find('---',1)+3:]
  # 語雀不支持<pre>標籤
  try:
      AA = re.findall("<pre[^>]+>", MD_body)
      for PRE in AA:
          MD_body = MD_body.replace(PRE, '```text')
  except:
      PRE = "<pre>"
      print(PRE, "IAMHERE")
  print(MD_body)
  MD_body = MD_body.replace("<pre>", '```text')
  MD_body = MD_body.replace("</pre>", '```')
  # 添加封面圖片
  F  = open(MD,'r').read()
  Data_header = yaml.load(F.split('---')[1], Loader=yaml.FullLoader)
  try:
    CP = Data_header['covercopy']
    CP = "|![](" + Data_header['cover']+")|\n"  + "|:--:|\n" + "|"+CP+"|\n"
  except:
    CP = ""
  # 添加本文github鏈接
  try:
      git_url = "".join([  "\n<span style='color:salmon'>由於語法渲染問題而影響閱讀體驗， 請移步博客閱讀～</span>",
                    "\n[本文GitPage地址]",
                    "(https://karobben.github.io/",
                    str(Data_header['date']).split(' ')[0].replace("-","/"), "/",
                    os.getcwd().split("/")[-1],"/",
                    MD[:-3],
                    ")\n"])
  except:
      git_url = ""
  # 合併前面的所有
  MD_body =  CP+ git_url + MD_body
  # 加個尾巴
  MD_body += '''
  ---

  **Enjoy~**

  本文由<span style='color:salmon'>Python腳本</span>[GitHub](https://karobben.github.io/2021/03/02/Python/yuqueAPI)/[語雀](https://www.yuque.com/liuwenkan/python/yuque_api)自動更新
  %%%
  GitHub: [Karobben](https://github.com/Karobben)
  Blog:[Karobben](https://karobben.github.io/)
  BiliBili:[史上最不正經的生物狗](https://space.bilibili.com/393056819)
  '''.replace("%%%",git_url)
  return MD_body

def MDupDate(MD, Repos_ID, Doc_list):
  # read MD file
  F  = open(MD,'r').read()
  Data_header = yaml.load(F.split('---')[1], Loader=yaml.FullLoader)
  # find the ID by slug/url
  if Data_header['url'] in [x['slug'] for x in Doc_list]:
    # 如果有單獨指定語雀標題：
    try:
        if Data_header['ytitle'] ==  "" :
            Title = Data_header['title']
        else:
            Title = Data_header['ytitle']
    except:
        Title = Data_header['title']
    data = {
    #'id': 我不想指定， 還是隨機吧
    'slug': Data_header['url'], # 這個還是最好要一個。 這個是網址
    'title': Title, # 這就不用多說了吧。
    'format': 'markdown',  # 這必須markdown 呀
    'body': MDbody_clean(F),
    'status': "1" # 0 是草稿， 直接發佈把
    }
    Doc_ID = [x['id'] for x in Doc_list][[x['slug'] for x in Doc_list].index(Data_header['url'])]
    header = {"X-Auth-Token": Identity['Token']}
    url = 'https://www.yuque.com/api/v2/repos/'+str(Repos_ID)+'/docs/'+ str(Doc_ID)
    Doc_Result = requests.put(url, data = data, headers = header).json()['data']
    print(MD,"is updated")
  else:
    print(MD,' \033[91m', "這個文件還沒有被創建。我懶得寫一個新建接口了（防止太混亂）\n所以請覈對以後， 先上新建這個文件，再來更新把= =推薦用瓦雀直接創建", '\033[0m')

def Categ(Category):
    try:
        List = open(Category,'r').read().replace(" ",'').split("](")
        Cate_list = [A.split(")")[0] for A in List][1:]
        return "導入成功", Cate_list
    except:
        return "導入失敗", []

def run(MD):
    print("updating for:", MD)
    Cate_state , Cate_reuslt = Categ(Category)
    print("目錄:", Cate_state)
    try:
      Data_header = yaml.load(open(MD,'r').read().split('---')[1], Loader=yaml.FullLoader)
      if Data_header['url'] not in Cate_reuslt and Cate_state == "導入成功" :
          print(MD +' \033[91m', "該文檔未加入目錄", '\033[0m')
      MDupDate(MD, Repos_ID, Doc_list)
    except:
      print( MD + ' \033[91m' + "UPDAT FAILED!!!" + '\033[0m')
    #  線程等待

Token = open(Token,'r').read().strip()
# Token = open('/home/ken/.yuqueToken','r').read().strip()
Identity = Yml_json('yuque.yml')
Identity.update({'Token':Token})
Repos_ID = ReporsID_get(Identity)
Doc_list = DocList_get(Repos_ID)


for MD in INPUT:
    run(MD)
'''
if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(run, INPUT)
'''
