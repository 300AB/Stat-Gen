import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import random

def Stat(min=0):
    rr = random.randint
    r1 = rr(1,6)
    r2 = rr(1,6)
    r3 = rr(1,6)
    if min != 0:
        print("debug output:",r1,"+",r2,"+",r3, "=", r1+r2+r3)
    return r1+r2+r3

def file_write():
    myFile = open("stat_file.txt", mode="r+")
    print("The content of the file before modification is:")
    text = myFile.read()
    print(text)
    #set each Stat() to Stat(1) to debug and see all d6
    print(Stat(),Stat(),Stat(),Stat(),Stat(),Stat(), file=myFile)
    myFile.close()
    myFile = open("stat_file.txt", "r")
    print("The content of the file after modification is:")
    text = myFile.read()
    print(text)


root = tk.Tk()

canvas = tk.Canvas(root, width=300, height=300)
canvas.grid(columnspan=3, rowspan=3)


#logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = Image
logo_label.grid(column=1,row=0)

#instructions
instructions = tk.Label(root, text="Click for stats output is in stat_file, every click appends more stats", font="Raleway", fg="gray")

instructions.grid(columnspan=3, column=0, row=1)

def button_true():
    browse_text.set("good luck")
    print("hi")
    file_write()

#text box
#text_box = tk.Text(root, height=8, width=16, padx= 15, pady= 15)
#text_box.insert(1.0, list)
#text_box.grid(column=1, row=3)

#button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable= browse_text, command=lambda:button_true(), font="Raleway", bg="black", fg="gray", width=7, height=1)
browse_text.set("Start")
browse_btn.grid(column=1,row= 2)


root.mainloop()
