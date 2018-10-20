
class editCon():
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

        self.linesToEdit=int(linsEdit.split(','))
        if action =='Same':
            print('')
        else:
            for line in self.linesToEdit:
                print(actions[action])
                self.recording[line][0]=int(actions[action])
        if timeDelay == 'Same':
            print('')
        else:
            for line in self.linesToEdit:
                self.recording[line][1]=int(timeDelay)

        if point[0] == 'Same':
            print('')
        else:
            for line in self.linesToEdit:
                self.recording[line][1] = int(point[0])

        if point[1] == 'Same':
            print('')
        else:
            for line in self.linesToEdit:
                self.recording[line][1] = int(point[0])

        self.close()
        self.update()
        return