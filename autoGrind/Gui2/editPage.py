import tkinter

from autoGrind.Gui2.myent import myEnt
from autoGrind.controlers.editPageCon import editCon


class editPage(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.editcon=editCon()
        lbl=tkinter.Label(self,text='editing lines')
        lbl.grid(row=0,column=0)
        editlines = tkinter.Entry(self)
        editlines.grid(row=0, column=1, columnspan=3)
        editlines.config(width=40)

        def enterlines(text=''):
            editlines.delete(0,'end')
            editlines.insert(0,text)

        self.editcon.enterlines = enterlines
        lbl1 = tkinter.Label(self, text='action')
        lbl1.grid(row=1, column=0)
        self.recVar=tkinter.StringVar()

        actionDrop=tkinter.OptionMenu(self, self.recVar, 'Same', 'Left Click', 'Right Click', 'Drag Start',
                           'Drag Stop', 'Type', 'Color Stall', 'Color Condition','name groop')


        actionDrop.grid(row=1, column=1)
        actionDrop.config(width=10)
        keyMouseFrame = tkinter.Frame(self)
        keyMouseFrame.grid(row=1, column=2)
        self.recVar.set('Same')
        lbl2 = tkinter.Label(keyMouseFrame, text='time delay')
        lbl2.grid(row=0, column=0)
        delayEnt= myEnt(keyMouseFrame, 'Same')
        delayEnt.grid(row=0,column=1)
        delayEnt.config(width=7)
        pntFrame=tkinter.Frame(keyMouseFrame)
        pntFrame.grid(row=0,column=2,rowspan=2)
        lbl3 = tkinter.Label(pntFrame, text='Point X')
        lbl3.grid(row=0, column=0)
        pointXEnt = myEnt(pntFrame, 'Same')
        pointXEnt.grid(row=0, column=1)
        pointXEnt.config(width=6)
        lbl3 = tkinter.Label(pntFrame, text='Point y')
        lbl3.grid(row=0, column=2)

        pointYEnt = myEnt(pntFrame, 'Same')


        pointYEnt.grid(row=0, column=3)
        pointYEnt.config(width=6)



        def setYpoint(ypoint):
            pointYEnt.delete(0,'end')
            pointYEnt.insert(0,ypoint)
        def setXpoint(xpoint):
            pointXEnt.delete(0,'end')
            pointXEnt.insert(0,xpoint)

        def getPoint():
            self.editcon.getPoint(setXpoint,setYpoint)

        getpointbtn = tkinter.Button(pntFrame, text='   get point   ',command=getPoint)
        getpointbtn.grid(row=1, column=0,rowspan=4,columnspan=2)
        keyframe=tkinter.Frame(keyMouseFrame)
        keyframe.grid(row=0,column=4,rowspan=2)
        lbl4 = tkinter.Label(keyframe, text='key event')
        lbl4.grid(row=0, column=0)

        keyEnt = myEnt(keyframe)
        keyEnt.insert(0,'Same')
        keyEnt.grid(row=0, column=1)
        keyEnt.config(width=7)

        getkeyStrockbtn = tkinter.Button(keyframe, text='get key stroke')
        getkeyStrockbtn.grid(row=1, column=0,rowspan=5,columnspan=3)

        botomFrame = tkinter.Frame(self)
        botomFrame.grid(row=5, column=0,sticky='we', columnspan=8)
        botomFrame.grid_columnconfigure(2, weight=1)
        botonCenter=tkinter.Frame(botomFrame)
        botonCenter.pack()
        savebtn = tkinter.Button(botonCenter, text='Save',command=lambda :self.editcon.saveComand(self.recVar.get(),delayEnt.get(),[pointXEnt.get(),pointYEnt.get()],keyEnt.get(),editlines.get()))
        savebtn.pack(side=tkinter.LEFT)

        delbtn = tkinter.Button(botonCenter, text='Delete',command=self.editcon.delete_act)
        delbtn.pack(side=tkinter.LEFT)

        self.editcon.close=self.onclose

        self.pack()
        self.parent = parent
        self.line = tkinter.StringVar()

        parent.protocol("WM_DELETE_WINDOW", self.onclose)
        self.pageUp = True

        def getlines(self):
            return editlines.get()
        editCon.getlines =getlines

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