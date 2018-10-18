import tkinter
from scrole.vScroll import VerticalScrolledFrame
from Gui2.MainControler import playControls


# menu bar

class mainPage(tkinter.Tk):
    def __init__(self, playcon):
        tkinter.Tk.__init__(self)
        self.recordingBox = tkinter.Listbox(self)
        self.addTopButtons(playcon)
        self.config(height=200, width=400)
        self.pack_propagate(0)

        self.recordingBox.config(selectmode=tkinter.EXTENDED)

        scrollbar = tkinter.Scrollbar(self.recordingBox, orient="vertical")
        self.recordingBox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.recordingBox.yview)
        scrollbar.pack(side="right", fill="y")
        self.recordingBox.pack(expand=1, fill=tkinter.BOTH)

        for i in range(2):
            self.recordingBox.insert(i,str(i))

        bottomControls = tkinter.Frame(self)
        bottomControls.pack()
        bottomControlsIner = tkinter.Frame(bottomControls)
        bottomControlsIner.pack()
        prevPage = tkinter.Button(bottomControlsIner, text='Previous')
        prevPage.grid(row=2, column=0)
        prevPage = tkinter.Button(bottomControlsIner, text='show Info')
        prevPage.grid(row=2, column=1)
        nextPage = tkinter.Button(bottomControlsIner, text='next')
        nextPage.grid(row=2, column=2)
        self.bottomPage()
        self.title('Auto Grinder')
        self.plBtnTxt = tkinter.StringVar()

        self.mainloop()
    def ctrlcomand(self,key):
        print(key)
        self.recordingBox.config(selectmode = tkinter.MULTIPLE)

    def addTopButtons(self, playCon):
        btnPane = tkinter.Frame(self)
        btnPane.pack()
        recordBtn = tkinter.Button(btnPane, text='record', command=playCon.record)
        recordBtn.grid(row=0, column=0)
        self.plBtnTxt=tkinter.StringVar()
        self.startBtn = tkinter.Button(btnPane, textvariable=self.plBtnTxt, command=playCon.play)
        self.plBtnTxt.set('Play')
        self.startBtn.grid(row=0, column=2)
        pauseBtn = tkinter.Button(btnPane, text='pause', command=playCon.pause)
        pauseBtn.grid(row=0, column=3)
        stopBtn = tkinter.Button(btnPane, text='stop', command=playCon.stop)
        stopBtn.grid(row=0, column=1)
        delBtn = tkinter.Button(btnPane, text='delete', command=playCon.delete)
        delBtn.grid(row=0, column=4)
        delBtn = tkinter.Button(btnPane, text='edit selected',command=lambda : playcon.editselect([self.recordingBox.get(idx) for idx in self.recordingBox.curselection()]))
        delBtn.grid(row=0, column=5)

    def bottomPage(self):
        bottomframe = tkinter.Frame(self)
        bottomframe.pack()
        self.recInfo = tkinter.StringVar()
        label = tkinter.Label(bottomframe, textvariable=self.recInfo)
        self.recInfo.set('action')
        label.pack()


    def editPageClosed(self):
        self.editing = False




if __name__ == '__main__':
    playcon=playControls()
    main = mainPage(playcon)
    main.mainloop()
