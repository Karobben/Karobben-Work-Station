#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i','-I','--input')     #输入文件
parser.add_argument('-o','-U','--output')     #输入文件

#获取参数
args = parser.parse_args()
INPUT = args.input
OUTPUT = args.output

import multiprocessing as mp
import time, re
import requests


F = open(INPUT,'r')
File = F.read()

pattern = re.compile(r'\(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\) \((?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F])| )+'+"\)") # 匹配模式
List = pattern.findall(File)

def RespTime(url,return_dict):
  # Page is exist or not
  url = url.split(')')[0].replace("(","")
  try:
    try:
      r = requests.get(url, timeout=20)
      rtime = str(r.elapsed.total_seconds())+"s)"
    except:
      rtime = "OutOfTime)"
  except:
    rtime = "Failed)"
  Result = "("+url+") (Update:"+time.strftime("%D")+ "; "+ rtime
  return_dict[Result] = Result

if __name__ == '__main__':
    manager = mp.Manager()
    return_dict = manager.dict()
    jobs = []
    for i in List:
        p = mp.Process(target=RespTime, args=(i,return_dict))
        jobs.append(p)
        p.start()
    for proc in jobs:
        proc.join()

DB="\n".join(return_dict.values())


for i in List:
  Str = i.split(")")[0].replace("(",'')
  #pattern = re.compile(Str+r"\)[ ]\((?:[a-zA-Z]|[0-9]|[:/|\.]|;)+[ ][0-9]|[a-zA-Z]|\.?+")
  pattern = re.compile(Str+"\) \(.+")
  i2 = "("+pattern.findall(DB)[0]
  print(i,i2,sep='\n')
  File = File[:File.find(i)] + i2+ File[File.find(i)+len(i):]

F = open(OUTPUT,'w')
F.write(File)
F.close()
