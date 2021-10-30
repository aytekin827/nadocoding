from tkinter import *
import os 

root = Tk()
root.title("제목 없음 - Windows 메모장") 
root.geometry("640x480") # 가로 * 세로 

# frame = Frame(root)
# frame.pack()

# 스크롤바
scrollbar = Scrollbar(root)
scrollbar.pack(side='right',fill='y')

# 본문영역
text = Text(root,relief='flat',yscrollcommand=scrollbar.set)
text.pack(fill='both', expand=True, side='left')

scrollbar.config(command=text.yview)

# 열기, 저장 파일 이름
filename = 'mynote.txt'

# 메뉴
menu = Menu(root)
def read_file():
    if os.path.isfile(filename): # 파일 있으면 True, 없으면 False
        with open(filename,'r', encoding='utf-8') as f:
            text.delete('1.0',END) # 텍스트 위젯 본문 삭제
            text.insert(END,f.read()) # 파일 내용을 본문에 입력

def save_file():
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text.get('1.0',END))

# 메뉴 - 파일(F)
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label='열기',command=read_file)
menu_file.add_command(label='저장',command=save_file)
menu_file.add_separator()
menu_file.add_command(label='끝내기',command=root.quit)

menu.add_cascade(label='파일(F)',menu=menu_file)
menu.add_cascade(label='편집(E)')
menu.add_cascade(label='서식(O)')
menu.add_cascade(label='보기(V)')
menu.add_cascade(label='도움말(H)')

root.config(menu=menu)

root.mainloop()