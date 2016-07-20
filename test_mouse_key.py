import os,sys
from mouse_key import *

def move_click(x,y,t=0.01):
    mouse_move(x,y)
    time.sleep(t)
    mouse_click(x,y)
def readFile(fname):
    with open(fname, 'r') as f:
        return f.readlines()


#load url list
urlList = readFile(sys.argv[1])
for url in urlList:
    #open chrome
    os.system("start chrome %s" % (url))
    time.sleep(10)
    #move to input tag
    move_click(383,288)
    time.sleep(1)
    #input sexy
    key_input("sexy")
    sendKey(0x0D)
    time.sleep(1)
    #input enter key
    sendKey(0x0D)
    time.sleep(1)
