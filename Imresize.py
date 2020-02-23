#!/usr/local/bin/python3.7
'''
Author: Karobben
Github: https://github.com/Karobben
'''
import argparse
import os
from os.path import getsize
import PIL.Image as Image

parser = argparse.ArgumentParser()
parser.add_argument('-i','-I','--input',nargs='+')    #输入文件
parser.add_argument('-o','-O','--output',default = "OUT")   #输出文件
parser.add_argument('-r','-R','--ratio', type = int,default = 2)    #resize ratio
parser.add_argument('-w','-W','--width',default = "NA") #resize by width
parser.add_argument('-t','-T','--height',default = "NA")    #resize by Height
parser.add_argument('-p','-P','--print',default = "None")    #resize by Height
parser.add_argument('-inf','-INF','--infor',default = "Not", nargs='?')    #resize by Height
parser.add_argument('-f','-F','--formatout',default = "Origin")    #resize by Height
parser.add_argument('-q','-Q','--quality',default = "85")    #resize by Height

#获取参数
args = parser.parse_args()
INPUT = args.input
OUTPUT = args.output
R_img = args.ratio
W_img = args.width
H_img = args.height
PRINT = args.print
INFORM = args.infor
Format = args.formatout
Quality = args.quality

def size_format(b):
    if b < 1000:
              return '%i' % b + 'B'
    elif 1000 <= b < 1000000:
        return '%.1f' % float(b/1000) + 'KB'
    elif 1000000 <= b < 1000000000:
        return '%.1f' % float(b/1000000) + 'MB'
    elif 1000000000 <= b < 1000000000000:
        return '%.1f' % float(b/1000000000) + 'GB'
    elif 1000000000000 <= b:
        return '%.1f' % float(b/1000000000000) + 'TB'

def FD_judge(path):
    result = ""
    if len(path) > 1:
        result = "Files"
    elif os.path.isdir(path[0]):
        result = "Directory"
    elif os.path.isfile(path[0]):
        result = "File"
    else:
        result = "path is incorrect"
    return result

def Calc_WH(w,h,W_img,H_img,R_img):
    if W_img != "NA" and H_img == "NA": #Resize by Width
        print('Resize by Width')
        R = w/ int(W_img)
        w=int(w/R)
        h=int(h/R)
    elif H_img != "NA" and W_img == "NA":   #Resize by Height
        print("Resize by Height")
        R = h/ int(H_img)
        w=int(w/R)
        h=int(h/R)
    elif H_img != "NA" and W_img != "NA":   #Resize by Width and Height
        print('Resize by Width and Height')
        w=int(W_img)
        h=int(H_img)
    else:
        print("Resize by ratio, R="+str(R_img))
        w=int(w/R_img)
        h=int(h/R_img)
    return w,h

def Resize(path,W_img,H_img,R_img):
    Img=Image.open(path)
    w,h=Img.size
    w,h=Calc_WH(w,h,W_img,H_img,R_img)
    Img_out=Img.resize((w,h),Image.ANTIALIAS)
    return Img_out

def Resize_loop(INPUT,OUTPUT):
    if Typ_in == "File":
        Result = Resize(INPUT,W_img,H_img,R_img)
        OUTPUT = OUT_fig(INPUT,OUTPUT)
        Result.save(OUTPUT)
    elif Typ_in == "Files":
        List = os.popen("ls "+INPUT).read().split('\n')[:-1]
        for i in List:
            Result = Resize(i,W_img,H_img,R_img)
            OUTPUT = OUT_fig(i,OUTPUT)
            Result.save(OUTPUT)
    elif Typ_in == "Directory":
        List = os.popen("ls "+INPUT+"/*").read().split('\n')[:-1]
        for i in List:
            print("INPUT =  ",i)
            Result = Resize(i,W_img,H_img,R_img)
            OUTPUT = args.output
            OUTPUT = OUT_fig(i,OUTPUT)
            Result.save(OUTPUT)

def IMG_inf(INPUT):
    Space = size_format(getsize(INPUT))
    Img = Image.open(INPUT)
    Name    = Img.filename
    Format  = Img.format_description
    Mode    = Img.mode
    try:
        Bit     = "bit:" + str(Img.bits)
    except:
        Bit     = "bit:NA"
    try:
        Dpi     = "dpi:" + 'x'.join([str(x) for x in Img.info['dpi']])
    except:
        Dpi     = "dpi: NA"
    Size    = "size:" + 'x'.join([str(x) for x in Img.size])
    Result = Name +"\t"+"    ".join([Space, Size, Dpi, Format,Mode,Bit])
    return Result

# OUTPUT path
def OUT_fig(INPUT,OUTPUT):
    if Typ_in=="File" and OUTPUT == "OUT":
        OUTPUT = "Re_" + INPUT
    elif Typ_in=="File" and OUTPUT != "OUT":
        OUTPUT = OUTPUT
    else:
        if not os.path.exists(OUTPUT):
            os.makedirs(OUTPUT)
        OUTPUT = OUTPUT +"/"
    if Typ_in != "File":
        OUTPUT = OUTPUT+ INPUT.split('/')[-1]
    '''
    if Typ_in == "Directory":
        print("OUT:",INPUT)
        OUTPUT = OUTPUT+ INPUT.split('/')[-1]
    print(OUTPUT)
    '''
    if Format != "Origin":
        print("Switch Format")
        OUT_F = OUTPUT.split('.')[-1]
        OUTPUT = OUTPUT.replace(OUT_F,Format)
    return OUTPUT

def IMG_Inf(INPUT):
        if Typ_in == "File":
            print(IMG_inf(INPUT))
        elif Typ_in == "Files":
            #List = os.popen("ls "+INPUT).read().split('\n')[:-1]
            List = os.popen("ls "+INPUT).read().split('\n\n')[0].split('\n')[:-1]
            for i in List:
                print(IMG_inf(i))
        elif Typ_in == "Directory":
            List = os.popen("ls "+INPUT+"/*").read().split('\n\n')[0].split('\n')[:-1]
            for i in List:
                print(IMG_inf(i))


if INFORM == "Not": # Resize
    Typ_in = FD_judge(INPUT)
    for i in INPUT:
        print(Typ_in)
        Resize_loop(i,OUTPUT)
else:  # img information
    Typ_in = FD_judge(INPUT)
    for i in INPUT:
        IMG_Inf(i)

'''
if INFORM == "None": # Resize
    Typ_in = FD_judge(INPUT)
    print(Typ_in)
    OUTPUT = OUT_fig(INPUT,OUTPUT)
    Resize_loop()
else:  # img information
    Typ_in = FD_judge(INPUT)
    if Typ_in == "File":
        print(IMG_inf(INPUT))
    elif Typ_in == "Files":
        #List = os.popen("ls "+INPUT).read().split('\n')[:-1]
        List = os.popen("ls "+INPUT).read().split('\n\n')[0].split('\n')[:-1]
        for i in List:
            print(IMG_inf(i))
    elif Typ_in == "Directory":
        List = os.popen("ls "+INPUT+"/*").read().split('\n\n')[0].split('\n')[:-1]
        for i in List:
            print(IMG_inf(i))

'''
