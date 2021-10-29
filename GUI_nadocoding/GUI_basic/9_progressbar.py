import time
from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Nado GUI") 
root.geometry("640x480") # 가로 * 세로 

# progresbar = ttk.Progressbar(root, maximum=100, mode='indeterminate') # indeterminate 왔다갔다 함 progressbar가
# progresbar = ttk.Progressbar(root, maximum=100, mode='determinate') 
# progresbar.start(10) # 10ms 마다 움직임 
# progresbar.pack()

# def btncmd():
#     progresbar.stop() # 작동 중지
    
# btn = Button(root,text='stop',command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1,101): # 1~100까지
        time.sleep(0.01) # 0.01초 대기

        p_var2.set(i) # progressbar 값 설정
        progressbar2.update() # ui 업데이트
        print(p_var2.get())
btn = Button(root,text='start',command=btncmd2)
btn.pack()

root.mainloop()