import threading
import pyautogui as py
import time
import tkinter as tk


class OtherComandControler(object):
    actions = ['mouse move','Left Click', 'Right Click', 'Drag Start',
               'Drag Stop', 'Type', 'Color Stall', 'Color Condition', 'name groop']

    def __init__(self):
        self.actionNameList = list(('', ''))
        self.savedActions = list()
        self.namedrop = tk.StringVar()
        self.namedrop.set('enter task name')
        self.name = tk.StringVar()
        self.position = 0, 0
        self.color = (0, 0, 0)
        self.index = 6
        self.editButtonTxt = tk.StringVar()
        self.KeyPreses=None


    def getPntCLR(self):
        if self.index==4:
            self.recordKeys()
        else:
            self.position = 0, 0
            pntThread = threading.Thread(target=self.mouseMove)
            pntThread.start()
        pass

    def recordKeys(self):
        print('recording keys')

    def gotPoint(self, setx, sety, Color):

        print(' x=' + str(setx) + ' y=' + str(sety) + ' color =' + str(Color))
        self.setinfo(' x=' + str(setx) + ' y=' + str(sety) + ' color =' + str(Color))

    def mouseMove(self):
        myMouse = py
        oPos = 0
        scimg = py.screenshot()
        while True:
            time.sleep(1)
            nPos = myMouse.position()
            if oPos == nPos:
                self.counter += 1
                print(self.counter)
                if self.counter > 4:
                    self.position = nPos
                    clr = scimg.getpixel(nPos)
                    self.color = clr
                    self.gotPoint(nPos[0], nPos[1], clr)
                    return

            else:
                oPos = nPos
                self.counter = 0
            self.setinfo(str(5 - self.counter) + ' seconds till capture')

    def setinfo(self, text):
        pass

    def getDelay(self):
        pass

    def Save(self):
        if self.index == 6 or self.index==7:
            self.sendInfo(self.index, int(self.getDelay()), list(self.color), list(self.position), self.getChecked())
        elif self.index<5:
            self.sendInfo(self.index, int(self.getDelay()), list(self.position))
        elif self.index==5:
            self.sendInfo(self.index,int(self.getDelay()), keypresses=list(self.KeyPreses))
        self.close()
        pass

    def sendInfo(self, actNum, delay, position=None, color=None, checked=None,keypresses=None):
        print(actNum, delay, position, color, checked,keypresses)
        pass

    def close(self):
        pass

    def getAction(self):
        pass

    def getChecked(self):
        pass

    def namechanged(self, event):
        self.name.set(self.namedrop.get())
        pass

    def getNamedAction(self):
        pass

    def setNamedAction(self):
        pass

    def actionChanged(self, recvar):
        if recvar=='Same':
            self.index=8
        else:
            self.index = self.actions.index(recvar)
            if self.index < 5:
                self.editButtonTxt.set('get cursor position')
            elif self.index == 6 or self.index == 7:
                self.editButtonTxt.set('get Clr and Pixel')
            elif self.index==5:
                self.editButtonTxt.set('get keys')
            pass
