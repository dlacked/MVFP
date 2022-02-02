import os
from functools import partial
from tkinter import *
from random import *

ValueDic = {1:120, 2:160, 3:130, 4:100, 5:100, 6:100, 7:85, 8:90, 9:100, 10:100, 11:90, 12:70, 13:100, 14:90, 15:85, 16:60, 17:80, 18:90, 19:80, 20:75, 21:70, 22:75, 23:75, 24:70, 25:80, 26:80, 27:80, 28:65, 29:70, 30:70, 31:70, 32:70, 33:75, 34:70, 35:65, 36:70, 37:75, 38:70, 39:70, 40:70, 41:65, 42:70, 43:65, 44:65, 45:65, 46:65, 47:65, 48:60, 49:60, 50:80}
Score = 0
def mainclick(Score):
    while(True):
        root.title("Who is the most expensive player?")
        while(True):
            num1 = randrange(1, 51)
            num2 = randrange(1, 51)
            if num1 != num2 and ValueDic[num1] != ValueDic[num2]:
                break
        leftBackgroundImage = PhotoImage(file = "img/{}.png".format(num1)) #num1에 해당하는 선수
        leftImage = Label(image = leftBackgroundImage)
        leftImage.place(x = -2, y = -2)

        ButtonImage1 = PhotoImage(file = "img/buttonimage2.png")
        leftButton = Button(root, image = ButtonImage1, command = partial(leftclick, num1, num2, Score))
        leftButton.place(x = 296, y = 479)

        rightBackgroundImage = PhotoImage(file = "img/{}.png".format(num2)) #num2에 해당하는 선수
        rightImage = Label(image = rightBackgroundImage)
        rightImage.place(x = 620, y = -2)

        ButtonImage2 = PhotoImage(file = "img/buttonimage2.png")
        rightButton = Button(root, image = ButtonImage2, command = partial(rightclick, num1, num2, Score))
        rightButton.place(x = 920, y = 479)

        root.mainloop()


def leftclick(num1, num2, Score):
    if ValueDic[num1] > ValueDic[num2]:
        Score += 20
        mainclick(Score)
    else:
        gameover(Score)

    return

def rightclick(num1, num2, Score):
    if ValueDic[num1] < ValueDic[num2]:
        Score += 20
        mainclick(Score)
    else:
        gameover(Score)

    return

def gameover(Score):
    root.title("Value Over")
    go = PhotoImage(file = "img/gameover.png")
    goimage = Label(root, image=go)
    goimage.place(x=-2, y=-2)
    Scoretext = Label(root, text=f"{Score}", font=("Arial", 80), bg = "#567ACE", fg = "White")
    if Score == 0:
        Scoretext.place(x=605, y =420)
    else:
        Scoretext.place(x=575, y = 420)
    root.mainloop()

root = Tk()
root.title("main") #타이틀 이름 설정
root.minsize(width=1257, height=720)
root.maxsize(width=1257, height=720)

mainBackgroundImage = PhotoImage(file = "img/mainimage.png") #백그라운드 이미지 설정
mainImage = Label(root, image = mainBackgroundImage) #백그라운드 이미지 변수 선언
mainImage.place(x = -25, y = -2) #백그라운드 이미지 위치 설정

mainButtonImage = PhotoImage(file = "img/buttonimage1.png") #버튼 이미지 설정
mainButton = Button(root, image = mainButtonImage, command = partial(mainclick, Score)) #버튼 이미지 변수 선언
mainButton.place(x = 485, y = 540) #버튼 이미지 위치 설정


root.mainloop()
