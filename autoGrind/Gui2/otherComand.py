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
        actionDrop.grid(row=0,column=0)
        actionDrop.config(width=20)



if __name__ == '__main__':
    playcon = tkinter.Tk()
    edit = editPage(playcon)
    edit.mainloop()