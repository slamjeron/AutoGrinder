
class nameAct():
    def __init__(self,nameList=list(),actionList=[[[]]]):
        #[  [ [0,44,55],[2,55,77], ],[ [2,34,66] ]  ]
        self.nameList=nameList
        self.actionList=actionList

    def getActions(self,name):
        if name in self.nameList:
            ind =self.nameList.index(name)
            return self.actionList[ind]
    def setNamedAction(self,name=str(),actions=[]):
        if name not in self.nameList:
            self.nameList.append(name)
            self.actionList.append(actions)
        else:
            ind =self.nameList.index(name)
            self.actionList[ind].append(actions)

    def setname(self,index,name):
        if len(self.nameList)>index:
            self.nameList[index]=name

    def setAllActionsConectedToName(self,name=str(),actions=[[]]):
        if name in self.nameList:
            ind = self.nameList.index(name)
            self.actionList[ind]=actions

    def removeNamedAction(self,name=str()):
        if name in self.nameList:
            ind = self.nameList.index(name)
            del self.nameList[ind]
            del self.actionList[ind]