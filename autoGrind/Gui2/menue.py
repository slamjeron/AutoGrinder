import tkinter


class MyMenu():
    def onExit(self):
        self.main.quit()

    def onSave(self):
        print('Saving')

    def onSaveAs(self):
        print('Saving as')

    def onOpen(self):
        print('opening dialogue')

    def onEditingPage(self):
        print('showing Editing Page')

    def onHotKeyPage(self):
        print('showing Editing Page')

    def onRecordSettings(self):
        print('showing rec settings editor')

    def __init__(self, parent=tkinter.Tk):
        self.main = parent
        self.menuBar = tkinter.Menu(parent)

    def editAll(self):
        return
    def set(self):
        fileMenu = tkinter.Menu(self.menuBar)
        openResentMb = tkinter.Menu(fileMenu)
        viewMenu = tkinter.Menu(fileMenu)
        self.main.config(menu=self.menuBar)
        self.menuBar.add_cascade(label='file', menu=fileMenu)

        fileMenu.add_command(label="Save", command=self.onSave)
        fileMenu.add_command(label="Save as", command=self.onSaveAs)
        fileMenu.add_command(label="Open", command=self.onOpen)
        fileMenu.add_cascade(label="Open recent", menu=openResentMb)
        openResentMb.add_command(label='recent file')
        fileMenu.add_command(label="Exit", command=self.onExit)

        def addResentFile(label,command):
            openResentMb.add_command(label=label,command=command)

        self.addResentFile =addResentFile
        self.menuBar.add_cascade(label='View', menu=viewMenu)
        viewMenu.add_command(label='Editing page', command=self.onEditingPage)
        viewMenu.add_command(label='Hot key page', command=self.onHotKeyPage)
        viewMenu.add_command(label='record settings', command=self.onRecordSettings)
        editMenue= tkinter.Menu(self.menuBar)
        editMenue.add_command(label="edit all", command=self.editAll)
    def addResentFile(self,label,command):
        return