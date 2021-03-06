from tkinter import Toplevel

import pyautogui

from Gui2.editPage import editPage as ed
from baseMacro.globalHook import myHook
from baseMacro.hotkeys import HotKeys
from baseMacro.recordingAction import recorder
from baseMacro.playRec import RecPlayer

import copy

from controlers.pageBluePrint import mainPagebuttonBluePrint
from dataTypes.dataTypes import NamedEvents, Mouse, typerReader


class playControls(mainPagebuttonBluePrint):

    def displayCurentInfo(self, text):
        self.recInfo.set(text)
        return

    def getRecording(self):
        return self.recordList


    def setRecording(self, list):
        self.recordList=list

    def __init__(self):
        self.recordList = list()
        self.recentFiles = list()
        self.copyedAction= list()
        self.main = None
        rec=recorder()
        self.recInfo=None
        rec.getRecording=self.getRecording
        rec.setRecording=self.setRecording
        rec.showLine=self.showLine
        rec.displayCurentInfo=self.displayCurentInfo
        #named events with the same name will
        named=NamedEvents()
        def getNamedEvents():
            return named
        def setNamed(namedEvents):
            named=namedEvents


        self.myMenue = object()
        self.editkey = rec.on_key_press
        self.hook=myHook()
        self.hook.on_click = rec.on_click
        self.hook.on_key_press=self.keyPress
        self.hook.on_key_relaese=self.keyRelease
        hotkey=HotKeys()
        self.checkLoopStatus=None
        player=RecPlayer()
        player.getRecording=self.getRecording
        player.displayCurentInfo=self.displayCurentInfo
        def delete():
            select= list(self.getSelection())
            if len(select)>0:
                select.sort(key=int,reverse=True)
                for item in select:
                    del self.recordList[(item)]
                    self.curline-=1
                self.showAll()

        self.delete=delete

        def startrec():
            print(not rec.isRecording and not player.isplaying)
            rec.record((not rec.isRecording and  not player.isplaying))

        def playrec():
            print('should play')
            player.looping,player.loopAmount=self.checkLoopStatus()
            player.play(not rec.isRecording and not player.isplaying)

        def stop():
            rec.stopRecording()
            player.stop()

        self.stop=stop
        hotkey.playhotkeys.playmethod = playrec
        hotkey.rechotkeys.playmethod=startrec
        hotkey.stophotkeys.playmethod=stop
        self.pause=player.mpause
        hotkey.pausehotkeys.playmethod = self.pause
        self.hotkeyPress=hotkey.hotkeys
        self.hotkeyRelease=hotkey.hotkeyrel
        self.record=startrec
        self.play=playrec
        self.rec=rec
        self.curline=0
        self.player=player

    def showLine(self,line):
        self.taskBox.insert(self.curline,str(self.curline)+' |'+line)
        self.curline+=1

    def close(self):
        self.hook.mouse_listener.stop()
        self.hook.close()
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
        key = str(key).replace('_r', '')
        key = str(key).replace('_l', '')
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
        if 5==int(l):
            if list[4]:
                checstr='repeat till equal'
            else:
                checstr='repeat till not equal'
            return str(index) + '| act =' + act + '| delay = ' + str(list[1]) + '| pnt = ' + str(
                list[2]) + '|color = ' + str(list[3])+"| "+checstr

        if 4 == int(l):
            return str(index) + '| act =' + act + '| delay = ' + str(list[1]) + '|Key = ' + str(list[3])

        if 0 == int(l):
            return str(index) + '| act =' + act + '| delay = ' + str(list[1]) + '| pnt = ' + str(
                list[2])

    def showAll(self):
        self.taskBox.delete(0, 'end')
        lineNum = 0
        for line in self.recordList:
            self.taskBox.insert(lineNum, str(lineNum)+' |'+ str(line))
            lineNum += 1
        self.curline=lineNum

    def play(self):
        pltext = self.getStartBTNText()
        if pltext == 'Pause':
            self.setStartBTNText('Play')
        else:
            self.setStartBTNText('Pause')
        return


    def setStartBTNText(self, text):
        return

    def getStartBTNText(self):
        return

    def editselect(self, selected):
        # open the editing page
        print('editing selected')
        selectedIndex = selected

        self.newWindow = Toplevel(self.main)
        self.edit = ed(self.newWindow)
        editcon=self.edit.editcon
        editcon.linesToEdit=selectedIndex
        editcon.showEditLines()
        editcon.showAll=self.showAll
        editcon.getRecording=self.getRecording
        editcon.setRecording=self.setRecording
        self.edit.pack()
        return

    def copyselected(self):
        selected= self.getSelection()
        print(selected)
        self.copyedAction=list()
        for index in selected:
            self.copyedAction.append(copy.deepcopy(self.recordList[index]))

    def paste(self):
        index=self.getSelection()
        index=list(index)
        cpIndex=0
        if index[-1]>len(self.recordList):
            for item in self.copyedAction:
                self.recordList.append(item)
        else:
            for item in self.copyedAction:
                print(item)
                self.recordList.insert(index[-1]+1+cpIndex,item)
                cpIndex+=1
        self.showAll()

    def replace(self):
        ## not realy working
        index=self.getSelection()
        index=list(index)
        cpIndex=0

        for item in index:
            del self.recordList[item]
        if index[-1] > len(self.recordList):
            for item in self.copyedAction:
                self.recordList.append(item)
        else:
            for item in self.copyedAction:
                print(item)
                self.recordList.insert(index[-1]+cpIndex,item)
                cpIndex+=1
        self.showAll()

    def insert(self,index):
        if len(index)>0:
            index=list(index)
            index=[int(index[-1])]
            self.recordList.insert(index[0],Mouse(0.5,Mouse.move,[1,1]))
            self.showAll()
            self.editselect(index)


    def cursorPosition(self):
        index = self.getSelection()
        if index is not None:
            index = list(index)
            index = int(index[-1])
            print(index)
            if self.recordList[index].object==Mouse.object:
                m= self.recordList[index]
                print(m.position)
                pyautogui.moveTo(*m.position)
