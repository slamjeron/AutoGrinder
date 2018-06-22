import pickle
from threading import Thread, Event

from pyautogui import *
from pynput import keyboard, mouse

recording = False
playing = False


class GuiCon(object):
    def __init__(self):

        self._clickList = list()
        self._stopCommand = 'q'
        self._stRecordCommand = 'f11'
        self._playRec = 'p'
        self._endComand = 'esc'
        self.fileName = 'default'

        self.pauseKey = ''
        self.resumeKey = ''
        self.slowerKey = '+'
        self.speedKey = '-'
        self.clickKey = ''
        self.dellKey = ''
        self.nextKey = ''
        self.backKey = ''

        self.ex = False
        self.up = False
        self.rep = 1
        self.stopFla = Event()
        self.pl = PlayThread(self.stopFla, self._clickList, self.rep)
        self.active = True

        self.pl.start()

        mn = Menue(self.startStatments)
        mn.start()
        try:
            self.openRecord()
        except FileNotFoundError:
            print('')
        self.pl.playSpeed = 60

    def startStatments(self):
        while self.active:
            if self.active:
                print(
                    'End: -1\nHelp: 1\nChang Repeat Amount: 3\nreset record: 4\nchange fileName and location: 5\nChange speed: 6\n'
                    'view record: 7\n')
                select = input('selection: ')
                if self.active == False:
                    return
                try:
                    select = int(select)
                except ValueError:
                    print('value is not an integer')
                if select == 1:
                    print('the current Hot Keys\nkey "', self._stRecordCommand, '" starts Recording\nKey "',
                          self._playRec,
                          '" Starts Playing bacqk your mouse clicks and key stroks\nKey "', self._stopCommand,
                          '" stops recording and play back\nKey "', self._endComand, '" stops the program\n\n'
                                                                                     'to increase the time it takes to play part of the recording type the "',
                          self.slowerKey,
                          '" key to decrease the time it takes to play the recording type the "', self.speedKey, '" ')
                elif select == 99:
                    print('the current Hot Keys\nkey "', self._playRec, '" starts Recording: 1\nKey "', self._playRec,
                          '" Starts Playing back your mouse clicks and key stroks: 2\nKey "', self._stopCommand,
                          '" stops recording and play back:3\nKey "', self._endComand, '" end the program: 4')

                    keysel = input('select:')
                    try:
                        keysel = int(keysel)
                    except ValueError:
                        print('value is not an integer')

                    if keysel == 1:
                        print('type the key you would like for the record command')
                    elif keysel == 2:
                        print('type the key you would like for the play command')
                    elif keysel == 3:
                        print('type the key you would like for the stop command')
                    elif keysel == 4:
                        print('type the key you would like for the end program command')
                elif select == 3:
                    num = input('number of times you would like to repeat the record:')
                    try:
                        num = int(num)
                    except ValueError:
                        print('value is not an integer')
                    self.pl.rep = num
                    self.rep = num
                elif select == 4:
                    txt = input('are you sure you want to delete your record type "y" if you do other wise type "n": ')
                    if txt == 'y':
                        self.resetRecord()


                elif select == 5:
                    txt = input('input the new text file name: ')
                    self.fileName = txt
                    try:
                        self.openRecord()
                    except FileNotFoundError:
                        print('')
                    self.resetRecord()
                elif select == 6:
                    num = input('enter the play back speed 1 is normal speed 20 is 20% faster input 80 for the fastest '
                                'speed and normal is the slowest: ')

                    try:
                        num = int(num)
                    except ValueError:
                        print('value is not an integer')
                    if num < 81:
                        if num > 0:
                            if num == 1:
                                self.pl.playSpeed = 0
                            else:
                                self.pl.playSpeed = num
                        else:
                            print('you can not make playback go any slower than normal')
                    else:
                        print('input must be smaller than 81')
                elif select == 7:
                    self.printRecord()
                elif select == -1:
                    self.stopAll()
                print()

    def printRecord(self):
        if len(self.pl._array) > 0:
            for li in self.pl._array:
                if li[0] == 0:
                    comand = 'left click'
                elif li[0] == 2:
                    comand = 'key Press'
                print('comand=', comand, '  delay=', li[1], '   mouse point=', li[2], '   key button=', li[3])

    def start(self, parent=None):
        with keyboard.Listener(on_press=self.OnKeyPress) as self.keylis:
            with mouse.Listener(on_click=self.on_click) as self.mouse_listener:
                self.mouse_listener.join()
        print('ending program\n enter any value to end the program')

    def stopAll(self):
        global recording
        global playing

        recording = False
        playing = False
        self.mouse_listener.stop()
        self.keylis.stop()
        self.stopFla.set()
        self.active = False
        self.menEvent.set()

    def stop(self):
        global playing
        global recording
        playing = False
        recording = False
        print('pausing')
        self.saveRecord()

    def saveRecord(self):
        mfile = open(self.fileName + '.txt', 'wb')
        obj = [self.pl._array, self._stopCommand, self._stRecordCommand, self._playRec, self._endComand, self.rep,
               self.pl.playSpeed]
        pickle.dump(obj, mfile)
        print('saved')
        mfile.close()

    def openRecord(self):

        mfile = open(self.fileName + '.txt', 'rb')
        self.pl._array, self._stopCommand, self._stRecordCommand, self._playRec, self._endComand, self.rep, self.pl.playSpeed = pickle.load(
            mfile)
        mfile.close()

        self.pl.rep = int(self.rep)
        print('\nrepititions:', self.rep)
        print('\nplay speed:', self.pl.playSpeed)

    def record(self):
        global recording

        self.up = True
        recording = True
        print('recording')

    def on_click(self, x, y, button, pressed):
        global recording
        if recording == True:
            if pressed:
                if self.up == True:
                    self.up = False
                    pnt = int(x), int(y)
                    lis = [0, self.pl.getMilsec(), pnt, '']
                    self.pl._array.append(lis)
                    self.pl.millsec = 0
            else:
                self.up = True

    def play(self, rep=0):
        global playing
        global recording
        playing = True
        self.pl.millsec = 0
        self.pl.cnt = 0
        if rep > 0:
            self.pl.rep = rep
        self.pl.cnt = 0
        print('playing record')

    def resetRecord(self):
        print('reseting clicks')
        self.pl._array = list()

    def OnKeyPress(self, keyCode):
        global recording
        global playing
        key = str(keyCode).strip('\'')
        key = str(key).replace('Key.', '')
        if key == self._endComand:

            self.stopAll()
            return False
        elif key == self._stRecordCommand and recording == False and playing == False:
            self.record()
        elif key == self._playRec and recording == False and playing == False:
            print('play key hit')
            self.pl.slowing = False
            self.pl.speedUp = False
            self.pl.delete = False
            self.pl.insertClick = False
            self.pl.pause = False
            print('playing intems = false')
            self.play()

        elif key == self._stopCommand:
            self.stop()
        elif recording:
            lis = [2, self.pl.millsec, None, key]
            self._clickList.append(lis)
            self.pl.millsec = 0
            print(key)
        elif playing == True:
            if self.slowerKey == key:
                self.pl.slowing = True
            if self.speedKey == key:
                self.pl.speedUp = True
            if self.pauseKey == key:
                self.pl.pause = True
                print('trying pause')
            if self.resumeKey == key:
                self.pl.pause == False
            if self.dellKey == key and self.pl.pause:
                self.pl.delete = True
            if self.clickKey == key and self.pl.pause:
                self.pl.insertClick = True
            if self.nextKey == key and self.pl.pause:
                self.pl.next = True
            if self.backKey == key and self.pl.pause:
                self.pl.previous = True


class PlayThread(Thread):
    def __init__(self, event, array, rep):
        Thread.__init__(self)
        self.stopped = event
        self.millsec = 0

        self._array = list()
        self.rep = rep
        self.cnt = 0
        self.playSpeed = 0
        self.slowing = False
        self.speedUp = False
        self.delete = False
        self.insertClick = False
        self.pause = False
        self.next = False
        self.previous = False

    def getMilsec(self):
        return self.millsec

    def run(self):
        global playing
        global recording
        playing = False
        self.millsec = 0
        index = 0

        while not self.stopped.wait(1 / 1000.0):

            if playing:

                arrlen = len(self._array)
                if index < arrlen:
                    try:
                        if self.millsec > self._array[index][1] - ((self.playSpeed / 100) * self._array[index][1]):

                            if self._array[index][0] == 0:
                                click(self._array[index][2])

                            elif self._array[index][0] == 2:
                                str = self._array[index][3]

                            index += 1
                            self.millsec = 0
                        else:
                            if self.pause == False:
                                if self.slowing:
                                    self._array[index][1] += 1000
                                    print('slowing down')
                                    self.slowing = False
                                if self.speedUp:
                                    self._array[index][1] -= 100
                                    print('speeding up')
                                    self.speedUp = False
                                self.millsec += 1
                            else:
                                if self.millsec==1:
                                    moveTo(self._array[index][2])
                                if self.delete:
                                    try:
                                        del self._array[index]
                                    except IndexError:
                                        index -= 1
                                        moveTo(self._array[index][2])

                                    print('deleting')
                                    self.delete = False
                                if self.insertClick:
                                    pnt = position()
                                    lis = [0, 2000, pnt, '']

                                    self._array.insert(index + 1, lis)
                                    self.millsec = 0
                                    print('adding click')
                                    self.insertClick = False
                                    index+=1
                                if self.next:
                                    index += 1
                                    try:
                                        moveTo(self._array[index][2])
                                    except IndexError:
                                        index -= 1
                                        moveTo(self._array[index][2])
                                    self.millsec = 0
                                    self.next = False
                                if self.previous:
                                    index -= 1
                                    try:
                                        moveTo(self._array[index][2])
                                    except IndexError:
                                        index = 0

                                    self.millsec = 0
                                    self.previous = False
                    except IndexError:
                        print('cant do that')

                else:
                    index = 0

                    self.cnt += 1

                if self.cnt >= self.rep:
                    index = 0
                    self.cnt = 0
                    print('ending play back')
                    playing = False
            else:
                index = 0
            if recording:
                self.millsec += 1


class Menue(Thread):
    def __init__(self, startst):
        Thread.__init__(self)
        self.startst = startst

    def run(self):
        self.startst()


def main():
    con = GuiCon()
    con.start()
    return 0


main()
