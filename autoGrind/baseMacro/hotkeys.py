import pyautogui
class hotkeycon():
    def __init__(self,heldkey,presedKey):
        object.__init__(self)
        self.heldkey=heldkey
        self.presedKey=presedKey
    def playmethod(self):
        return
    def sethotKeyKeys(self,heldkey,presedKey):
        self.heldkey = heldkey
        self.presedKey = presedKey

    def keysPressed(self,curentPressed,curentHeld):

        if self.heldkey =='':
            if curentHeld== self.presedKey:
                print('hot key pressed')
                self.playmethod()
        else:
            if curentHeld==self.heldkey and curentPressed== self.presedKey:
                print('hot key pressed')
                self.playmethod()
class HotKeys():
    def __init__(self):
        self.presedKey = ''
        self.heldKey=''
        self.playhotkeys=hotkeycon("ctrl","p")
        self.stophotkeys = hotkeycon("", "q")
        self.pausehotkeys = hotkeycon("ctrl", "w")
        self.rechotkeys = hotkeycon("ctrl", "r")


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
        self.playhotkeys.keysPressed(self.presedKey,self.heldKey)
        self.stophotkeys.keysPressed(self.presedKey,self.heldKey)
        self.pausehotkeys.keysPressed(self.presedKey,self.heldKey)
        self.rechotkeys.keysPressed(self.presedKey,self.heldKey)
        return


    def hotkeyrel(self, key):
        self.heldKey=''
        self.presedKey=''
        return