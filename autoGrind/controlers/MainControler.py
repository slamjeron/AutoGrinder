from tkinter import Toplevel
from editPage import editPage as ed
from autoGrind.baseMacro.globalHook import myHook
from autoGrind.baseMacro.hotkeys import HotKeys
from autoGrind.baseMacro.recordingAction import recorder
from autoGrind.baseMacro.playRec import RecPlayer


class playControls():
    def __init__(self):
        self.recordList = list()
        self.main = None
        rec=recorder()
        rec.array=self.recordList

        self.editkey = rec.on_key_press
        self.hook=myHook()
        self.hook.on_click = rec.on_click
        self.hook.on_key_press=self.keyPress
        self.hook.on_key_relaese=self.keyRelease
        hotkey=HotKeys()
        player=RecPlayer()
        player.recording=self.recordList
        def startrec():
            if not player.playing:
                rec.startRecording()
        def playrec():
            if not rec.recording:
                print('playing')
                player.play()

        def stop():
            print('stoping')
            print(rec.recording)
            rec.stop()
            player.stop()
        hotkey.playhotkeys.playmethod = playrec
        hotkey.rechotkeys.playmethod=startrec
        hotkey.stophotkeys.playmethod=stop
        self.hotkeyPress=hotkey.hotkeys
        self.hotkeyRelease=hotkey.hotkeyrel
        rec.showRecordedItem=self.showline
        self.rec=rec
        self.curline=0

    def showline(self,line):
        self.taskBox.insert(self.curline, self.formatItem(self.curline, line))
        self.curline+=1
    def close(self):
        self.hook.mouse_listener.stop()
        self.rec.kill()

    def keyPress(self,key):
        nkey=self.formatKeyIn(key)
        self.recPress(nkey)
        self.hotkeyPress(nkey)
        self.editkey(nkey)
    def formatKeyIn(self,key_code):
        try:
            key_code='{0}'.format(key_code.char)
        except AttributeError:
            key_code = '{0}'.format(key_code)
        key = str(key_code).replace('Key.', '')
        return key
    def recPress(self,key):
        return

    def editkey(self,key):
        return

    def hotkeyPress(self,key):
        return

    def keyRelease(self, key):
        nkey = self.formatKeyIn(key)
        self.recRelease(nkey)
        self.hotkeyRelease(nkey)

    def recRelease(self, key):


        return

    def hotkeyRelease(self, key):
        return
    def formatItem(self, index, list):
        l = list[0]
        actions = ['Left Click', 'Right Click', 'Drag Start',
                   'Drag Stop', 'Type', 'Color Stall', 'Color Condition', 'name groop']
        act = actions[int(l)]


        return str(index) + '| action =' + act + '| time delay = ' + str(list[1]) + '| Point = ' + str(
            list[2]) + '|Key Press = ' + list[3]

    def showList(self):
        self.taskBox.delete(0, 'end')
        lineNum = 0
        for line in self.recordList:
            self.taskBox.insert(lineNum, self.formatItem(lineNum, line))
            lineNum += 1

    def play(self):
        pltext = self.getStartBTNText()
        if pltext == 'Pause':
            self.setStartBTNText('Play')
        else:
            self.setStartBTNText('Pause')
        return

    def stop(self):
        print('stopping')
        return

    def delete(self):
        print('deleating')
        return

    def record(self):
        print('recording')
        return

    def setStartBTNText(self, text):
        return

    def getStartBTNText(self):
        return

    def editselect(self, selected):
        # open the editing page
        print('editing selected')
        selectedIndex = list()
        for index in selected:
            var = int(str(index).split('|')[0])
            selectedIndex.append(var)
            print(var)
        self.newWindow = Toplevel(self.main)
        self.edit = ed(self.newWindow)
        self.edit.editcon.recording = self.recordList
        self.edit.editcon.linesToEdit = selectedIndex
        self.edit.editcon.showEditLines()
        self.edit.editcon.update = self.showList
        self.edit.pack()
        return
