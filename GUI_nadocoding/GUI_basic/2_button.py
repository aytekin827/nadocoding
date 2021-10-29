from tkinter import *

root = Tk()
root.title("Nado GUI") 

root.geometry("640x480") # 가로 * 세로 

btn1 = Button(root, text="button1")
btn1.pack() # pack을 해줘야지 root객체에 버튼이 들어간다. 

# padx, pady 여백 크기를 설정한다. 상황에 따라 바뀐다
btn2 = Button(root, padx=5, pady=10, text="button2222222") 
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="button3")
btn3.pack()

# width, height 버튼크기를 고정해줌 
btn4 = Button(root, width=10, height=3, text="button444444444444444444") 
btn4.pack()

# 글자 색, 배경화면
btn5 = Button(root, fg="red", bg="yellow", text="button5")
btn5.pack()

# 이미지를 버튼에 넣기
photo = PhotoImage(file='GUI_basic/check.png')
btn6 = Button(root, image=photo)
btn6.pack()

# import sys
# filepath = "C:/Users/Aytekin/Desktop/nadocoding/scraper_nadocoding/web scraping project"
# print(filepath)
# sys.path.append(filepath)
# from . import project

# make button actually alive
def btncmd():
    print("button clicked!")
btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()