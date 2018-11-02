class typerReader():
    def getType(self,item):
        if item.object==Mouse.object:
            return Mouse(item.get())

        if item.object==KeyBoard.object:
            return KeyBoard(item.get())

        if item.object==Color.object:
            return Color(item.get())

class Mouse():
    move = 0

    leftClick = 1
    leftDown = 2
    leftUp = 3
    rightClick = 4
    rightDown = 5
    rightUp = 6
    object = 'mouse'


    def __init__(self, secondDelay=None, event=None, position=None):
        self.eventTypes = ['move', 'Left Click', 'Left Down', 'Left Up', 'Right Click', 'Right Down', 'Right Up']
        self.event = event
        self.strEvent = self.eventTypes[event]
        self.position = position
        self.secondDelay = secondDelay

    def __str__(self):
        return self.eventTypes[self.event] + ' |delay = ' + str(self.secondDelay) + '| point ' + str(self.position)

    def get(self):
        return self.secondDelay, self.event, self.position


class KeyBoard():
    Type = 0

    Press = 1
    Release = 2
    typeString = 3
    object = 'key'
    eventTypes = ['type', 'Press', 'release', 'type string']

    def __init__(self, secondDelay=None, event=None, key=None, ):
        self.event = event
        self.strEvent = self.eventTypes[event]
        self.key = key
        self.secondDelay = secondDelay

    def get(self):
        return self.secondDelay, self.event, self.key

    def __str__(self):
        return self.eventTypes[self.event] + '|delay = ' + str(self.secondDelay) + '| key ' + self.key


class Color():
    delay = 0
    ifCondition = 1
    eventTypes = ['delay', 'if Condition']
    object = 'color'

    def __init__(self, secondDelay=None, event=None, color=None, position=None, onTrue=False, trueIndex=None,
                 falseIndex=None):
        self.event = event
        print(event)
        self.strEvent = self.eventTypes[event]
        self.color = color
        self.position = position
        self.secondDelay = secondDelay
        self.onTrue = onTrue
        self.trueIndex = trueIndex
        self.falseIndex = falseIndex

    def __str__(self):
        if self.event == 0:
            return self.eventTypes[self.event] + ' |delay = ' + str(self.secondDelay) + '| Color ' + str(
                self.color) + '| position ' + str(self.position) + '|next when = ' + str(self.onTrue)
        else:
            return self.eventTypes[self.event] + ' |delay = ' + str(self.secondDelay) + '| Color ' + str(
                self.color) + '| position ' + str(self.position) + 'on true index = ' + str(
                self.trueIndex) + 'on false index = ' + str(self.falseIndex)

    def get(self):
        return self.secondDelay, self.event, self.color, self.position, self.onTrue, self.trueIndex, self.falseIndex


class GoTo():

    def __init__(self, secondDelay, index=None, addindex=None):
        self.secondDelay = secondDelay
        self.object = 'goto'
        if index == None:
            self.addindex = addindex
        else:
            self.index = index

    def __str__(self):
        if self.index == None:
            return 'delay = ' + self.secondDelay + '| go to index =' + self.addindex
        else:
            return 'delay = ' + self.secondDelay + '| go to index =' + self.index


class NamedEvents():
    def __init__(self, names=[], events=[[]]):
        self.names = names
        self.events = events
        self.object = 'named'


class NamedEvent():
    def __init__(self, name, events=[]):
        self.name = name
        self.events = events
