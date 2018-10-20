import tkinter
class editPage(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        lbl=tkinter.Label(self,text='editing lines')
        lbl.grid(row=0,column=0)
        lbl1 = tkinter.Label(self, text='action')
        lbl1.grid(row=1, column=0)
        self.recVar=tkinter.StringVar()
        actionDrop=tkinter.OptionMenu(self, self.recVar, 'Same', 'Left Click', 'Right Click', 'Drag Start',
                           'Drag Stop', 'Type', 'Color Stall', 'Color Condition')
        actionDrop.grid(row=1, column=1)
        actionDrop.config(width=10)
        self.recVar.set('Same')
        lbl2 = tkinter.Label(self, text='time delay')
        lbl2.grid(row=1, column=2)
        delayEnt=tkinter.Entry(self)
        delayEnt.grid(row=1,column=3)
        delayEnt.insert(0,'Same')
        delayEnt.config(width=7)
        lbl3 = tkinter.Label(self, text='Point X')
        lbl3.grid(row=1, column=4)
        pointXEnt = tkinter.Entry(self)
        pointXEnt.grid(row=1, column=5)
        pointXEnt.insert(0,'Same')
        pointXEnt.config(width=6)
        lbl3 = tkinter.Label(self, text='Point y')
        lbl3.grid(row=1, column=6)
        pointYEnt = tkinter.Entry(self)
        pointYEnt.grid(row=1, column=7)
        pointYEnt.insert(0, 'Same')
        pointYEnt.config(width=6)
        lbl4 = tkinter.Label(self, text='key event')
        lbl4.grid(row=1, column=8)

        keyEnt = tkinter.Entry(self)
        keyEnt.grid(row=1, column=9)
        keyEnt.insert(0, 'Same')
        keyEnt.config(width=7)



        editlines = tkinter.Entry(self)
        editlines.grid(row=0, column=1, columnspan=3)
        savebtn = tkinter.Button(self, text='Save')
        savebtn.grid(row=2, column=2)

        delbtn = tkinter.Button(self, text='Delete')
        delbtn.grid(row=2, column=3)

        cursorbtn = tkinter.Button(self, text='get Cursor')
        cursorbtn.grid(row=2, column=0)
        getkeyStrockbtn = tkinter.Button(self, text='get key stroke')
        getkeyStrockbtn.grid(row=2, column=0)
        getkeyStrockbtn = tkinter.Button(self, text='get point')
        getkeyStrockbtn.grid(row=2, column=1)
        self.pack()
        self.parent = parent
        self.line = tkinter.StringVar()

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
if __name__ == '__main__':
    playcon = tkinter.Tk()
    edit = editPage(playcon)
    edit.mainloop()