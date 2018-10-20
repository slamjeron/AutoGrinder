
from pyautogui import *

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

    def play(self):
        self.playing = True
        self.pause = False

    def stoped(self):
        return

    def player(self):
        rec = self.recording

        if self.playing:
            if self.pause is False:
                if len(rec) <= 1:
                    self.playing = False
                try:
                    if self.milsec >= rec[self.index][1]+1:

                        if rec[self.index][0] == 0:
                            print(self.index)
                            click(rec[self.index][2][0], rec[self.index][2][1])
                            self.index += 1
                except:
                    self.playing = False

                self.milsec += 1
                if self.index > len(rec) - 1:
                    self.playing = False

                    self.stoped()
        else:
            self.index = 0
            self.milsec = 0
