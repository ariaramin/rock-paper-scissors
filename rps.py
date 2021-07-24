#import moduls
import random
from random import randint
from tkinter import *
from tkinter.font import Font 

#create tk
master = Tk()
master.geometry('475x310')
master.title('Rock,Paper,Scissors')

bscore = 0
uscore = 0

# functions
def Restart():
    global bscore, uscore
    bscore = 0
    uscore = 0
    bot_score.set(0)
    user_score.set(0)


def play(rps):
    global bscore, uscore
    rps_random = ['Rock','Paper','Scissors']
    pc = rps_random[randint(0,2)]
    rps_bot.set(pc)

    if rps == 'rpsr':
        if pc == 'Paper':
            bscore += 1
            bot_score.set(bscore)
        elif pc =='Scissors':
            uscore += 1
            user_score.set(uscore)

    if rps == 'rpsp':
        if pc == 'Scissors':
            bscore += 1
            bot_score.set(bscore)
        elif pc =='Rock':
            uscore += 1
            user_score.set(uscore)
    
    if rps == 'rpss':
        if pc == 'Rock':
            bscore += 1
            bot_score.set(bscore)
        elif pc =='Paper':
            uscore += 1
            user_score.set(uscore)
        


# create GUI 
font = Font(family="Verdana", size=15)

rock_img = PhotoImage(file = r'./rock.png')
paper_img = PhotoImage(file = r'./paper.png')
scissors_img = PhotoImage(file = r'./scissors.png')

Label(master, text = 'Bot:', font=font).grid(row=0, column=0, columnspan=3)
rps_bot = StringVar()
Label(master, textvariable=rps_bot, font=font).grid(row=1, column=0, columnspan=3)

Label(master, image=rock_img).grid(row=2, column=0)
Button(master, text = 'Rock', command= lambda:play('rpsr'), width=10, bg='#FFD600', font=font).grid(row= 3, column= 0)

Label(master, image=paper_img).grid(row=2, column=1)
Button(master, text = 'Paper', command= lambda:play('rpsp'), width=10, bg='#64DD17', font=font).grid(row= 3, column= 1)

Label(master, image=scissors_img).grid(row=2, column=2)
Button(master, text = 'Scissors', command= lambda:play('rpss'), width=10, bg='#FF6D00', font=font).grid(row= 3, column= 2)

user_score = StringVar()
user_score.set(0)
Label(master, textvariable=user_score, width=12 ,height=5, bg='#ff1744', font=font).grid(row = 4, column=0, columnspan=2)
bot_score = StringVar()
bot_score.set(0)
Label(master, textvariable=bot_score, width=12 ,height=5, bg='#1e88e5', font=font).grid(row = 4, column=1, columnspan=3)

Button(master, text = 'Restart', command=Restart, width=32, bg='#9E9E9E', font=font).grid(row=5, column = 0, columnspan= 3)

master.mainloop()