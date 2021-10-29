from tkinter import *

root = Tk()
root.title("Nado GUI") 
root.geometry("640x480") # 가로 * 세로 

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side='right',fill='y')

# set이 없으면 스크롤을 내려도 다시 올라온다
listbox = Listbox(frame,selectmode='extended',height = 10, yscrollcommand=scrollbar.set)
for i in range(1,32): # 1~31일
    listbox.insert(END,str(i)+"일")
listbox.pack(side='left')

scrollbar.config(command=listbox.yview)

root.mainloop()