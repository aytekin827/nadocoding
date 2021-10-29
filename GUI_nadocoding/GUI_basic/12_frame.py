from tkinter import *

root = Tk()
root.title("Nado GUI") 
root.geometry("640x480") # 가로 * 세로 

Label(root,text='select menu').pack(side='top')

Button(root, text='order').pack(side='bottom')
# hamburger example

frame_burger = Frame(root,relief='solid', bd=1)
frame_burger.pack(side='left',fill='both',expand=True)

Button(frame_burger, text='hamburger').pack()
Button(frame_burger, text='cheeseburger').pack()
Button(frame_burger, text='chikenburger').pack()

frame_drink = LabelFrame(root,text='drink')
frame_drink.pack(side='right',fill='both',expand=True)
Button(frame_drink,text='coke').pack()
Button(frame_drink,text='sprite').pack()

root.mainloop()