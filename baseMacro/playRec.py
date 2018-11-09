from pyautogui import *
from threading import Thread
from controlers.pageBluePrint import mainPagebuttonBluePrint
import time

from dataTypes.dataTypes import Mouse,KeyBoard,Color

""" 
use key comands to control actions
"""


class RecPlayer(mainPagebuttonBluePrint):
    def __init__(self):
        self.index = 0
        self.milsec2 = 0
        self.recording = list()
        self.isplaying = False
        self.pause = False
        self.end=False
        self.test=False
        self.secondes = time.time()

        myThread=Thread(target=self.player)
        myThread.start()
        self.looping=False
        self.loopAmount=1
        self.loops = 0
        self.colorChecks=0

    def play(self,redy):
        if redy:
            self.recording=self.getRecording()

            self.secondes = time.time()
            self.index=0
            self.curentsec=1
            if self.looping:
                if self.loopAmount=="loop":
                    self.loopAmount=-1
                else:
                    self.loopAmount=float(self.loopAmount)
            else:
                self.loopAmount=1
            self.loops = 1
        self.isplaying = True
        self.pause = False


    def kill(self):
        self.end=True

    def stop(self):
        self.isplaying=False
        return



    def player(self):


        while self.end is False:
            time.sleep(0.001)
            if self.isplaying:
                if self.pause is False:
                    if self.test:

                        print(len(self.recording))
                    if len(self.recording) < 1:
                        if self.test:
                            print(len(self.recording))
                        self.isplaying = False
                    sec = time.time() - self.secondes
                    sec = round(sec, 2)

                    if len(self.recording) > self.index:
                        sec=time.time() - self.secondes
                        sec =round(sec,2)
                        if sec >= self.recording[self.index].secondDelay:

                            myobject=self.recording[self.index].object

                            self.curentsec=0
                            if myobject == Mouse.object:
                                act=Mouse(*self.recording[self.index].get())
                                pos= act.position
                                if act.event==act.move:
                                    position(*pos)
                                if act.event== act.leftClick:
                                    print('trying to click')
                                    click(*pos)
                                if act.event==act.leftDown:
                                    mouseDown(*pos,'right')
                                self.index += 1


                            if myobject == KeyBoard.object:
                                act=KeyBoard(*self.recording[self.index].get())
                                if act.event== act.Type:
                                    press(act.key)
                                self.index += 1

                            if myobject == Color.object:
                                act=Color(*self.recording[self.index].get())
                                if act.event== act.delay:

                                    if pixelMatchesColor(*act.position,tuple(act.color))==act.onTrue:
                                        self.index += 1




                            self.secondes = time.time()

                    else:
                        try:
                            int(self.loopAmount)
                        except:
                            self.loopAmount=1

                        if self.loopAmount==-1:
                            self.index=0
                            self.curentsec=0

                        elif self.loops<self.loopAmount:
                            print('loops='+str(self.loops))
                            self.loops+=1
                            self.index=0
                            self.curentsec=0
                        else:
                            self.isplaying = False
                            self.loops=0

                    if len(self.recording)>self.index:
                        if self.curentsec<=sec:
                            self.displayCurentInfo(str(sec)+'next action time='+str(self.recording[self.index].secondDelay)+
                                                   'index ='+str(self.index))
                            self.curentsec+=1



            else:
                self.index = 0
                self.milsec2=0
