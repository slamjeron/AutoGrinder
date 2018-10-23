import tkinter
from autoGrind.controlers.menueControler import MenueControler
class MyMenu():
    def onExit(self):
        self.main.quit()



    def __init__(self, parent=tkinter.Tk):
        self.main = parent
        self.menuBar = tkinter.Menu(parent)
        self.con=MenueControler()

    def editAll(self):
        return
    def set(self):
        fileMenu = tkinter.Menu(self.menuBar)
        openResentMb = tkinter.Menu(fileMenu)
        viewMenu = tkinter.Menu(fileMenu)
        self.main.config(menu=self.menuBar)
        self.menuBar.add_cascade(label='file', menu=fileMenu)

        fileMenu.add_command(label="Save", command= self.con.onSave)
        fileMenu.add_command(label="Save as", command= self.con.onSaveAs)
        fileMenu.add_command(label="Open", command= self.con.onOpen)
        fileMenu.add_cascade(label="recent macro", menu=openResentMb)
        fileMenu.add_command(label="Exit", command= self.con.onExit)


        self.menuBar.add_cascade(label='View', menu=viewMenu)
        viewMenu.add_command(label='Editing page', command= self.con.onEditingPage)
        viewMenu.add_command(label='Hot keys', command= self.con.onHotKeyPage)
        viewMenu.add_command(label='record settings', command= self.con.onRecordSettings)
        editMenue= tkinter.Menu(self.menuBar)
        editMenue.add_command(label="edit all", command=self.con.editAll)

        def addResentFile(label, command):
            openResentMb.add_command(label=label, command=command)
        self.con.addResentFile = addResentFile
