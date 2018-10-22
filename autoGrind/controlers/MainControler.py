from tkinter import Toplevel,filedialog
from autoGrind.Gui2.editPage import editPage as ed
from autoGrind.baseMacro.globalHook import myHook
from autoGrind.baseMacro.hotkeys import HotKeys
from autoGrind.baseMacro.recordingAction import recorder
from autoGrind.baseMacro.playRec import RecPlayer
import pickle
from  os.path import exists
class openSave(object):
    def __init__(self):
        object.__init__(self)
        self.diolog=filedialog
    def save_record(self, userInfo,programInfo, fileName=None):
        """
        saves the record
        """
        print(fileName)
        if fileName==None:
            fileName=self.diolog.asksaveasfilename(filetypes =(("auto grinder file", "*.grind"),("All Files","*.grind")))
        mfile = open(fileName, 'wb')

        pickle.dump(userInfo, mfile)
        ufile=open('proFile.grind','wb')
        pickle.dump(programInfo,ufile)
        return fileName
        mfile.close()

    def openPro(self):
        info=list()
        if exists('./proFile.grind'):
            mfile = open('proFile.grind', 'rb')
            info = pickle.load(mfile)
        return info

    def openRecord(self,fileName=None):
        if fileName ==None:
            fileName = self.diolog.askopenfilename(filetypes =(("auto grinder file", "*.grind"),("All Files","*.grind")))
        mfile = open(fileName, 'rb')
        info = pickle.load(mfile)
        mfile.close()
        return info

class playControls():

    def __init__(self):
        self.recordList = list()
        self.recentFiles = list()

        self.main = None
        rec=recorder()

        rec.array=self.recordList

        self.myMenue = object()
        self.editkey = rec.on_key_press
        self.hook=myHook()
        self.hook.on_click = rec.on_click
        self.hook.on_key_press=self.keyPress
        self.hook.on_key_relaese=self.keyRelease
        hotkey=HotKeys()
        self.checkLoopStatus=None
        player=RecPlayer()
        player.recording=self.recordList
        def delete():
            self.recordList.clear()
            self.showList()
        self.delete=delete

        def startrec():
            if not rec.recording and not player.playing:
                rec.startRecording()
        def playrec():
            if not rec.recording and not player.playing:
                print('playing')
                player.looping,player.loopAmount=self.checkLoopStatus()
                player.play()

        def stop():
            rec.stop()
            player.stop()
        self.stop=stop
        hotkey.playhotkeys.playmethod = playrec
        hotkey.rechotkeys.playmethod=startrec
        hotkey.stophotkeys.playmethod=stop
        self.hotkeyPress=hotkey.hotkeys
        self.hotkeyRelease=hotkey.hotkeyrel
        rec.showRecordedItem=self.showline
        self.record=startrec
        self.play=playrec
        self.rec=rec
        self.curline=0
        self.player=player
    def setMenue(self):
        opsave = openSave()
        self.filename = ''


        def onSave():
            if self.filename is not '':
                profiles=[self.recentFiles]
                userFiles=[self.recordList]
                opsave.save_record(userFiles,profiles, self.filename)
            else:
                self.filename =opsave.save_record(self.recordList,None)

            if self.filename in self.recentFiles:
                pass
            else:
                self.recentFiles.append(self.filename)
                self.myMenue.addResentFile(self.filename,lambda :openSave.openRecord(self.filename))
            print('Saving code')

        def onSaveAs():
            print('Saving as')
            if self.filename in self.recentFiles:
                pass
            else:
                self.recentFiles.append(self.filename)
                self.myMenue.addResentFile(self.filename, lambda: openSave.openRecord(self.filename))
            self.filename = opsave.save_record(self.recordList)

        def onOpen():
            print('opening dialogue')
            self.recordList=opsave.openRecord()
            self.showList()

        def onEditingPage(self):
            print('showing Editing Page')

        def onHotKeyPage(self):
            print('showing Editing Page')

        def onRecordSettings(self):
            print('showing rec settings editor')


        self.myMenue.onSave = onSave
        self.recentFiles = opsave.openPro()
        for files in self.recentFiles:
            self.myMenue.addResentFile(files, lambda: opsave.openRecord(files))
        self.myMenue.onSaveAs = onSaveAs
        self.myMenue.onOpen=onOpen

    def showline(self,line):
        self.taskBox.insert(self.curline, self.formatItem(self.curline, line))
        self.curline+=1
    def close(self):
        self.hook.mouse_listener.stop()
        self.player.kill()
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
