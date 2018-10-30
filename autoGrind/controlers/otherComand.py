import threading
import pyautogui as py
import time
import tkinter as tk

class OtherComandControler(object):
    def __init__(self):
        self.actionNameList = list(('',''))
        self.savedActions=list()
        self.namedrop = tk.StringVar()
        self.namedrop.set('enter task name')
        self.name=tk.StringVar()
        self.position=0,0
        self.color=(0,0,0)
    def getPntCLR(self):
        self.position=0,0
        pntThread = threading.Thread(target=self.mouseMove)
        pntThread.start()
        pass

    def gotPoint(self, setx, sety,Color):

        print(' x='+ str(setx)+' y='+str(sety)+' color ='+ str(Color))
        self.setinfo(' x='+ str(setx)+' y='+str(sety)+' color ='+ str(Color))

    def mouseMove(self):
        myMouse = py
        oPos = 0
        scimg=py.screenshot()
        while True:
            time.sleep(1)
            nPos = myMouse.position()
            if oPos == nPos:
                self.counter += 1
                print(self.counter)
                if self.counter > 4:
                    self.position = nPos
                    clr=scimg.getpixel(nPos)
                    self.color=clr
                    self.gotPoint(nPos[0],nPos[1],clr)
                    return

            else:
                oPos = nPos
                self.counter = 0
            self.setinfo(str(5 - self.counter) + ' seconds till capture')


    def setinfo(self,text):
        pass

    def getDelay(self):
        pass

    def Save(self):
        actions = ['Left Click', 'Right Click', 'Drag Start',
                   'Drag Stop', 'Type', 'Color Stall', 'Color Condition', 'name groop']
        act=actions.index(self.getAction())
        self.sendInfo(act,int(self.getDelay()),list(self.position),list(self.color),self.getChecked())
        self.close()
        pass

    def sendInfo(self,actNum, delay, position, color,checked):
        print(actNum,delay,position,color,checked)
        pass

    def close(self):
        pass

    def getAction(self):
        pass

    def getChecked(self):
        pass

    def namechanged(self,event):
        self.name.set(self.namedrop.get())
        pass

    def getNamedAction(self):
        pass

    def setNamedAction(self):
        pass

    def actionChanged(self):
        pass