#!/usr/local/bin/python3.7
import cv2
import numpy as np
from mss import mss
from collections import Counter
from pynput.mouse import Button, Controller
import time

import signal

Y_choice2 = "a"

def INPUT_delay():
  class InputTimeoutError(Exception):
    pass
  def interrupted(signum, frame):
    raise InputTimeoutError
  signal.signal(signal.SIGALRM, interrupted)
  signal.alarm(3)
  try:
    BB = input('请在1秒内输入你的名字：')
    signal.alarm(0)  # 读到输入的话重置信号
  except InputTimeoutError:
    BB = 'A'
  return BB

mouse = Controller()

print('The current pointer position is {0}'.format(
    mouse.position))


cords = {'top':800 , 'left': 1935, 'width': 420, 'height': 60 }
A =time.time()

while True:
    with mss() as sct :
        img = np.array(sct.grab(cords)) #sct.grab(cords/monitor)
    #img[img==0]=255
    img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    #resize to reduce cacl
    Ra = 6
    # strat
    Signal = "Run"
    for i in range(int(60/Ra)-4):
        i = i*Ra
        for ii in range(int(420/Ra)-4):
            ii = ii*Ra
            if np.sum(img[i,ii])==0:
                #img[i:i+4,ii:ii+4] = 255
                #print(i,ii)
                mouse.position = (1935+ii+20, 800+i+60)
                mouse.press(Button.left)
                mouse.release(Button.left)
                #time.sleep(0.01)
                Signal = "Break"
                #break
            if Signal == "Break":
                break

    # find the click center
'''
    cv2.imshow('image',img)
    cv2.moveWindow("image",2800,0)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
cv2.destroyAllWindows()
'''
