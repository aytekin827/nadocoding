from tkinter import *

root = Tk()
root.title("Nado GUI") 
root.geometry("640x480") # 가로 * 세로 

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END,'input character')

e = Entry(root,width=30) # enter X
e.pack()
e.insert(0,'only one line possible')


def btncmd():
    # 내용 출력
    print(txt.get('1.0',END)) # txt의 라인 1부터 end까지 가져와라
    print(e.get())

    # 내용 삭제
    txt.delete('1.0',END)
    e.delete(0,END)
btn = Button(root,text='click',command=btncmd)
btn.pack()
root.mainloop()