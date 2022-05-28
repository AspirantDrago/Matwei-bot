import os
from main import *
ls  = []
ad = 0


if not os.path.isfile('юзеры.txt'):
    with open('юзеры.txt', 'w') as f:
        print(0, file=f)






class Proverka():
    def writing(self):
        with open('юзеры.txt', 'a') as f:
            for i in ls:
                i = str(i)
                print(i, file=f)


    def find_id(self):
        with open('юзеры.txt', 'a+') as f:
            for i in f:
                i = str(i)
                ls.append(int(i))
    def quit(self):
        exit()



os.startfile('main.py')



if check_erors == True:
    p = Proverka()
    p.find_id()
    os.startfile('main.py')





#p = Proverka()
#p.find_id()
#
#s = Proverka()
#s.writing()