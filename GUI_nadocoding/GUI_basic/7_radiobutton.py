from tkinter import *

root = Tk()
root.title("Nado GUI") 
root.geometry("640x480") # 가로 * 세로 

# radio button 
label1 = Label(root,text='select menu').pack()

burger_var = IntVar() # 여기에 인트형으로 값을 저장한다
btn_burger1 = Radiobutton(root,text='ham burger',value=1, variable=burger_var)
btn_burger1.select() # 기본 디폴트값으로 선택이 되어있음
btn_burger2 = Radiobutton(root,text='cheese burger',value=2, variable=burger_var)
btn_burger3 = Radiobutton(root,text='chicken burger',value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

label2 = Label(root,text='select drink').pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text='coke', value='coke', variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text='sprite', value='sprite', variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()

def btncmd():
    print(burger_var.get()) # 햄버거 중 선택된 라디오 항목의 값(value)를 출력
    print(drink_var.get()) # 음료 중 선택된 값(value)을 출력
btn = Button(root,text='order',command=btncmd)
btn.pack()
root.mainloop()