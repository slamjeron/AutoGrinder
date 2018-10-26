
from pyautogui import *
from threading import Thread
from autoGrind.controlers.pageBluePrint import mainPagebuttonBluePrint
import time
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
        self.secondes = time.time()

        myThread=Thread(target=self.player)
        myThread.start()
        self.looping=False
        self.loopAmount=1
        self.loops = 0

    def play(self,redy):
        if redy:
            self.recording=self.getRecording()
            print(self.recording)
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
            self.recording[self.index][1]
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

                    if len(self.recording) <= 1:
                        self.isplaying = False
                    sec = time.time() - self.secondes
                    sec = round(sec, 2)


                    try:
                        sec=time.time() - self.secondes
                        sec =round(sec,2)
                        if sec >= self.recording[self.index][1]:
                            action=self.recording[self.index][0]
                            self.curentsec=0
                            if action == 0:
                                click(self.recording[self.index][2][0], self.recording[self.index][2][1])
                                self.index += 1

                            if action == 4:
                                press(self.recording[self.index][3])
                                self.index += 1

                            if action == 5:

                                if pixelMatchesColor(self.recording[self.index][2][0], self.recording[self.index][2][1],self.recording[self.index][3])==self.recording[self.index][4]:
                                    self.index+=1
                                else:
                                    pass




                            self.secondes = time.time()

                    except:
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
                            self.displayCurentInfo(str(sec)+'next action time='+str(self.recording[self.index][1]))
                            self.curentsec+=1



            else:
                self.index = 0
                self.milsec2=0
