from tkinter import *
from typing import ChainMap

root = Tk()
root.title("Nado GUI") 

root.geometry("640x480") # 가로 * 세로 

label1 = Label(root, text="hello label")
label1.pack()

photo = PhotoImage(file="GUI_basic/check.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text='see you again')
    
    global photo2 # garbage collection에 걸리지 않도록 하기 위해서 전역변수로 설정해야 한다.
    photo2 = PhotoImage(file='GUI_basic/redx.png')
    label2.config(image=photo2)

btn = Button(root, text='click' ,command=change)
btn.pack()

root.mainloop()