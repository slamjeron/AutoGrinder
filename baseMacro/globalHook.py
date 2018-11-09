import pynput as keyHook

class myHook():
    def __init__(self):
        object.__init__(self)

    def startHook(self):
        print('starting hook')
        with keyHook.keyboard.Listener(on_press=self.on_key_press, on_release=self.on_key_relaese) as self.keylis:
            with keyHook.mouse.Listener(on_click=self.on_click) as self.mouse_listener:
                self.mouse_listener.join()
    def on_click(self, x, y, button, pressed):
        return

    def on_key_press(self, key_code):
        return

    def on_key_relaese(self, key_code):
        return
    def close(self):
        print('stoping hook')
        self.mouse_listener.stop()

if __name__ == '__main__':
    hook=myHook()
    hook.startHook()