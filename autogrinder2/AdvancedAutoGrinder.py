# coding=utf-8
import pickle
from threading import Thread, Event
from pyautogui import *
from pynput import keyboard, mouse

#pyinstaller advanstAutoGrinder.py to publish prgram

recording = False
playing = False
class GuiCon(object):
    def __init__(self):
        self._clickList = list()
        self.fileName = 'default'
        self.ex = False
        self.up = False
        self.rep = 1
        self.stopFla = Event()
        self.pl = PlayThread(self.stopFla, self._clickList, self.rep)
        self.active = True
        self.pl.start()
        mn = Menue(self.startStatments)
        mn.start()
        self.pl.playSpeed = 1
        try:
            mfile = open('currentFile' + '.txt', 'rb')
            self.fileName = pickle.load(mfile)
            self.openRecord()
        except FileNotFoundError:
            print('')
        self._stopCommand = 'q'
        self._stRecordCommand = 'r'
        self._playRec = 'p'
        self._endComand = 'esc'
        self.pauseKey = '0'
        self.resumeKey = '1'
        self.slowerKey = '+'
        self.speedKey = '-'
        self.clickKey = '2'
        self.replaceKey = '3'
        self.dellKey = 'delete'
        self.nextKey = 'right'
        self.backKey = 'left'
    def start(self):
        # begins my program
        with keyboard.Listener(on_press=self.on_key_press) as self.keylis:
            with mouse.Listener(on_click=self.on_click) as self.mouse_listener:
                self.mouse_listener.join()
        print('ending program\n enter any value to end the program')
    def startStatments(self):
        while self.active:
            if self.active:
                print('End: -1\nHelp: 1\nChange Repeat Amount: 3\nreset record: 4\nchange file Name and location: 5\n'
                      'Change speed: 6\nview record: 7\n')
                select = input('selection: ')
                if not self.active:
                    return
                try:
                    select = int(select)
                except ValueError:
                    print('value is not an integer')
                if select == 1:
                    print('the current Hot Keys\nkey "', self._stRecordCommand, '" starts Recording\nKey "',
                          self._playRec,
                          '" Starts Playing back your mouse clicks and key strokes\nKey "', self._stopCommand,
                          '" stops recording and play back\nKey "', self._endComand, '" stops the program')
                elif select == 99:
                    print('the current Hot Keys\nkey "', self._playRec, '" starts Recording: 1\nKey "', self._playRec,
                          '" Starts Playing back your mouse clicks and key strokes: 2\nKey "', self._stopCommand,
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
                    print('your curint files name is ', self.fileName)
                    txt = input('input the new text file name: ')
                    self.fileName = txt
                    try:
                        self.openRecord()
                    except FileNotFoundError:
                        print('')
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
        comand = ''
        if len(self.pl.array) > 0:
            for li in self.pl.array:
                if li[0] == 0:
                    comand = 'left click'
                elif li[0] == 2:
                    comand = 'key Press'
                print('comand=', comand, '  delay=', li[1], '   mouse point=', li[2], '   key button=', li[3])
    def stopAll(self):
        global recording
        global playing
        recording = False
        playing = False
        self.mouse_listener.stop()
        self.keylis.stop()
        self.stopFla.set()
        self.active = False
    def stop(self):
        global playing
        global recording
        playing = False
        recording = False
        print('pausing')
        self.save_record()
    def save_record(self):
        """
        saves the record
        """
        mfile = open(self.fileName + '.txt', 'wb')
        obj = [self.pl.array, self._stopCommand, self._stRecordCommand, self._playRec, self._endComand, self.rep,
               self.pl.playSpeed]
        pickle.dump(obj, mfile)
        print('saved')
        mfile = open('currentFile' + '.txt', 'wb')
        pickle.dump(self.fileName, mfile)
        mfile.close()
    def openRecord(self):
        mfile = open(self.fileName + '.txt', 'rb')
        self.pl.array, self._stopCommand, self._stRecordCommand, self._playRec, self._endComand, self.rep, self.pl.playSpeed = pickle.load(
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
        self.pl.array = list()
    def on_click(self, x, y, button, pressed):
        global recording
        # gets when the mouse clicks on the screen and records it
        if recording:
            if pressed:
                if self.up:
                    self.up = False
                    pnt = int(x), int(y)
                    lis = [0, self.pl.getMilsec(), pnt, '']
                    self.pl.array.append(lis)
                    self.pl.millsec = 0
            else:
                self.up = True
    def on_key_press(self, key_code):
        """
        determins what keys do and records them
        """
        global recording
        global playing
        key = str(key_code).strip('\'')
        key = str(key).replace('Key.', '')
        if key == self._endComand:
            self.stopAll()
            return False
        elif key == self._stRecordCommand and not recording and not playing :
            self.record()
        elif key == self._playRec and recording == False and playing == False:
            print('play key hit')
            # self.pl is the Player class a thread that plays the recording and keeps track of time.
            # the commands below help the player class know what to do.
            self.pl.slowing = False
            self.pl.speedUp = False
            self.pl.delete = False
            self.pl.insertClick = False
            self.pl.pause = False
            self.play()
        elif key == self._stopCommand:
            self.stop()
        elif recording:
            lis = [2, self.pl.millsec, None, key]
            self.pl.array.append(lis)
            self.pl.millsec = 0
            print(key)
        elif playing:
            # any item with the name of self.***key is a String holding a key name
            if self.slowerKey == key:
                self.pl.slowing = True
            if self.speedKey == key:
                self.pl.speedUp = True
            if self.pauseKey == key:
                self.pl.pause = True
            if self.resumeKey == key:
                self.pl.pause = False
            if self.dellKey == key and self.pl.pause:
                self.pl.delete = True
            if self.clickKey == key and self.pl.pause:
                self.pl.insertClick = True
            if self.nextKey == key and self.pl.pause:
                self.pl.next = True
            if self.backKey == key and self.pl.pause:
                self.pl.previous = True
            if self.replaceKey == key and self.pl.pause:
                self.pl.replace = True
class PlayThread(Thread):
    """
    plays you’r recording and keeps track of time
    """
    def __init__(self, event, array, rep):
        Thread.__init__(self)
        self.stopped = event
        self.millsec = 0
        self.array = list()
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
        self.replace = False
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
                arrlen = len(self.array)
                if index < arrlen:
                    try:
                        if self.millsec > self.array[index][1] - ((self.playSpeed / 100) * self.array[index][1]):
                            if self.array[index][0] == 0:
                                click(self.array[index][2])
                            elif self.array[index][0] == 2:
                                str = self.array[index][3]
                                press(str)
                            index += 1
                            self.millsec = 0
                        else:
                            if self.pause == False:
                                if self.slowing:
                                    self.array[index][1] += 1000
                                    print('slowing down')
                                    self.slowing = False
                                if self.speedUp:
                                    self.array[index][1] -= 100
                                    print('speeding up')
                                    self.speedUp = False
                                self.millsec += 1
                            else:
                                if self.delete:
                                    try:
                                        del self.array[index]
                                    except IndexError:
                                        index -= 1
                                        moveTo(self.array[index][2])
                                    print('deleting')
                                    self.delete = False
                                if self.insertClick:
                                    pnt = position()
                                    lis = [0, 2000, pnt, '']
                                    self.array.insert(index + 1, lis)
                                    self.millsec = 0
                                    print('adding click')
                                    self.insertClick = False
                                    index += 1
                                if self.replace:
                                    pnt = position()
                                    lis = [0, self.array[index][1], pnt, '']
                                    self.array[index] = lis
                                    self.millsec = 0
                                    print('replacing click')
                                    self.replace = False
                                    index += 1
                                if self.next:
                                    index += 1
                                    try:
                                        moveTo(self.array[index][2])
                                    except IndexError:
                                        index -= 1
                                        moveTo(self.array[index][2])
                                    self.millsec = 0
                                    print('index: ', index)
                                    self.next = False
                                if self.previous:
                                    index -= 1
                                    try:
                                        moveTo(self.array[index][2])
                                    except IndexError:
                                        index = 0
                                    print('index: ', index)
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
