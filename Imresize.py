#!/usr/local/bin/python3.7

import argparse
import os
import PIL.Image as Image

parser = argparse.ArgumentParser()
parser.add_argument('-i','-I','--input')    #输入文件
parser.add_argument('-o','-O','--output',default = "OUT")   #输出文件
parser.add_argument('-r','-R','--ratio', type = int,default = 2)    #resize ratio
parser.add_argument('-w','-W','--width',default = "NA") #resize by width
parser.add_argument('-t','-T','--height',default = "NA")    #resize by Height

#获取参数
args = parser.parse_args()
INPUT = args.input
OUTPUT = args.output
R_img = args.ratio
W_img = args.width
H_img = args.height

def FD_judge(path):
    result = ""
    if "*" in path:
        result = "Files"
    elif os.path.isdir(path):
        result = "Directory"
    elif os.path.isfile(path):
        result = "File"
    else:
        result = "path is incorrect"
    return result

print(FD_judge(INPUT))

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


# INput determine

Typ_in = FD_judge(INPUT)

# OUTPUT path
if Typ_in=="File" and OUTPUT == "OUT":
    OUTPUT = "Re_" + INPUT
elif Typ_in=="File" and OUTPUT != "OUT":
    OUTPUT = OUTPUT
else:
    if not os.path.exists(OUTPUT):
        os.makedirs(OUTPUT)
    OUTPUT = OUTPUT +"/"



if Typ_in == "File":
    Result = Resize(INPUT,W_img,H_img,R_img)
    Result.save(OUTPUT)
elif Typ_in == "Files":
    List = os.popen("ls "+INPUT).read().split('\n')[:-1]
    for i in List:
        Result = Resize(i,W_img,H_img,R_img)
        Result.save(OUTPUT + i.split('/')[-1])
elif Typ_in == "Directory":
    List = os.popen("ls "+INPUT+"/*").read().split('\n')[:-1]
    for i in List:
        Result = Resize(i,W_img,H_img,R_img)
        Result.save(OUTPUT+i.split('/')[-1])

