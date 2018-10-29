
class Mouse():

    def __init__(self,secondDelay,event,position):
        self.move=0

        self.leftClick=1
        self.leftDown = 2
        self.leftUp = 3
        self.rightClick = 4
        self.rightDown = 5
        self.rightUp = 6
        self.eventTypes=['move','Left Click','Left Down','Left Up','Right Click','Right Down','Right Up']
        self.datatype='mouse'
        self.event=event
        self.strEvent= self.eventTypes[event]
        self.position=position
        self.secondDelay=secondDelay

    def __str__(self):
        return 'delay = '+self.secondDelay+'|'+self.eventTypes[self.event]+'| point '+self.position


class KeyBoard():

    def __init__(self, secondDelay, event, key):
        self.Type = 0

        self.Press = 1
        self.Release = 2
        self.typeString=3
        self.eventTypes = ['type', 'Press', 'release', 'type string']
        self.datatype = 'key'
        self.event = event
        self.strEvent=self.eventTypes[event]
        self.key = key
        self.secondDelay = secondDelay

    def __str__(self):
        return 'delay = '+self.secondDelay+'|'+self.eventTypes[self.event] + '| key ' + self.key


class Color():

    def __init__(self, secondDelay, event, color,position,onTrue=False,trueIndex=None,falseIndex=None):
        self.delay=0
        self.ifCondition=1
        self.eventTypes = ['delay','if Condition']
        self.datatype = 'color'
        self.event = event
        self.strEvent=self.eventTypes[event]
        self.color = color
        self.position = position
        self.secondDelay = secondDelay
        self.onTrue=onTrue
        self.trueIndex = trueIndex
        self.falseIndex = falseIndex

    def __str__(self):
        if self.event==0:
            return 'delay = '+self.secondDelay+'|'+self.eventTypes[self.event] + '| Color ' + self.color+'| position ' + self.position+ '|next when = '+self.onTrue
        else:
            return 'delay = '+self.secondDelay+'|'+self.eventTypes[self.event] + '| Color ' + self.color + '| position ' + self.position + 'on true index = '+str(self.trueIndex)+ 'on false index = '+str(self.falseIndex)

class GoTo():

    def __init__(self, secondDelay, index=None,addindex=None):
        self.secondDelay=secondDelay
        self.datatype = 'goto'
        if index==None:
            self.addindex=addindex
        else:
            self.index=index

    def __str__(self):
        if self.index==None:
            return 'delay = '+self.secondDelay+'| go to index ='+self.addindex
        else:
            return 'delay = '+self.secondDelay+'| go to index ='+self.index