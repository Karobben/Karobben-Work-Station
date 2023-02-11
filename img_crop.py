#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i','-I','--input')    
parser.add_argument('-o','-U','--output', default = None , nargs='?')   
parser.add_argument('-r','-R','--risze',  default='1,1', nargs='?', help = '"1,1" resize the output image')    
parser.add_argument('-c','-C','--crop',  help = '"100,200,100,300" axis of the crop position: x1 to x2, y1 to y2')
parser.add_argument('-s','-S','--show',  default=None, nargs='?', help = '"1,1" resize the output image')    
parser.add_argument('-a','-A','--angle',  default=None, nargs='?', help = 'angle for rotate the output image')    

##
args = parser.parse_args()
INPUT = args.input
RESIZE = args.risze
CROP = args.crop
OUTPUT = args.output
SHOW = args.show
ROTATE = args.angle

import cv2
import numpy as np

Crop_l = [int(i) for i in CROP.split(',')]
Resize_l = [float(i) for i in RESIZE.split(',')]
# Load image, grayscale, median blur, Otsus threshold
image_r = cv2.imread(INPUT)
image = image_r
image = image[Crop_l[2]-1:Crop_l[3], Crop_l[0]-1:Crop_l[1]]
Resize_r = (int((Crop_l[1] - Crop_l[0]) * Resize_l[0]), int(Resize_l[1] * (Crop_l[3] - Crop_l[2])))
image = cv2.resize(image, Resize_r, interpolation = cv2.INTER_AREA)


if ROTATE != None:
    ROTATE = float(ROTATE)
    if int(ROTATE) in [90, 180, 270]:
        if ROTATE == 180:
            image = cv2.rotate(image, cv2.ROTATE_180)
        if ROTATE == 270:
            image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        if ROTATE == 90:
            image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    else:
        (h, w) = image.shape[:2]
        (cX, cY) = (w // 2, h // 2)
        # rotate our image by 45 degrees around the center of the image
        M = cv2.getRotationMatrix2D((cX, cY), -1 * ROTATE, 1.0)
        image = cv2.warpAffine(image, M, (w, h))

if SHOW == None:
    ptLeftTop = (Crop_l[0], Crop_l[2])
    ptRightBottom = (Crop_l[1], Crop_l[3])
    point_color = (0, 0, 255) # BGR
    thickness = 1
    lineType = 8
    image_r = cv2.rectangle(image_r, ptLeftTop, ptRightBottom, point_color, thickness, lineType)
    cv2.imshow('image_r', image_r)
    cv2.imshow('image', image)
    cv2.waitKey()    
    cv2.destroyAllWindows()

if OUTPUT != None:
    cv2.imwrite(OUTPUT,image)
