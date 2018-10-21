
from pyautogui import *
from threading import Thread

""" 
use key comands to control actions
"""


class RecPlayer():
    def __init__(self):
        self.index = 0
        self.milsec = 0
        self.recording = list()
        self.playing = False
        self.pause = False
        self.end=False
        myThread=Thread(target=self.player)
        myThread.start()
        myThread1 = Thread(target=self.playcount)
        myThread1.start()

    def play(self):
        self.playing = True
        self.pause = False

    def kill(self):
        self.end=True

    def stop(self):
        self.playing=False
        return
    def playcount(self):
        while self.end is False:
            if self.playing:
                if self.pause is False:
                    self.milsec += 1

    def player(self):
        rec = self.recording
        while self.end is False:

            if self.playing:
                if self.pause is False:

                    if len(rec) <= 1:
                        self.playing = False
                    try:
                        if self.milsec >= rec[self.index][1]*1000:

                            if rec[self.index][0] == 0:
                                print(self.index)
                                click(rec[self.index][2][0], rec[self.index][2][1])
                                self.index += 1
                            if rec[self.index][0] == 4:
                                print(self.index)
                                press(rec[self.index][3])
                                self.index += 1
                    except:
                        self.playing = False


                    if self.index > len(rec) - 1:
                        self.playing = False

            else:
                self.index = 0
                self.milsec = 0
