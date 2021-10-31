from tkinter import *
from project import scrape_IT_news,scrape_news,scrape_weather,eng_today_conv

root = Tk()
root.title("Secretary") 
root.geometry("640x480")

# 오늘의 정보 불러오는 프레임
todayinfo_frame = LabelFrame(root,text='비서버튼')
todayinfo_frame.pack(padx=5,pady=5, ipady=5, ipadx=5)

def secretary():
    text.delete('1.0',END)
    text.insert(END,'[오늘의 날씨]\n')
    for i in scrape_weather():
        text.insert(END,i)
        text.insert(END,'\n')
    text.insert(END,'\n')

    text.insert(END, '[헤드라인 뉴스]\n')
    for i in scrape_news():
        text.insert(END,i)
        text.insert(END,'\n')
    text.insert(END,'\n')

    text.insert(END, '[IT 뉴스]\n')
    for i in scrape_news():
        text.insert(END,i)
        text.insert(END,'\n')
    text.insert(END,'\n')

    text.insert(END, '[오늘의 영어 회화]\n')
    eng_today = eng_today_conv()
    text.insert(END,eng_today[0])
    text.insert(END, '\n(영어 지문)\n')

    for i in eng_today[1]:
        text.insert(END,i)
        text.insert(END,'\n')
    text.insert(END,'\n')

    text.insert(END, '\n(한글 지문)\n')

    for i in eng_today[2]:
        text.insert(END,i)
        text.insert(END,'\n')
    text.insert(END,'\n')

btn_info = Button(todayinfo_frame,text='호출',command=secretary)
btn_info.pack()

# 오늘의 정보 출력하는 프레임
text_frame = LabelFrame(root,text='오늘의 정보')
text_frame.pack(fill='both',padx=5,pady=5, ipady=5)

scrollbar = Scrollbar(text_frame)
scrollbar.pack(side='right',fill='y')

text = Text(text_frame,relief='flat',yscrollcommand=scrollbar.set)
text.pack(fill='both',side='left',expand=True)

scrollbar.config(command=text.yview)

root.resizable(False,False)
root.mainloop()