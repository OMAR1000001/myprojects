from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
eWord={}
learn={}

try:
    data=pandas.read_csv("data/known_words.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/Arabic+English.csv.csv")
    learn = original_data.to_dict(orient="records")
else:
    learn=data.to_dict(orient="records")

def next_card():
    global eWord,flip_after
    window.after_cancel(flip_after)
    eWord=random.choice(learn)
    canves.itemconfig(title_card,text="English",fill="black")
    canves.itemconfig(word_card,text=eWord['English'],fill="black")
    canves.itemconfig(card_front,image=front_img)
    flip_after=window.after(3000, flip_card)


def flip_card():
    canves.itemconfig(title_card,text="العربيه",fill="white")
    canves.itemconfig(word_card,text=eWord["العربيه"],fill="white")
    canves.itemconfig(card_front,image=back_img)
def is_learn():
    learn.remove(eWord)
    data=pandas.DataFrame(learn)
    data.to_csv("data/known_words.csv",index=False)
    next_card()


window =Tk()
window.title("flashy")
window.config(padx=50,pady=50,bg= BACKGROUND_COLOR)

flip_after=window.after(3000,flip_card)

canves=Canvas(width=800,height=528)
front_img=PhotoImage(file="images/card_front.png")
back_img=PhotoImage(file="images/card_back.png")
card_front=canves.create_image(400,263,image=front_img)
title_card=canves.create_text(400,150,text="title",font=("Ariel",40,"italic"))
word_card=canves.create_text(400,263,text="word",font=("Ariel",60,"bold"))

canves.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canves.grid(row=0,column=0,columnspan=2)

wrong_img=PhotoImage(file="images/wrong.png")
unknowen_button=Button(image=wrong_img,bg=BACKGROUND_COLOR,highlightthickness=0,command= flip_card)
unknowen_button.grid(row=1,column=0)

right_img=PhotoImage(file="images/right.png")
knowen_button=Button(image=right_img,bg=BACKGROUND_COLOR,highlightthickness=0,command=is_learn)
knowen_button.grid(row=1,column=1)











next_card()

window.mainloop()