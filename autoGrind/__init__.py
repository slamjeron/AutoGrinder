
from autoGrind.Gui2.main import playControls,mainPage,threading

# if __name__ == '__main__':
#     playcon = playControls()
#     main = mainPage(playcon)
#     thread= threading.Thread(target=playcon.hook.startHook)
#     thread.start()
#     main.mainloop()
numbers =[444,654,78,44,33,5345,66,55,23,44,666,778,323]
orederd= []

def findLargest(list):
    largest=0
    for num in list:
        if num > largest:
            largest=num
    return largest
temp=numbers

while len(temp)>0:
    larg=findLargest(temp)
    temp.remove(larg)
    orederd.append(larg)
    print(temp)
    if len(temp)==0:
        break
    print(len(temp))
print(orederd)