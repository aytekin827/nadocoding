from tkinter import *

root = Tk()
root.title("Nado GUI") 
root.geometry("640x480") # 가로 * 세로 

Btn1 = Button(root, text='button 1')
Btn2 = Button(root, text='button 2')

# Btn1.pack()
# Btn2.pack()

# Btn1.pack(side='left')
# Btn2.pack(side='left')

# grid 배치하기
# Btn1.grid(row=0,column=0)
# Btn2.grid(row=1,column=1)

# 애플 키보드 만들어보기
# 맨 윗줄
btn_f16 = Button(root,text='F16', width=5, height=2) # pad 각 버튼의 크기 , width, height 각 버튼의 크기를 설정
btn_f17 = Button(root,text='F17', width=5, height=2)
btn_f18 = Button(root,text='F18', width=5, height=2)
btn_f19 = Button(root,text='F19', width=5, height=2)

btn_f16.grid(row=0,column=0, sticky=N+E+W+S, padx=3, pady=3) # sticky 이게 양 폭을 맞춰줌, grid에서 pad는 버튼간의 간격을 나타냄
btn_f17.grid(row=0,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_f18.grid(row=0,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_f19.grid(row=0,column=3, sticky=N+E+W+S, padx=3, pady=3)

# clear줄
btn_clear = Button(root,text='clear', width=5, height=2)
btn_equal = Button(root,text='=', width=5, height=2)
btn_div = Button(root,text='/', width=5, height=2)
btn_mul = Button(root,text='*', width=5, height=2)

btn_clear.grid(row=1,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_equal.grid(row=1,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_div.grid(row=1,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_mul.grid(row=1,column=3, sticky=N+E+W+S, padx=3, pady=3)

# 7시작 줄
btn_7 = Button(root,text='7', width=5, height=2)
btn_8 = Button(root,text='8', width=5, height=2)
btn_9 = Button(root,text='9', width=5, height=2)
btn_sub = Button(root,text='-', width=5, height=2)

btn_7.grid(row=2,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_8.grid(row=2,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_9.grid(row=2,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_sub.grid(row=2,column=3, sticky=N+E+W+S, padx=3, pady=3)

# 4시작 줄
btn_4 = Button(root,text='4', width=5, height=2)
btn_5 = Button(root,text='5', width=5, height=2)
btn_6 = Button(root,text='6', width=5, height=2)
btn_add = Button(root,text='+', width=5, height=2)

btn_4.grid(row=3,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_5.grid(row=3,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_6.grid(row=3,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_add.grid(row=3,column=3, sticky=N+E+W+S, padx=3, pady=3)

# 1시작 줄
btn_1 = Button(root,text='1', width=5, height=2)
btn_2 = Button(root,text='2', width=5, height=2)
btn_3 = Button(root,text='3', width=5, height=2)
btn_enter = Button(root,text='enter', width=5, height=2)

btn_1.grid(row=4,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_2.grid(row=4,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_3.grid(row=4,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_enter.grid(row=4,column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3) # 현재 위치로부터 아랫줄으로 몇줄을 더함 rowspan = row 2개를 합치겠다는 뜻

# 0시작 줄
btn_0 = Button(root,text='0', width=5, height=2) # 가로로 합쳐짐
btn_point = Button(root,text='.', width=5, height=2)

btn_0.grid(row=5, column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3) # columnspan 현재 위치로부터 오른쪽으로 몇줄을 더함.
btn_point.grid(row=5,column=2, sticky=N+E+W+S, padx=3, pady=3)



root.mainloop()