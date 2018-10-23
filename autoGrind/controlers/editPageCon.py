from autoGrind.controlers.pageBluePrint import mainPagebuttonBluePrint


class editCon(mainPagebuttonBluePrint):
    def __init__(self):
        object.__init__(self)
        self.recording=list()
        self.linesToEdit=list()
        self.enterlines=None
        self.close=None
        self.update=None

    def showEditLines(self):
        strin=','.join(map(str,self.linesToEdit))
        if strin is not None:
            self.enterlines(strin)


    def saveComand(self,action,timeDelay,point,keyevent,linsEdit):
        actions={'Left Click':'1', 'Right Click':'2', 'Drag Start':'3',
                           'Drag Stop':'4', 'Type':'5', 'Color Stall':'6', 'Color Condition':'7','name groop':'8'}
        self.linesToEdit = list()
        self.recording=self.getRecording()
        for item in linsEdit.split(','):

            print(item)
            self.linesToEdit.append(int(item))

        if action =='Same':
            print('')
        else:
            for line in self.linesToEdit:
                if line < len(self.recording):
                    print(actions[action])
                    self.recording[line][0]=int(actions[action])
        if timeDelay == 'Same':
            print('')
        else:
            for line in self.linesToEdit:
                if line<len(self.recording):
                    self.recording[line][1]=float(timeDelay)

        if point[0] =='Same':
            pass
        else:
            for line in self.linesToEdit:
                if line < len(self.recording):
                    self.recording[line][2][0]=int(point[0])
        if point[1] =='Same':
            pass
        else:
            for line in self.linesToEdit:
                if line < len(self.recording):
                    self.recording[line][2][1]=int(point[1])

        if keyevent=='Same':
            pass
        else:
            for line in self.linesToEdit:
                if line < len(self.recording):
                    self.recording[line][3]=keyevent
        self.setRecording(self.recording)
        self.showAll()
        self.close()
        return