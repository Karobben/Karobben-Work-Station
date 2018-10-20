#!/usr/local/bin/python3.7
import argparse

#命令行输入参数处理
parser = argparse.ArgumentParser()
parser.add_argument('-i','-I','--input')     #输入文件
parser.add_argument('-o','-O', '--output',default = "out.table")   #输出文件

#获取参数
args = parser.parse_args()

FILE = args.input
OUTPUT = args.output


####grep information from uniprot
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import re
import pandas as pd

import multiprocessing as mp
import time

sit="https://www.uniprot.org/uniprot/"
list = pd.read_csv(FILE,header=None)


def Trans(i):
    url = sit+i
    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, 'lxml')
    A_title = soup.find('head').find('title')
    A_str = A_title.get_text()
    B_title = A_str.split(sep= " - ")[0:3]
    Anno = soup.find(property="schema:text")
    Anno = str(Anno)
    if Anno == 'None':
        Anno = "Said... Can't find usefull information"
    else:
        Anno = Anno.split(">",1)
        Anno = Anno[1].split("<",-1)[0]
    TR = Anno.replace("/"," or ")
    TR = TR.replace(" ","%20")
    TR = TR.replace(":","%3A")
    TR = TR.replace(">","%3E")
    TR = TR.replace("+","%2B")
    TR = TR.replace("=","%3D")
    U_1="http://www.youdao.com/w/eng/"
    U_2="/#keyfrom=dict2.index"
    url2=U_1 + TR + U_2
    html = urlopen(url2).read().decode('utf-8')
    soup = BeautifulSoup(html, 'lxml')
    Tran=soup.find(id="fanyiToggle")
    Tran=str(Tran)
    if Tran == 'None':            #This is a word
        Tran = str(soup.find(id="phrsListTab"))
        if Tran == 'None':
            Tran=str("I can't underisrand")  #this is a wrong word
        else:
            Tran = str(soup.find(id="phrsListTab").find_all("li"))
        if Tran =='[]':           #This word could only find on Internet
            Tran=soup.find(id="tWebTrans")
            Tran=Tran.find_all('span')
            Tran=str(Tran).replace("[]","")
            Tran=str(Tran).replace(" ","")
            Tran=str(Tran).replace("\n","")
            Tran=Tran.replace("<span>",'')
            Tran=Tran.replace("</span>",'')
        else:                     #This word could find on official dictionary
            Tran=Tran.replace("<li>",'')
            Tran=Tran.replace("</li>",'')
    else:
        Tran=soup.find(id="fanyiToggle").find_all('p')[1]
        Tran=str(Tran)
        Tran=Tran.replace("<p>",'')
        Tran=Tran.replace("</p>",'')
    R_tmp = i+"\t"+B_title[0]+ "\t"+ B_title[1]+ "\t" + B_title[2]+ "\t" +Anno + "\t" + Tran
    print(R_tmp)

A=time.time()
def multicore():
  pool = mp.Pool(processes=20)
  for i in list[0]:
    multi_res = [pool.apply_async(Trans,(i,))]
  pool.close()
  pool.join()

if __name__ == '__main__':
    multicore()
print("Time spend= ",time.time()-A)
