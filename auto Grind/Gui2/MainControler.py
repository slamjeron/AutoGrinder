from tkinter import Toplevel
from Gui2.editPage import editPage as ed
class playControls():
    def __init__(self):
        self.recordList=list()
        self.main=None
        self.recordList.append([1,[500,444],''])
        self.recordList.append([3, [500, 444], 'k'])
        self.recordList.append([3, [500, 444], 'e'])
        self.recordList.append([1, [100, 444], ''])
        self.recordList.append([1, [500, 395], ''])
    def formatItem(self,index,list):
        l=list[0]
        if l==0:
            act='None'
        if l==1:
            act='Left Click'
        if l==2:
            act='Right Click'
        if l==3:
            act='Type'
        if l==4:
            act='Pixel Pause'
        if l==5:
            act='Pixel'
        return str(index)+'| action='+act+'| Point '+str(list[1])+'|Key Press='+list[2]

    def showList(self):
        self.taskBox.delete(0,'end')
        lineNum=0
        for line in self.recordList:
            self.taskBox.insert(lineNum,self.formatItem(lineNum,line))
            lineNum+=1


    def play(self):
        pltext=self.getStartBTNText()
        if pltext=='Pause':
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

    def setStartBTNText(self,text):
        return

    def getStartBTNText(self):
        return
    def editselect(self,selected):
        # open the editing page
        print('editing selected')
        selectedIndex=list()
        for index in selected:
            var=int(str(index).split('|')[0])
            selectedIndex.append(var)
            print(var)
        self.newWindow = Toplevel(self.main)
        self.edit = ed(self.newWindow)
        self.edit.pack()
        return
