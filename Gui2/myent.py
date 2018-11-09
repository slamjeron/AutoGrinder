import tkinter

class LblEnt(tkinter.Frame):
    def __init__(self,parent,text='',boxtype='ent',position='top'):
        tkinter.Frame.__init__(self,parent)

        self.lab=tkinter.Label(self,text=text)
        if boxtype=='ent':
            self.ent =tkinter.Entry(self)
        elif boxtype=='spin':
            self.ent=tkinter.Spinbox(self, from_=1, to=100000)
        if position=='top':
            self.lab.grid(row=0,column=0)
            self.ent.grid(row=1,column=0)
class myEnt(tkinter.Entry):
    def __init__(self,parent,text=''):
        tkinter.Entry.__init__(self,parent)
        self.text=text
        self.insert(0, text)
        self.bind('<FocusIn>', self.emptytext)
        self.bind('<FocusOut>', self.lostFocus)
        return

    def emptytext(self,event):
        if self.get()==self.text:
            self.delete(0, 'end')

    def lostFocus(self,event):
        try:
            float(self.get())
        except ValueError:
            self.delete(0, 'end')
            self.insert(0, self.text)