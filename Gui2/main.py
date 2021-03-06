import tkinter
from tkinter import ttk
from PIL import Image
from controlers.MainControler import playControls
import threading
from Gui2.menue import MyMenu
from Gui2.myent import myEnt


# menu bar

class mainPage(tkinter.Tk):
    def __init__(self, playcon=playControls):
        tkinter.Tk.__init__(self)
        self.recordingBox = tkinter.Listbox(self)
        self.playcon = playcon
        playcon.taskBox = self.recordingBox
        playcon.main = self
        myMenue = MyMenu(self)
        myMenue.con.getRecording = self.playcon.getRecording
        myMenue.con.setRecording = self.playcon.setRecording
        myMenue.con.copy = self.playcon.copyselected
        myMenue.con.past = self.playcon.paste
        myMenue.con.showAll = self.playcon.showAll

        popup_menu = tkinter.Menu(self.recordingBox, tearoff=0)
        popup_menu.add_command(label='cursor to position', command=self.playcon.cursorPosition)
        popup_menu.add_command(label='edit selected',command= lambda: playcon.editselect(
            self.recordingBox.curselection()))
        popup_menu.add_command(label='Copy', command=self.playcon.copyselected)
        popup_menu.add_command(label='Paste', command=self.playcon.paste)

        popup_menu.add_command(label='Delete', command=self.playcon.delete)

        def popup(event):
            try:
                popup_menu.tk_popup(event.x_root, event.y_root + 20, 0)
            finally:
                popup_menu.grab_release()

        self.recordingBox.bind("<Button-3>", popup)
        self.addTopButtons()
        self.config(height=200, width=450)
        self.pack_propagate(0)
        self.recordingBox.config(selectmode=tkinter.EXTENDED)

        scrollbar = tkinter.Scrollbar(self.recordingBox, orient="vertical")
        self.recordingBox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.recordingBox.yview)
        scrollbar.pack(side="right", fill="y")
        self.recordingBox.pack(expand=1, fill=tkinter.BOTH)

        playcon.taskBox = self.recordingBox

        bottomControls = tkinter.Frame(self)
        bottomControls.pack()
        bottomControlsIner = tkinter.Frame(bottomControls)
        bottomControlsIner.pack()
        prevPage = ttk.Button(bottomControlsIner, text='show Info')
        prevPage.grid(row=2, column=1)

        self.bottomPage()
        self.title('AutoGrinder')

        def close():
            self.destroy()
            print('closing win')
            playcon.close()

        self.protocol("WM_DELETE_WINDOW", close)
        playcon.showAll()
        myMenue.con.onExit = close
        myMenue.set()

    def addTopButtons(self):
        test = "play"
        btnPane = tkinter.Frame(self)
        btnPane.pack()
        recordBtn = ttk.Button(btnPane, text='record', command=self.playcon.record)
        recordBtn.grid(row=0, column=0)

        def btnRecordKey(key):
            recordBtn['text'] = 'Record' + key

        btnRecordKey('(ctrl, R)')
        startBtn = ttk.Button(btnPane, text=test, command=self.playcon.play)
        startBtn.grid(row=0, column=2)

        def btnStartKey(key):
            startBtn['text'] = 'Play' + key

        btnStartKey('(F11)')

        def getStartBTNText():
            return startBtn['text']

        playcon = self.playcon
        playcon.btnStartKey = btnStartKey
        playcon.getStartBTNText = getStartBTNText
        var = tkinter.BooleanVar()
        loopCheck = ttk.Checkbutton(btnPane, variable=var)
        loopCheck.grid(row=1, column=3)
        var2 = tkinter.BooleanVar()

        keyControlMs = ttk.Checkbutton(btnPane, text='controll ', variable=var2)
        keyControlMs.grid(row=1, column=4)
        loopent = myEnt(btnPane, 'loop')
        loopent.grid(row=1, column=4)
        loopent.config(width=6)

        def checkLoopStatus():
            return var.get(), loopent.get()

        playcon.checkLoopStatus = checkLoopStatus
        playcon.getSelection = self.recordingBox.curselection
        stopBtn = ttk.Button(btnPane, text='stop', command=self.playcon.stop)
        stopBtn['text'] = 'Stop (F8)'

        pauseBtn = ttk.Button(btnPane, text='stop', command=self.playcon.pause)
        pauseBtn['text'] = 'Pause (F7)'

        def btnStopKey(key):
            stopBtn['text'] = 'Stop' + key

        btnStopKey(' (F8)')
        stopBtn.grid(row=0, column=1)
        delBtn = ttk.Button(btnPane, text='delete', command=self.playcon.delete)
        delBtn.grid(row=1, column=0)

        editBtn = ttk.Button(btnPane, text='edit selected', command=lambda: playcon.editselect(
            self.recordingBox.curselection()))
        editBtn.grid(row=1, column=1)

        insertBtn = ttk.Button(btnPane, text='insert', command=lambda: playcon.insert(self.recordingBox.curselection()))
        insertBtn.grid(row=1, column=2)

    def bottomPage(self):
        bottomframe = tkinter.Frame(self)
        bottomframe.pack()
        self.recInfo = tkinter.StringVar()
        label = ttk.Label(bottomframe, textvariable=self.recInfo)
        self.recInfo.set('action')
        self.playcon.recInfo = self.recInfo
        label.pack()


def start():
    playcon = playControls()
    main = mainPage(playcon)
    thread = threading.Thread(target=playcon.hook.startHook)
    thread.start()
    main.mainloop()


if __name__ == '__main__':
    start()
