from tkinter import *
import math
from winsound import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Verdana"
WORK_MIN = 0.5
SHORT_BREAK_MIN = 0.5
LONG_BREAK_MIN = 0.5
reps = 0
checks = ""
counter = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    window.after_cancel(counter)
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0
    title.config(text="Timer", fg=GREEN)
    print("reset")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    global title
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        what = WORK_MIN
        title.config(text="WORK!!!", fg=RED)

        def play_work():
            return PlaySound("work.wav", SND_FILENAME)

        play_work()

    elif reps == 2 or reps == 4 or reps == 6:
        what = SHORT_BREAK_MIN
        title.config(text="SHORT BREAK", fg=GREEN)

        def play_lavirginia():
            return PlaySound("lavirginia.wav", SND_FILENAME)

        play_lavirginia()

    else:
        what = LONG_BREAK_MIN
        title.config(text="LONG BREAK", fg=PINK)

        def play_lickitup():
            return PlaySound("lickitup.wav", SND_FILENAME)

        play_lickitup()

    count_down(what * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    # print(count)
    if count > 0:
        global counter
        counter = window.after(1000, count_down, count -1)
    else:
        start_timer()
        if reps % 2 == 0:
            global checks
            checks = checks + "✔"

            check_mark.config(text=checks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Tomate
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_png)
timer_text = canvas.create_text(100, 112, text= "00:00", fill="white", font=(FONT_NAME, 35, "normal"))
canvas.grid(column=1, row=1)



#check marks Label
check_mark = Label(font=(FONT_NAME, 25, "normal"))
check_mark.config(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

#Timer Label
title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
title.grid(column=1, row=0)


#Start Button

#calls action() when pressed
button_start = Button(text="start", command=start_timer)
button_start.grid(column=0, row=2)

#Reset Button



button_reset = Button(text="reset", command=reset)
button_reset.grid(column=2, row=2)



window.mainloop()