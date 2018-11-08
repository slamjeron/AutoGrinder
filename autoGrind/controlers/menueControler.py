from tkinter import filedialog
from autoGrind.controlers.pageBluePrint import mainPagebuttonBluePrint
import pickle
from pathlib import Path

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
            self.curentRecord=savediologue().name
        if self.curentRecord is not None:
            with open(self.curentRecord, 'wb') as handle:
                pickle.dump(self.getRecording(), handle, protocol=pickle.HIGHEST_PROTOCOL)
            handle.close()


        if self.curentRecord not in self.resentMacros:
            self.resentMacros.append(self.curentRecord)
            rec=self.curentRecord
            self.addResentFile(self.curentRecord,lambda :self.openrecent(rec))
            with open('./profiles.grind', 'wb') as handle:
                pickle.dump(self.resentMacros, handle, protocol=pickle.HIGHEST_PROTOCOL)
            handle.close()

    def openrecent(self,filename):
        self.curentRecord= filename
        self.open()
    def open(self):
        def openDiologue():
            return filedialog.askopenfile(filetypes=[('Auto Grinder file','.grind')])
        if self.curentRecord ==None:
            self.curentRecord=openDiologue()
            self.curentRecord = self.curentRecord.name


        if self.curentRecord is not None:
            with open(self.curentRecord, 'rb') as handle:
                self.setRecording(pickle.load(handle))

            handle.close()
            self.showAll()
        if self.curentRecord not in self.resentMacros:
            self.resentMacros.append(self.curentRecord)
            rec=self.curentRecord
            self.addResentFile(self.curentRecord,lambda :self.openrecent(rec))
            with open('./profiles.grind', 'wb') as handle:
                pickle.dump(self.resentMacros, handle, protocol=pickle.HIGHEST_PROTOCOL)
            handle.close()

    def openProHistory(self):
        with open('./profiles.grind', 'rb') as handle:
            self.resentMacros=pickle.load(handle)
            handle.close()
        templist=list()
        for recentmacro in  self.resentMacros:
            mac=Path(recentmacro)
            if mac.is_file():
                templist.append(recentmacro)
                self.addResentFile(recentmacro,lambda :self.openrecent(recentmacro))
        self.resentMacros=templist

    def __init__(self):
        object.__init__(self)
        self.curentRecord=None
        self.resentMacros=list()

    def copy(self):
        pass

    def past(self):
        pass
