#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/08/03
# @Author  : Karobben
# @Site    : China
# @File    : VideoSlice.py
# @Software: Atom

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i','-I','--input',
                    help='Input Video file')     #输入文件
parser.add_argument('-o','-U','--output', default = "img_OUT",
                    help='Output Video file, default as "out_test.avi"')     #输出文件
parser.add_argument('-r','-R','--ratio', default = 1,
                    type = int,
                    help='Speed up by ratio, "default = 2"')     #输出文件
parser.add_argument('-f','-F','--fps', default = 0,
                    type = int,
                    help='Speed up by ratio, "default = 2"')     #输出文件
parser.add_argument('-inf', nargs='?',default=True)
parser.add_argument('-s','-S','--splice', default = False,
                    type = str,
                    help='splice: -s 0,100')     #输出文件

#获取参数
args = parser.parse_args()
INPUT = args.input
OUTPUT = args.output
Ratio = args.ratio
fps_o = args.fps
Splice = args.splice
inf = args.inf


import cv2, os



#INPUT = 'bug.avi'
cap = cv2.VideoCapture(INPUT)
fps_c = cap.get(cv2.CAP_PROP_FPS)
Video_h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
Video_w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
print("Current fps:",fps_c)


#OUTPUT = "out_test.avi"
if fps_o == 0:
    fps_o = fps_c



def Video_speed(cap, OUTPUT):
    if Splice:
        S_E = [int(i) for i in Splice.split(",")]
        i = S_E[0]
        while i < S_E[-1]:
            if i % Ratio == 0:
                cap.set(1, i-1)
                ret,frame=cap.read()
                Video = INPUT.split('/')[-1]
                cv2.imwrite(OUTPUT+"/" +Video+"_" +str(i)+"_.png" ,frame)
            i +=1


if inf == True:
    Video_speed(cap, OUTPUT)
