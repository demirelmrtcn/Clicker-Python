import time, pyautogui, keyboard, threading
from tkinter import *

window = Tk()

#Functions
def clickedStart():
    time.sleep(1)

    run = True
    intervalInt = None

    try:
        intervalInt = int(txt.get())
    except:
        pass
    start = time.time()

    while run == True:

        if keyboard.is_pressed('q'):
            run = False
            break

        if intervalInt != None:
            if time.time() >= (start + intervalInt):
                pyautogui.click()
                start = time.time()
        else:
            pyautogui.click()

window.title("AutoClicker")

lbl = Label(window, text="Click Delay")
lbl.grid(column=1, row=0, padx=(75, 10))

txt = Entry(window, width=10)
txt.grid(column=1, row=1, padx=(75, 10))

btn = Button(window, text="Start Bot", command=clickedStart, bg="green", fg="lightgreen")
btn.grid(column=1, row=2, padx=(75, 10), pady=(15, 10))

window.geometry('250x100')

icon = PhotoImage(file = "appicon.png")
window.iconphoto(False, icon)

txt.focus()
window.mainloop()