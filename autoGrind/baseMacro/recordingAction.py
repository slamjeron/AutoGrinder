
import time

from autoGrind.Gui2.otherComand import AddComPage
from autoGrind.controlers.pageBluePrint import mainPagebuttonBluePrint
import pyautogui as mouse
import tkinter as tk

from autoGrind.dataTypes.dataTypes import Color,KeyBoard,Mouse

'''
to record we need to have a key and mouse hook
i will also need to be able to have the user create hot keys
'''
class recorder(mainPagebuttonBluePrint):




    def record(self, redy=False):
        if redy:
            print('isRecording')
            self.isRecording = True
            print(time.time() - self.secondes)
            self.secondes = time.time()
            self.recording=self.getRecording()
            self.goBTN = False

    def __init__(self):
        object.__init__(self)
        print('recorder ready')
        self.isRecording = False
        self.programOn=True
        self.up=True
        self.recording=list()
        self.secondes = time.time()
        self.index=0
        self.bmcstart=True
        self.goBTN=False
        self.comandWindow= tk.Toplevel
        self.comandPage=AddComPage

    def on_click(self, x, y, button, pressed):
        if self.isRecording:
            if pressed:
                if self.up:
                    self.up = False
                    pnt = [int(x), int(y)]
                    self.addToRecord(0,pnt,'')

            else:
                self.up = True

    def kill(self):
        self.programOn=False


    def on_key_press(self, key_code):
        """
        determins what keys do and records them
        """
        key_code = self.formatKeyIn(key_code)

        if self.programOn == False:
            return

        if self.isRecording:
            self.recordKey(key_code)


    def showRecordedItem(self,list):
        return

    def savecomand(self, actNum, delay, position=None, color=None, checked=None, keypresses=None):
        action = None

        if actNum == 6:
            action = Color(delay, 0, position, color, checked)
            print(str(action))
        if actNum == 7:
            action = Color(delay, 1, color, position, checked)
        if actNum < 5:
            action = Mouse(delay, actNum,position)
        self.recording.append(action)
        self.index += 1
        self.showLine(str(action))
        self.isRecording = True
        self.secondes = time.time()

    def recordKey(self,key_code):
        if key_code=='+':
            self.recording = self.getRecording()
            # open the other comand view
            self.comandWindow = tk.Toplevel()
            self.comandPage=AddComPage(self.comandWindow)
            self.comandPage.pack()
            self.isRecording=False


            self.comandPage.controler.sendInfo=self.savecomand
            pass

        else:

            self.addToRecord(4, '', key_code)

    def stopRecording(self):
        print('stoping')
        self.setRecording(self.recording)
        self.isRecording=False
    def bmcrec(self,key,diff):
        if self.goBTN == False and self.bmcstart:
            if mouse.pixelMatchesColor(792, 716, (143, 216, 35)):
                lis = [5, 3, [791, 711], [143, 216, 35], True]
                print('ready for next round')
                self.recording.append(lis)
                self.index += 1
                self.showLine(lis)
                self.secondes = time.time()
                self.secondes -= 0.3
                self.goBTN = True


        if self.goBTN:
            if mouse.pixelMatchesColor(809, 685, (5, 146, 239)):
                self.goBTN = False
            des=round(diff)-diff
            if key=='' or key =='space' or key == ',' or key == '.':
                if diff > 1:
                    diff = 1+des

                return diff
            else:
                if diff > 4:
                    diff = 4+des
                return diff
        if key == 'space':

            self.goBTN = False
        return diff


    def addToRecord(self,action,pnt,key):
        if self.isRecording:
            diff=  time.time()-self.secondes
            diff=self.bmcrec(key,diff)

            diff = round(diff,2)
            if diff>0:
                if action == 4:
                    lis=KeyBoard(diff,0,key)
                if action==0:
                    lis=Mouse(diff,Mouse.leftClick,pnt)
                self.recording.append(lis)

                # self.addRecTtem(self.index,lis)
                self.index+=1
                self.showLine(str(lis))
                self.secondes = time.time()


    def formatKeyIn(self,key_code):
        try:
            key_code='{0}'.format(key_code.char)
        except AttributeError:
            key_code = '{0}'.format(key_code)
        key = str(key_code).replace('Key.', '')
        return key


