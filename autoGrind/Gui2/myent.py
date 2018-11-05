import tkinter


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