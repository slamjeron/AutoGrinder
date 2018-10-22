
from pyautogui import *
from threading import Thread
import time
""" 
use key comands to control actions
"""


class RecPlayer():
    def __init__(self):
        self.index = 0
        self.milsec2 = 0
        self.recording = list()
        self.playing = False
        self.pause = False
        self.end=False
        self.secondes = time.time()
        myThread=Thread(target=self.player)
        myThread.start()
        self.looping=False
        self.loopAmount=1
        self.loops = 0

    def play(self):
        self.playing = True
        self.pause = False
        self.secondes = time.time()
        if self.looping:
            if self.loopAmount=="loop":
                self.loopAmount=-1
            else:
                self.loopAmount=float(self.loopAmount)
        else:
            self.loopAmount=1
        self.loops = 0

    def kill(self):
        self.end=True

    def stop(self):
        self.playing=False
        return

    def recoreder(self):
        return


    def player(self):
        rec = self.recording

        while self.end is False:
            time.sleep(0.001)
            if self.playing:
                if self.pause is False:

                    if len(rec) <= 1:
                        self.playing = False

                    try:
                        sec=time.time() - self.secondes
                        sec =round(sec,2)
                        if sec >= rec[self.index][1]:

                            if rec[self.index][0] == 0:
                                click(rec[self.index][2][0], rec[self.index][2][1])
                                self.index += 1
                            if rec[self.index][0] == 4:
                                press(rec[self.index][3])
                                self.index += 1
                            self.secondes = time.time()
                    except:
                        if self.loopAmount==-1:
                            self.index=0
                        elif self.loops<self.loopAmount:
                            self.loops+=1
                            self.index=0
                        else:
                            self.playing = False
                            self.loops=0



                    if self.index > len(rec) - 1:
                        self.playing = False
            else:
                self.index = 0
                self.milsec2=0
