import random
import time
from tkinter import*

root = Tk()
root.geometry("1350x750+0+0")
root.title("Puzzle Game")
root.configure(bg='Cadet Blue')

Tops = Frame(root, bg='Cadet Blue', pady=2, width=1350, height=100, relief=RIDGE)
Tops.grid(row=0, column=0)

lblTitle = Label(Tops, font=('arial', 80, 'bold'), text="Advanced Puzzle Game", bd=10, bg='Cadet Blue',fg='Cornsilk', justify=CENTER)
lblTitle.grid(row=0,column=0)

mainFrame = Frame(root, bg='Powder Blue', bd=10, width=1350, height=600, relief=RIDGE)
mainFrame.grid(row=1, column=0, padx=30)

leftFrame =Frame(mainFrame, bd=10, width=700, height=500, pady=2, bg='Cadet Blue', relief=RIDGE)
leftFrame.pack(side=LEFT)

RightFrame = Frame(mainFrame, bd=10, width=540, height=500, padx=1, bg='Cadet Blue', relief=RIDGE)
RightFrame.pack(side=RIGHT)


RightFrame1 = Frame(RightFrame, bd=10, width=540, height=200, padx=10, pady=2, bg='Cadet Blue', relief=RIDGE)
RightFrame1.grid(row=0, column=0)


RightFrame1a = Frame(RightFrame, bd=10, width=540, height=140, padx=10, pady=2, bg='Cadet Blue', relief=RIDGE)
RightFrame1a.grid(row=1, column=0)


RightFrame2b = Frame(RightFrame, bd=10, width=540, height=140, padx=10, pady=2, bg='Cadet Blue', relief=RIDGE)
RightFrame2b.grid(row=2, column=0)


numberofClicks = 0
displayClicks = StringVar()
displayClicks.set("Number of clicks " + "\n" + str(numberofClicks))

gameStateString = StringVar()

def upDateCounter():
	global numberofClicks, displayClicks

	displayClicks.set("Number of clicks " + "\n" + str(numberofClicks))

def gameStateUpdate(gameState):
	global gameStateString
	gameStateString.set(gameState)


class Button_:
	def __init__(self, text_, x, y):
		self.enterValue = text
		self.textTaken = StringVar()
		self.textTaken.set(text_)
		self.x = x
		self.y = y
		self.btnNumber = Button(leftFrame, textvariable.textTaken, font=('arial',80), bd=3, command=lambda i=self.x, j=self.y : emptySpotChecker(i, j))
		self.btnNumber.place(x=self.x*150, y=self.y*150, width=170, height=170)


def shuuffle():
	global btnNumbers, displayClicks
	nums[]
	for x in range(12):
		x += 1
		if x == 12:
			nums.append("")
	    else:
	    	nums.append(str(x))

	for y in range(len (btnNumbers)):
		for x in range(len (btnNumbers[y])):
			num = random.choice(nums)
			btnNumbers[y] [x].textTaken.set(num)
			nums.remove(num)

	numberofClicks = 0
	upDateCounter()
	gameStateUpdate("")		




























root.mainloop()