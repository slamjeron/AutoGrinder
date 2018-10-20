from tkinter import Toplevel
from editPage import editPage as ed


class playControls():
    def __init__(self):
        self.recordList = list()
        self.main = None
        self.recordList.append([0, 1000, [500, 444], ''])
        self.recordList.append([4, 1000, [500, 444], 'k'])
        self.recordList.append([4, 1000, [500, 444], 'e'])
        self.recordList.append([0, 1000, [100, 444], ''])
        self.recordList.append([0, 32123, [500, 395], ''])

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
