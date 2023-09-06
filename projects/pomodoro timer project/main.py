from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    counter(25*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def counter(count):
    min_cou = math.floor(count/60)
    sec_cou =count % 60
    if sec_cou < 10:
        sec_cou=f"0{sec_cou}"

    canv.itemconfig(timer,text=f"{min_cou}:{sec_cou}")
    if count != 0:
        window.after(1000,counter, count-1)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Ponodoro")
window.config(padx=100,pady=50,bg=YELLOW)


title=Label(text="Timer",font=(FONT_NAME,35,"bold"),fg=GREEN,bg=YELLOW)
title.grid(row=1,column=2)

mark=Label(text="🗹",font=(FONT_NAME,20,"bold"),fg=GREEN,bg=YELLOW)
mark.grid(row=4,column=2)

canv=Canvas(width=205,height=224,bg=YELLOW,highlightthickness=0)
tmatm_img=PhotoImage(file="tomato.png")
canv.create_image(103,112,image=tmatm_img)
timer=canv.create_text(103,130,text="",fill="white",font=(FONT_NAME,24,"bold"))
canv.grid(row=2,column=2)


start_button =Button(text="start",command=start_timer)
start_button.grid(row=3,column=1)

reset_button =Button(text="reset")
reset_button.grid(row=3,column=3)




window.mainloop()