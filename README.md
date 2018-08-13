### linux-AutoGrinder
## Synopsis

The purpos of "Auto Grinder" is to automate repetitive tasks on the computer. Built for games or buisnes applications, I have used it to play a game caled "Darkorbit".

## Code Example

to record what the user dose i use the library pynput code witch can acces an use input then i place it in a list.
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

    def on_key_press(self, keyCode):
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

            #self.pl is the Player class a thread that plays the recording and keeps track of time.
            #the commands below help the player class know what to do.
            self.pl.slowing = False
            self.pl.speedUp = False
            self.pl.delete = False
            self.pl.insertClick = False
            self.pl.pause = False
            print('playing intems = false')
            self.play()




## Motivation

I built this program to remove repetitive tasks from my life. I curently use a java program, I built to play a game caled
dark orbit. when i got new computers I set them up with ubuntu, and for the life of me i could not get the program I had developed to work with the linux operating system. eventuily this program will do more than just repeat what was recorded
do the grinding for 'DarkOrbit'

## Installation
to install my program click <a href="https://github.com/slamjeron/linux-AutoGrinder/raw/master/autogrinder2/dist/advanstAutoGrinder.zip" download="advancedAutoGrinder">advansed auto grinder</a> then unzip the file then double click on the folder and then
right click inside the folder, click Open in Turminal, then type sudo ./advanstAutoGrinder then a terminal window should open.
Provide code examples and explanations of how to get the project.

## API Reference
to build my program i used pynput to get user input, pyautogui to simulate user input, Pickle to save my programs information
and that is all I used.

## Tests
this will start the program
def main():
    con = GuiCon()
    con.start()
    return 0


main()

this code keeps track of user input

    def on_click(self, x, y, button, pressed):
        print (x,y)


    def on_key_press(self, key_code):
        print (key_code)
and those are the main functions

## Contributors

my program has many key comands that you will need to know
in both the advanstAutoGrinder and the comandcontroler i have the folowing hot keys,
"-" key will increas the speed of the next action "+" key will decreas the speed of the next action,
"Q" will stop the recording and play back "R" starts recording "P" starts playing back your recording
"ESC" will stop the program though to compleat the the closing proses you must ither close the program or
type somthing in the turminal.

#comands for advanstAutoGrinder
"0" key will paus play back so you can edit the curent action right erow key will make you go to the privous action left
erow key will make you go to the next action. curently you may not resume the play back you must press "Q" them "P" to start
the sequence over. when paused type 2 too add a click to the curent index. too replace an action type 3 and where ever your curser
is it will click there next time the record is played.


## License

this program is an open sorce program.
