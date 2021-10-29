from tkinter import *

root = Tk()
root.title("Nado GUI") 
root.geometry("640x480") # 가로 * 세로 

chkvar = IntVar() # chkvar에 int형으로 저장한다.
chkbox = Checkbutton(root,text="don't show again",variable=chkvar)
# chkbox.select() # 자동 선택 처리
# chkbox.deselect() # 선택 해제 처리
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root,text="do not show until next week",variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get())
    print(chkvar2.get())
btn = Button(root,text='click',command=btncmd)
btn.pack()
root.mainloop()