from pynput import keyboard, mouse
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
        self.millsec = 0
        self.index=0

    def startHook(self):
        with keyboard.Listener(on_press=self.on_key_press, on_release=self.on_key_relaese) as self.keylis:
            with mouse.Listener(on_click=self.on_click) as self.mouse_listener:
                self.mouse_listener.join()

    def on_click(self, x, y, button, pressed):
        if self.recording:
            if pressed:
                if self.up:
                    self.up = False
                    pnt = [int(x), int(y)]
                    self.addToRecord(1,pnt,'')
                    self.millsec = 0

            else:
                self.up = True

    def kill(self):
        self.mouse_listener.stop()
        self.keylis.stop()

    def timeCounter(self):
        if self.programOn == False:
            return
        if self.recording:
            self.millsec +=1
        else:
            self.millsec = 0

    def on_key_press(self, key_code):
        """
        determins what keys do and records them
        """
        key_code = self.formatKeyIn(key_code)

        if self.programOn == False:
            return

        if self.recording:
            self.recordKey(key_code)
        self.hotkeys(key_code)

    def on_key_relaese(self, key_code):
        if self.programOn ==False:
            return
        """
        determins what keys do and records them
        """
        key_code = self.formatKeyIn(key_code)
        self.hotkeyrel(key_code)

    def hotkeys(self,key):
        return

    def hotkeyrel(self,key):
        return

    def showInfo(self,action):
        return

    def recordKey(self,key_code):
        self.addToRecord(5, '', key_code)



    def addToRecord(self,action,pnt,key):
        milSec = self.millsec
        lis = list()
        lis = [action, milSec, pnt, key]
        self.array.append(lis)
        if pnt is not None:
            pnt=str(pnt)
        else:
            pnt= str("")
        # self.addRecTtem(self.index,lis)
        self.index+=1
        self.showInfo(lis)

    def formatKeyIn(self,key_code):
        try:
            key_code='{0}'.format(key_code.char)
        except AttributeError:
            key_code = '{0}'.format(key_code)
        key = str(key_code).replace('Key.', '')
        return key

if __name__ == '__main__':
    rec = recorder()
    rec.recording=True
    rec.startHook()