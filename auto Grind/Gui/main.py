import tkinter
from tkinter import messagebox
from scrole.vScroll import VerticalScrolledFrame
from Gui.menue import MyMenu
from Gui.editPage import editPage


# menu bar

class mainPage():
    def __init__(self):
        self.main = tkinter.Tk()
        self.controls = recPlayControls()
        self.myMenu = MyMenu(self.main)
        self.plBtnTxt = tkinter.StringVar()
        self.records = list()
        self.recIndex = 0
        self.linePerPage = 20
        self.pageNum = 0
        self.edit = editPage
        self.editing = False


    def onClosing(self):

        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.closeHook()
            self.main.destroy()
        return

    def closeHook(self):
        return

    def showInfo(self):
        stnum = self.pageNum * self.linePerPage
        for i in range(self.linePerPage):
            cnum = i + stnum
            self.lines[i].setActionNum(cnum)
            if (cnum < len(self.records)):
                self.lines[i].setText(self.formatList(self.records[cnum]))
                self.lines[i].setAction(self.actions[self.records[cnum][0]])
            else:
                self.lines[i].setText('')

    def priviusPage(self):
        if self.pageNum >= 1:
            self.pageNum -= 1

        stnum = self.pageNum * self.linePerPage
        for i in range(self.linePerPage):
            cnum = i + stnum
            self.lines[i].setActionNum(cnum)
            if (cnum < len(self.records)):
                self.lines[i].setText(self.formatList(self.records[cnum]))
                self.lines[i].setAction(self.actions[self.records[cnum][0]])
            else:
                self.lines[i].setText('')

    def nextPage(self):
        self.pageNum += 1
        stnum = self.pageNum * self.linePerPage

        for i in range(self.linePerPage):
            cnum = i + stnum
            self.lines[i].setActionNum(cnum)
            if (cnum < len(self.records)):
                self.lines[i].setText(self.formatList(self.records[cnum]))
                self.lines[i].setAction(self.actions[self.records[cnum][0]])
            else:
                self.lines[i].setText('')

    def formatList(self, itemList=list()):
        return str('delay ' + str(itemList[1]) + '|| point ' + str(itemList[2]) + ' || key ' + str(itemList[3]))

    def editAll(self):
        #opens a page that alows the user to edit the times between each action
        return

    def start(self):
        self.addTopButtons()
        self.addRecordView()

        bottomControls = tkinter.Frame(self.main)
        bottomControls.pack()
        bottomControlsIner = tkinter.Frame(bottomControls)
        bottomControlsIner.pack()
        self.actions = ['None', 'Left Click', 'Right Click', 'Drag Start', 'Drag Stop',
                        'Type', 'Color Stall', 'Color Condition']
        prevPage = tkinter.Button(bottomControlsIner, text='Previous', command=self.priviusPage)
        prevPage.grid(row=2, column=0)
        prevPage = tkinter.Button(bottomControlsIner, text='show Info', command=self.showInfo)
        prevPage.grid(row=2, column=1)
        nextPage = tkinter.Button(bottomControlsIner, text='next', command=self.nextPage)
        nextPage.grid(row=2, column=2)
        self.bottomPage()
        self.myMenu.editAll=self.editAll
        self.main.protocol("WM_DELETE_WINDOW", self.onClosing)
        self.main.title('Auto Grinder')

        self.main.mainloop()

    def addTopButtons(self):
        self.myMenu.set()
        btnPane = tkinter.Frame(self.main)
        btnPane.pack()
        recordBtn = tkinter.Button(btnPane, text='record', command=self.controls.record)
        recordBtn.grid(row=0, column=0)
        self.startBtn = tkinter.Button(btnPane, textvariable=self.plBtnTxt, command=self.controls.play)
        self.plBtnTxt.set('Play')
        self.startBtn.grid(row=0, column=2)
        pauseBtn = tkinter.Button(btnPane, text='pause', command=self.controls.pause)
        pauseBtn.grid(row=0, column=3)
        stopBtn = tkinter.Button(btnPane, text='stop', command=self.controls.stop)
        stopBtn.grid(row=0, column=1)
        delBtn = tkinter.Button(btnPane, text='delete', command=self.controls.delete)
        delBtn.grid(row=0, column=4)

    def bottomPage(self):
        bottomframe = tkinter.Frame(self.main)
        bottomframe.pack()
        self.recInfo = tkinter.StringVar()
        label = tkinter.Label(bottomframe, textvariable=self.recInfo)
        self.recInfo.set('action')
        label.pack()

    def displayAction(self, action):
        self.recInfo.set(self.formatList(action))

    def editfun(self, line):
        if self.editing == False:
            print('opening page')
            self.newWindow = tkinter.Toplevel(self.main)
            self.edit = editPage(self.newWindow)
            self.editing = True
            self.edit.pageClosed = self.editPageClosed
        lineLi = list()
        if line < len(self.records):
            lineLi = self.records[line]
        self.edit.setInfo(line, lineLi)

    def addRecordView(self):
        recordingPane = VerticalScrolledFrame(self.main)
        recordingPane.pack(expand=1, fill=tkinter.BOTH)
        recordingPane.configure(height=300)
        self.lines = list()
        for i in range(self.linePerPage):
            line = recLine(recordingPane.interior, i, self.editfun)
            line.grid(row=i, column=0)
            line.editSend = self.edit.setInfo

            self.lines.append(line)

    def editPageClosed(self):
        self.editing = False


class recLine(tkinter.Frame):
    def __init__(self, parent, num, edit):
        self.textvar = tkinter.StringVar()
        tkinter.Frame.__init__(self, parent, highlightbackground="black", highlightcolor="black", highlightthickness=1)

        self.config(width=500)
        ent = tkinter.Entry(self, textvariable=self.textvar)
        ent.grid(column=2, row=0)
        ent.config(width=40)
        self.recVar = tkinter.StringVar()
        self.recVar.set('None')  # set the default option
        self.label = tkinter.Label(self, text=str(num))
        self.linenm = num
        self.label.grid(column=0, row=0)
        self.edit = edit
        popupMenu = tkinter.OptionMenu(self, self.recVar, 'None', 'Left Click', 'Right Click', 'Drag Start',
                                       'Drag Stop', 'Type', 'Color Stall', 'Color Condition')
        popupMenu.config(width=12)
        popupMenu.grid(column=1, row=0)
        editBtn = tkinter.Button(self, text='edit', command=self.editSend)
        editBtn.grid(column=3, row=0)
        helpBtn = tkinter.Button(self, text='help')
        helpBtn.grid(column=4, row=0)

    def emptyLine(self):
        self.setAction('None')
        self.setText('')

    def setList(self, mList):
        self.list = mList

    def setAction(self, actStr=""):
        self.recVar.set(actStr)

    def editSend(self):
        self.edit(self.linenm)

    def setActionNum(self, text):
        self.linenm=text
        self.label.config(text=str(text))

    def setText(self, text):
        self.textvar.set(text)
        return


class recPlayControls():
    def record(self):
        print('recording')

    def play(self):
        print('playing')

    def pause(self):
        print('pausing')

    def stop(self):
        print('stoping')

    def delete(self):
        print('deleting')


def dele():
    print('changed delete')


def save():
    print('changed save')


if __name__ == '__main__':
    main = mainPage()
    main.start()
