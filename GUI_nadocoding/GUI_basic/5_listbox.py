from tkinter import *

root = Tk()
root.title("Nado GUI") 
root.geometry("640x480") # 가로 * 세로 

listbox = Listbox(root,selectmode='extended',height=0) # selectmode = single도 있다.
listbox.insert(0,'apple')
listbox.insert(1,'banana')
listbox.insert(2,'strawberry')
listbox.insert(END,'watermelon')
listbox.insert(END,'grape')
listbox.pack()



def btncmd():
    # 삭제
    # listbox.delete(END) # 맨 뒤 삭제
    # listbox.delete(0) # 맨 앞 삭제

    # 갯수 확인
    print('there are ',listbox.size(),'in this list')

    # 항목 확인 get(start idx, end idx)
    print('from first to third : ',listbox.get(0,2))

    # 선택된 항목 확인(return index value ex_(1,2,3))
    print("selected item :", listbox.curselection())
btn = Button(root,text='click',command=btncmd)
btn.pack()
root.mainloop()