from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Nado GUI") 
root.geometry("640x480") # 가로 * 세로 

values = [str(i)+'일' for i in range(1,32)] # 1~31 까지의 숫자리스트
combobox = ttk.Combobox(root,height=5,values=values)
combobox.pack()
combobox.set("카드결제일") # 최초 목록 제목 설정

readonly_combobox = ttk.Combobox(root,height=10,values=values,state='readonly') # height 값 10개까지 보여줌 위에거는 5개만 보여줌
readonly_combobox.current(0) # 0번째 인덱스 값 선택
readonly_combobox.pack()
# readonly_combobox.set("카드결제일") # 최초 목록 제목 설정
def btncmd():
    print(combobox.get()) # 선택된 값을 출력
    print(readonly_combobox.get())
    
btn = Button(root,text='choice',command=btncmd)
btn.pack()
root.mainloop()