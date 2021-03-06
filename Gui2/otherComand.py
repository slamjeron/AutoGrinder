import tkinter

from Gui2.myent import LblEnt
from controlers.otherComand import OtherComandControler


class AddComPage(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.pack()

        rec_var = tkinter.StringVar()
        controler = OtherComandControler()


        def close():
            parent.destroy()

        def parproto():
            close()

        def getTrueTimes():
            return reptimes.ent.get()

        controler.getTrueTimes = getTrueTimes

        parent.protocol("WM_DELETE_WINDOW", parproto)
        actionDrop = tkinter.OptionMenu(self, rec_var, 'Same','mouse move', 'Left Click', 'Right Click', 'Drag Start',
                                        'Drag Stop', 'Type', 'Color Stall', 'Color Condition',command=lambda _:controler.actionChanged(rec_var.get()))

        rec_var.set('Color Stall')
        # there will be a dellay entry for the second
        actionDrop.grid(row=0, column=0)
        actionDrop.config(width=20)
        delayFrame = tkinter.Frame(self)
        delayFrame.grid(row=0, column=1)
        delaylab = tkinter.Label(delayFrame, text='stall time ')

        delaylab.grid(row=0, column=0)
        vari = tkinter.StringVar()
        delayAmount = tkinter.Spinbox(delayFrame, from_=0, to=100000)
        delayAmount.grid(row=1, column=0)
        delayAmount.config(width=10)
        reptimes=LblEnt(delayFrame,'check times','spin')
        reptimes.ent.config(width=10)

        reptimes.grid(row=2,column=0)

        controler.close = close
        controler.getAction = rec_var.get
        pntClrbtn = tkinter.Button(self, textvariable = controler.editButtonTxt, command=controler.getPntCLR)
        controler.editButtonTxt.set('get Clr and Pixel')
        pntClrbtn.grid(row=1, column=1)

        def getDelay():
            return delayAmount.get()

        controler.getDelay = getDelay
        pntClrbtn = tkinter.Button(self, text='Save', command=controler.Save)
        pntClrbtn.grid(row=5, column=0,columnspan=2)

        infoLable = tkinter.Label(self, text='')
        infoLable.grid(row=6, column=0,columnspan=2)
        checked=tkinter.BooleanVar()
        nameDrop = tkinter.OptionMenu(self, controler.namedrop,*controler.actionNameList,command= controler.namechanged)
        nameDrop.grid(row=2,column=0)
        nameDrop.config(width=20)
        nameEnt=tkinter.Entry(self,textvariable=controler.name)
        nameEnt.grid(row=3, column=0)


        # self row 3 will be a combo box that the user can enter name
        # the name will be added to a list that can be axcest by the parent so i will add it to my controler.
        # the index of the action name list will be conected to a list of actions

        # user adds name
        # on save if name is not ''
        # if actionNameList.contains(name):
        # actions=actionList[actionNameList.index(name)]
        # else
        # actionNameList.append(name)
        # actions.append(cline)
        # actionList.append(actions)
        check=tkinter.Checkbutton(self,text= 'if pnt color = stored color move on',variable=checked)
        check.grid(row=4, column=0, columnspan=2)
        checked.set(True)

        def setInfo(text):
            infoLable['text'] = text

        setInfo('info')
        controler.setinfo = setInfo
        controler.getChecked = checked.get
        self.controler=controler




if __name__ == '__main__':
    playcon = tkinter.Tk()
    edit = AddComPage(playcon)

    edit.mainloop()
