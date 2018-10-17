import pyautogui
class HotKeys():
    def __init__(self):
        self.presedKey = ''
        self.heldKey=''
        self.playHoldingKey = "ctrl_l"
        self.playKey = "p"
        self.stopHoldingKey = ""
        self.stopKey = "q"
        self.pauseHoldingKey = "ctrl_l"
        self.pauseKey = "w"
        self.recHoldingKey = "ctrl_l"
        self.recKey = "r"
        self.mouse= pyautogui

    def play(self):
        return

    def stop(self):
        return

    def pause(self):
        return

    def record(self):
        return

    def playHotKeys(self,presedKey,heldKey):

        if self.hotKeysSet(presedKey,heldKey,self.playKey,self.playHoldingKey):
            print('playing')
            self.play()

    def stopHotKeys(self, presedKey, heldKey):
        if self.hotKeysSet(presedKey, heldKey, self.stopKey,  self.stopHoldingKey):
            print('stoping')
            self.stop()

    def pauseHotKeys(self, presedKey, heldKey):
        if self.hotKeysSet(presedKey, heldKey, self.pauseKey,  self.pauseHoldingKey):
            print('pausing')
            self.pause()

    def recordHotKeys(self, presedKey, heldKey):
        if self.hotKeysSet(presedKey, heldKey, self.recKey,  self.recHoldingKey):
            print('recording')
            self.record()

    def hotKeysSet(self,presedKey,heldKey,hPresed,hHeld):

        if hHeld=="":
            if heldKey==hPresed:
                return True
        else:
            if hPresed==presedKey and hHeld==heldKey:
                return True



    def hotkeys(self, key):
        if self.heldKey is not '':
            self.presedKey=key

        else:
            self.heldKey=key



        self.playHotKeys(self.presedKey,self.heldKey)
        self.stopHotKeys(self.presedKey,self.heldKey)
        self.pauseHotKeys(self.presedKey, self.heldKey)
        self.recordHotKeys(self.presedKey, self.heldKey)
        return


    def hotkeyrel(self, key):
        self.heldKey=''
        self.presedKey=''
        return