#!/usr/bin/env python3
'''
This script is helping you to working with your Schedule
smoothly. Schedule list is stored at "Dic_Behavior"
I also made I radom pool in "List_R" to avoid making anoing
choice. Voice engine is require for Sox and pyttsx3
For prepareing this two:

sudo apt install sox
pip install pyttsx3
'''
import time, random
import subprocess as sup

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-m','-M','--Mute',default="No")     #输入文件

#获取参数
args = parser.parse_args()
Mute = args.Mute

'''
Functions for Mainstring
'''
def Find_List(List,ele):
    Num = -1
    for i in List:
        Num +=1
        if i == ele:
            break
    return Num

def Time_out():
    Time_series = list(Dic_Behavior.keys())
    Time_now = time.ctime().split(" ")[3][:-3]
    #
    Time_series.append(Time_now)
    Time_series.sort()
    L_Num2  = Find_List(Time_series,Time_now)
    Time_No = Time_series[L_Num2-1]
    Time_Duration = Time_De(Time_No,Time_now)
    Behavior = Dic_Behavior[Time_No]
    if Behavior == "S":
        Behavior = Sub_n
    elif Behavior == "B":
        Behavior = "Break for 10 mins"
    return Behavior,Time_now,Time_Duration,Time_No,L_Num2

def Time_De(T1,T2):
    T1_h = int(T1.split(":")[0])
    T1_m = int(T1.split(":")[1])
    T2_h = int(T2.split(":")[0])
    T2_m = int(T2.split(":")[1])
    return abs((T2_m - T1_m) + (T2_h - T1_h)*60)

def Time_miner(T1,Num):
    T1_h = int(T1.split(":")[0])
    T1_m = int(T1.split(":")[1])
    MM = T1_h*60 + T1_m - Num
    H = MM//60
    H = H%24
    M = MM%60
    if H < 10:
        H = "0" + str(H)
    if M < 10:
        M = "0" + str(M)
    H,M = str(H),str(M)
    return H+":"+M

'''
Vocive engine
'''
# giving the path for the mp3 file
if Mute == "No":
    Music_Path = "/home/ken/Music/Jarvis/relax.wav.wav"
    try:
        pp = sup.Popen(("play"), stdin=sup.PIPE, stdout= sup.PIPE, stderr= sup.PIPE, encoding="utf-8")
    except:
        print('''Please install Sox:
        sudo apt install Sox
        or run with --Mute Yes\n\n\n\n''')
        raise Error
    import pyttsx3 # voice engine. If you don't need the Voice notice, please denote it
    def Speak(INPUT):
        engine = pyttsx3.init()
        engine.setProperty('voice','english_rp') ##Change the voice
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate-50) ##spead rate
        volume = engine.getProperty('volume')
        engine.setProperty('volume', volume+0.25) ##change the volume
        print(INPUT)
        engine.say(INPUT)
        engine.runAndWait()
    def Play(INPUT):
        '''
        This functions is require Sox,
        run sudp apt install Sox before Start the Sound Engine
        '''
        sup.run("play "+ INPUT, shell=True)
'''
Date Preparing
'''
# Schedule list
Dic_Behavior = {"09:00":"S",
                "09:50":"B",
                "10:00":"S",
                "10:50":"B",
                "11:00":"S",
                "11:50":"B",
                "12:00":"S",
                "12:50":"Long Break",
                "14:30":"S",
                "15:20":"B",
                "15:30":"S",
                "16:20":"B",
                "16:30":"S",
                "17:20":"B",
                "17:30":"S",
                "18:20":"B",
                "18:30":"S",
                "19:20":"Long Break",
                "20:30":"Extral Reading!",
                "21:20":"B",
                "21:30":"Let's Coding!",
                "22:20":"B",
                "22:30":"Review for the day",
                "24:00":"Sleeping Time!"}
# Random Tasks Pool
List_R = [  "Writing W",
            "Math",
            "Writing R",
            "Vocabulery",
            "Reading",
            "Text"]

List_T = list(List_R)
Behavior_last ="Blank"
Behavior = "Start"
Sub_n = ""
Time_No = "24:00"
L_Num1=0

while True:
#for i in range(100):
    #Time_now = Time_miner("08:00",-i*9)
    time.sleep(2)
    Behavior,Time_now,Time_Duration,Time_No,L_Num2 = Time_out()
    if L_Num1 != L_Num2:
        L_Num1 = L_Num2
        if Dic_Behavior[Time_No] == "S":
            try:
                Sub_n = random.choice(List_T)
            except:
                List_T = list(List_R)
                Sub_n = random.choice(List_T)
            List_T.remove(Sub_n)
            Behavior,Time_now,Time_Duration,Time_No,L_Num2 = Time_out()
        if Mute == "No":
            if "Break" in Behavior:
                Play(Music_Path)
            else:
                Speak(Behavior)
    print(Time_now,len(List_T),Behavior,Time_Duration)
