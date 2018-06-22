### linux-AutoGrinder
## Synopsis

the purpos of this program "auto grinder" is to automate repetitive tasks on the computer wether it be for games or buisnes applications i use this program for a game caled "Darkorbit"

## Code Example

Show what the library does as concisely as possible, developers should be able to figure out **how** your project solves their problem by looking at the code example.
Make sure the API you are showing off is obvious, and that your code is short and concise.

to record what the user dose i use the library pynput witch can acces an use input then i place it in a list.
to use pynput call

this code determines what happens when you type a key or click the mouse

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
            if self.replaceKey == key and self.pl.pause:
                self.pl.replace = True


## Motivation

A short description of the motivation behind the creation and maintenance of the project. This should explain **why** the project exists.

## Installation

Provide code examples and explanations of how to get the project.

## API Reference

Depending on the size of the project, if it is small and simple enough the reference docs can be added to the README. For medium size to larger projects it is important to at least provide a link to where the API reference docs live.

## Tests

Describe and show how to run the tests with code examples.

## Contributors

Let people know how they can dive into the project, include important links to things like issue trackers, irc, twitter accounts if applicable.

## License

A short snippet describing the license (MIT, Apache, etc.)