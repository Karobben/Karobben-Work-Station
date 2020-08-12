#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '-I', '--input', nargs='+',
                    help='Input Video file')     #输入文件
parser.add_argument('-o', '-U', '--output',
                    default = "out_test.avi",
                    help='Output Video file, default as "out_test.avi"')     #输出文件
parser.add_argument('-f','-F','--fps', default = 24,
                    type = int,
                    help='Speed up by ratio, "default = 24"')     #帧率

#获取参数
args = parser.parse_args()
File = args.input
OUTPUT = args.output
fps = args.fps

import cv2, os

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


Typ_in = FD_judge(File)

if Typ_in == "Directory":
    List = os.popen('ls '+File).read().split('\n')[:-1]
    img = cv2.imread(File +"/"+List[0])
else:
    List = File
    img = cv2.imread(List[0])

size = (len(img[0]),len(img))
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
videowriter = cv2.VideoWriter(OUTPUT,fourcc,fps,size)

for i in List:
    if Typ_in == "Directory":
        img = cv2.imread(File +"/"+i)
    else:
        img = cv2.imread(i)
    videowriter.write(img)

videowriter.release()
