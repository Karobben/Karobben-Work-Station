#!/usr/bin/env python3
'''
This script is for samply keep typing a
Squirtel on you terminal
Please Enjoy it
'''
import os
import time
Squirt_list1 = ['     AAAA         AAA', '    ADDDDAA      ADDDA', '   ADDDDDDDAA   ADDDDDA', '   ADDDDDDDABAA ADDDADA', '  ABDDDDDDDDBBBADDDADDA', '  ADDDDFADDDFBBBADDADDA', '  ADDDDABDDDFBBBADAAAA', '   ADDDABDDDAFBBBAA', '    AADDDDAADDFBBA', '    ADAAAADDDDFBBA', '     AACCADDDAFBBA', '       ACCAAAAFBBA', '      ADACCCCCAFA', '       AAAACCDAFA', '          AAADAA', '           ADDDA', '            AAA']
Squirt_list2 = ['', '    AAAA           AAA', '   ADDDDAA        ADDDA', '  ADDDDDDDDAA    ADDDDDA', '  ADDDDDDDDABAA  ADDDADA', ' ADDDDDDDDDDBBBAADDDADDA', ' ADDDDFADDDDFBBBADDADDA', ' ADDDDABDDDDFBBBADAAAA', '  ADDDABDDDDAFBBBAA', '   AADDDDDAADDFBBA', '     AACCADDDAFBBA', '       ACCAAAAFBBA', '      ADACCCCCAFA', '       AAAACCDAFA', '          AAADAA', '           ADDDA', '            AAA']

Squir_patern = {" ":"  ",
'A':'\x1b[7;30;40mAA\x1b[0m'  , 'B':'\x1b[7;31;41mB\u2580\x1b[0m',
"C":"\x1b[6;33;43mCC\x1b[0m"  , "D":"\x1b[6;34;44mDD\x1b[0m",
'E':'\x1b[30;0;2mEE\x1b[0m'   , 'F':'\x1b[7;37;47mEE\x1b[0m'  }

def Squrt(Squirt_list):
  Result = ""
  for i in Squirt_list:
    Line_tmp = ""
    for ii in i:
      Line_tmp += Squir_patern[ii]
    Result += Line_tmp + "\n"
  os.system("clear")
  print(Result)

while 1 == 1:
    Squrt(Squirt_list1)
    time.sleep(0.5)
    Squrt(Squirt_list2)
    time.sleep(0.5)
