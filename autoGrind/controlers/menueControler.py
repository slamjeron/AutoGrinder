from tkinter import  filedialog
from autoGrind.controlers.pageBluePrint import mainPagebuttonBluePrint
import pickle

class MenueControler(mainPagebuttonBluePrint):
    def onExit(self):
        return

    def onSave(self):
        self.save()
        print('saving')

    def onSaveAs(self):
        self.curentRecord =None
        self.save()
        return

    def onOpen(self):
        self.curentRecord = None
        self.open()
        return

    def onEditingPage(self):
        return

    def onHotKeyPage(self):
        return

    def onRecordSettings(self):
        return

    def editAll(self):
        return

    def set(self):
        return

    def addResentFile(self, label, command):
        return
    def save(self):
        def savediologue():
            return filedialog.asksaveasfile(defaultextension='.grind',filetypes=[('Auto Grinder file','.grind')])

        if self.curentRecord ==None:
            self.curentRecord=savediologue()
        if self.curentRecord is not None:
            print(self.curentRecord.name)
            with open(self.curentRecord.name, 'wb') as handle:
                pickle.dump(self.getRecording(), handle, protocol=pickle.HIGHEST_PROTOCOL)
            handle.close()
        if self.curentRecord.name not in self.resentMacros:
            self.resentMacros.append(self.curentRecord.name)
            self.addResentFile(self.curentRecord.name,self.curentRecord.name)
            with open('./profiles.grind', 'wb') as handle:
                pickle.dump(self.resentMacros, handle, protocol=pickle.HIGHEST_PROTOCOL)
            handle.close()
    def open(self):
        def openDiologue():
            return filedialog.askopenfile(filetypes=[('Auto Grinder file','.grind')])
        if self.curentRecord ==None:
            self.curentRecord=openDiologue()
        if self.curentRecord is not None:
            print(self.curentRecord.name)
            with open(self.curentRecord.name, 'rb') as handle:
                self.setRecording(pickle.load(handle))

            handle.close()
            self.showAll()
        if self.curentRecord.name not in self.resentMacros:
            self.resentMacros.append(self.curentRecord.name)
            self.addResentFile(self.curentRecord.name,self.curentRecord.name)
            with open('./profiles.grind', 'wb') as handle:
                pickle.dump(self.resentMacros, handle, protocol=pickle.HIGHEST_PROTOCOL)
            handle.close()
    def openProHistory(self):
        with open(self.curentRecord.name, 'rb') as handle:
            self.setRecording(pickle.load(handle))
    def __init__(self):
        object.__init__(self)
        self.curentRecord=None
        self.resentMacros=list()
