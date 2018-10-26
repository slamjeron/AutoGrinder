import tkinter

from autoGrind.Gui2.myent import myEnt
from autoGrind.controlers.editPageCon import editCon


class editPage(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        editcon=editCon()
        recVar=tkinter.StringVar()
        actionDrop = tkinter.OptionMenu(parent, recVar, 'Same', 'Left Click', 'Right Click', 'Drag Start',
                                        'Drag Stop', 'Type', 'Color Stall', 'Color Condition', 'name groop')

        recVar.set('Color Stall')
        # there will be a dellay entry for the second
        actionDrop.grid(row=0,column=0)
        actionDrop.config(width=20)
        delaylab=tkinter.Label(parent,text='stall time ')
        delayAmount = tkinter.Spinbox(parent,from_=0,to=100000)
        delayAmount.grid(row=1,column = 1)
        delayAmount.config(width=10)



if __name__ == '__main__':
    playcon = tkinter.Tk()
    edit = editPage(playcon)

    edit.mainloop()