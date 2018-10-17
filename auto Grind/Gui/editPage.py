import tkinter
class editPage(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        btn = tkinter.Button(self, text='btn')
        btn.grid(row=0, column=1)
        self.pack()
        self.parent = parent
        self.line = tkinter.StringVar()
        spiner = tkinter.Spinbox(self, from_=0, to=10000000, textvariable=self.line)
        spiner.config(width=4)
        spiner.grid(row=0, column=0)

        parent.protocol("WM_DELETE_WINDOW", self.onclose)
        self.pageUp = True

    def setInfo(self,line,mlist):
        self.line.set(str(line))
        return

    def onclose(self):
        self.pageUp = False
        print('closing')
        self.parent.destroy()
        self.pageClosed()
        return

    def pageClosed(self):
        return
