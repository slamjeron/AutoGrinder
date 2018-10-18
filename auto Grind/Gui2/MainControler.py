

class playControls():
    def __init__(self):
        self.recordList=list()
    def play(self):
        print('playing')
        return

    def stop(self):
        print('stopping')
        return

    def pause(self):
        print('stopping')
        return

    def delete(self):
        print('deleating')
        return

    def record(self):
        print('recording')
        return

    def editselect(self,selected):
        # open the editing page
        print('editing selected')
        selectedIndex=list()
        for index in selected:
            selectedIndex.append(index[0])
            print(index[0])
        return
