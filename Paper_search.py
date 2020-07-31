#!/usr/bin/env python3
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-i','-I','--input',nargs='+')    #输入文件
parser.add_argument('-t','-T','--title')    #输入文件

args = parser.parse_args()
INPUT = args.input
Title = args.title



from urllib.request import quote, unquote, urlopen
from bs4 import BeautifulSoup

#url1 = "https://www.sciencedirect.com/search?qs=plant%20inhibitor" + Title
#url2 = "&qs=n&form=QBRE&sp=-1&pq=rb+regeneration&sc=0-15&sk=&cvid=3C794B07B2E44D1CA680B48B8CC1EEBF"
#url1 = url1 + url2

url1 = "https://www.sciencedirect.com/search?qs=plant%20inhibitor"
#ret1 = quote(url1, safe=";/?:@&=+$,", encoding="utf-8")
html = urlopen(url1).read().decode('utf-8')
soup = BeautifulSoup(html, features='lxml')

for i in (soup.find_all("h2")):print(i)

F = open('test.md','w')
F.write(html)
F.close()
