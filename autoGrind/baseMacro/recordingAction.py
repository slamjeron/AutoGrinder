from pynput import keyboard, mouse
from threading import Thread
import time
'''
to record we need to have a key and mouse hook
i will also need to be able to have the user create hot keys
'''
class recorder(object):




    def __init__(self):
        object.__init__(self)
        print('recorder ready')
        self.recording = False
        self.programOn=True
        self.up=True
        self.array=list()
        self.secondes = time.time()
        self.index=0

    def on_click(self, x, y, button, pressed):
        if self.recording:
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

        if self.recording:
            self.recordKey(key_code)


    def showRecordedItem(self,list):
        return

    def recordKey(self,key_code):
        self.addToRecord(4, '', key_code)

    def startRecording(self):
        print('recording')
        self.recording=True
        print(time.time() - self.secondes)
        self.secondes=time.time()

    def stop(self):
        print('stoping')
        self.recording=False

    def addToRecord(self,action,pnt,key):
        if self.recording:
            diff=  time.time()-self.secondes
            diff = round(diff,2)
            if diff>0:

                milSec = diff

                lis = [action, milSec, pnt, key]
                self.array.append(lis)
                if pnt is not None:
                    pnt=str(pnt)
                else:
                    pnt= str("")
                # self.addRecTtem(self.index,lis)
                self.index+=1
                print(lis)
                self.showRecordedItem(lis)
                self.secondes = time.time()


    def formatKeyIn(self,key_code):
        try:
            key_code='{0}'.format(key_code.char)
        except AttributeError:
            key_code = '{0}'.format(key_code)
        key = str(key_code).replace('Key.', '')
        return key
