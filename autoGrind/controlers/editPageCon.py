import tkinter

from autoGrind.controlers.editPageBluePrint import bluePrint
from autoGrind.controlers.pageBluePrint import mainPagebuttonBluePrint
import threading
import pyautogui as mouse

import time

from autoGrind.dataTypes.dataTypes import typerReader


class editCon(mainPagebuttonBluePrint,bluePrint):

    def __init__(self):

        self.recording=list()
        self.linesToEdit=list()
        self.enterlines=None
        self.close=None
        self.update=None
        self.dataTxt = tkinter.StringVar()

    def delete_act(self):
        lines=''

        lines =self.getlines()
        super().delete_act()
        self.recording= self.getRecording()
        self.linesToEdit=list()
        lines=(list(map(int,lines.split(','))))
        lines.sort(key=int,reverse=True)
        print(lines)
        for item in lines:
            del self.recording[item]
        self.showAll()
        self.close()

    def showEditLines(self):
        strin=','.join(map(str,self.linesToEdit))

        if strin is not None:
            self.enterlines(strin)


    def saveComand(self,action,timeDelay,point,keyevent,linsEdit):
        actions=['Same','Move cursor', 'Left Click', 'Drag Start',
                           'Drag Stop', 'Right Click', 'Type', 'Color Stall', 'Color Condition','name groop']
        self.linesToEdit = list()
        self.recording=self.getRecording()
        for item in linsEdit.split(','):

            print(item)
            self.linesToEdit.append(int(item))

        if action =='Same':
            pass
        else:
            for line in self.linesToEdit:
                if line < len(self.recording):
                    self.recording[line]=typerReader.setObject(self,num=actions.index(action))
        if timeDelay == 'Same':
            print('')
        else:
            for line in self.linesToEdit:
                if line<len(self.recording):
                    self.recording[line].secondDelay=float(timeDelay)

        if point[0] =='Same':
            pass
        else:
            for line in self.linesToEdit:
                if line < len(self.recording):
                    if self.recording[line].object == 'mouse':
                        self.recording[line].position[0]=int(point[0])
        if point[1] =='Same':
            pass
        else:
            for line in self.linesToEdit:
                if line < len(self.recording):
                    if self.recording[line].object == 'mouse':
                        self.recording[line].position[1]=int(point[1])

        if keyevent=='Same':
            pass
        else:
            for line in self.linesToEdit:
                if line < len(self.recording):
                    self.recording[line][3]=keyevent
        self.setRecording(self.recording)
        self.showAll()
        self.close()
        return
    def getPoint(self,setx,sety):
        self.counter=0
        self.mousposition=list()
        pntThread = threading.Thread(target=self.mouseMove)
        pntThread.start()
        self.setXpoint=setx
        self.setYpoint=sety


    def mouseMove(self):
        myMouse=mouse
        oPos=0
        while True:
            time.sleep(1)
            nPos=myMouse.position()
            if oPos == nPos:
                self.counter+=1

                if self.counter>5:
                    self.mousposition=nPos
                    x,y=self.mousposition
                    self.setXpoint(str(x))
                    self.setYpoint(str(y))
                    self.dataTxt.set('capturing in ' + str(6 - self.counter))
                    return
                self.dataTxt.set('capturing in ' + str(6 - self.counter))
            else:
                oPos=nPos
                self.counter=0

    def actionDrop(self):
        pass