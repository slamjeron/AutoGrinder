from Gui import main
from properClose.recordingAction import recorder
from threading import Thread
from properClose.playRec import RecPlayer
from properClose.hotkeys import HotKeys


class MyThread(Thread):

    def __init__(self, method=None):
        Thread.__init__(self)
        self.running = True

    def stop(self):
        self.running = False

    def playmethod(self):
        return

    def recordMethod(self):
        return

    def act(self):
        return

    def run(self):
        if self.running:
            self.act()
            while self.running:
                self.playmethod()

                self.recordMethod()
        else:
            print('thread running')
            return


class mainControler():
    def __init__(self):
        self.page = main.mainPage()
        self.recorder = recorder()
        self.recorder.recording = False
        self.hotkeyCon = HotKeys()
        self.player = RecPlayer()
        self.timer = MyThread()
        self.play = MyThread()


    def closeHook(self):
        self.recorder.kill()
        self.timer.stop()
        self.play.stop()

        print('closing')

    def record(self):
        self.recorder.recording = True

    def playRecord(self):
        self.player.recording = self.recorder.array
        self.player.play()
        self.page.plBtnTxt.set("Playing")

    def stop(self):
        if self.recorder.recording:
            record = self.recorder.array
            if len(record) > 0:
                record.pop()
        self.recorder.recording = False
        self.player.playing = False
        self.page.plBtnTxt.set("Play")

    def pause(self):
        self.page.plBtnTxt.set("Paused")
        self.player.pause = True

    def delete(self):
        self.recorder.array = list()
        self.player.playing = False
        self.player.recording=self.page.records= self.recorder.array

    def changAllrecTimes(self,milsec):
        for item in self.recorder.array:
            item[1]=milsec
        self.player.recording = self.page.records = self.recorder.array
    def addControls(self):
        self.recorder.hotkeys = self.hotkeyCon.hotkeys
        self.recorder.hotkeyrel=self.hotkeyCon.hotkeyrel
        self.recorder.showInfo=self.page.displayAction

        self.hotkeyCon.play=self.playRecord
        self.hotkeyCon.stop = self.stop
        self.hotkeyCon.pause = self.pause
        self.hotkeyCon.record = self.record

        self.timer.recordMethod = self.recorder.timeCounter
        self.timer.playmethod = self.player.player
        self.player.recording = self.recorder.array
        self.player.stoped = self.stop


        controls = self.page.controls
        controls.record = self.record
        controls.delete = self.delete
        controls.pause = self.pause
        self.page.closeHook = self.closeHook
        self.page.records= self.recorder.array

        controls.play = self.playRecord
        controls.stop = self.stop

        self.play.act = self.recorder.startHook
        self.play.start()
        self.timer.start()
        self.page.start()


controler = mainControler()
controler.addControls()
