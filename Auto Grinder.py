
from Gui2.main import playControls,mainPage,threading

if __name__ == '__main__':
    playcon = playControls()
    main = mainPage(playcon)
    thread= threading.Thread(target=playcon.hook.startHook)
    thread.start()
    main.mainloop()

