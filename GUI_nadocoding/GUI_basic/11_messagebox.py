from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()
root.title("Nado GUI") 
root.geometry("640x480") # 가로 * 세로 

# example) train reservation system
def info():
    msgbox.showinfo('Alert','Reservation Completed!')

def warn():
    msgbox.showwarning('Warning','selected seat already reserved')

def error():
    msgbox.showerror('Error','Payment error occured')

def okcancel():
    msgbox.askokcancel('OK / Cancel','The seat you have selected is with kid. do you want to continue?')

def retrycancel():
    response = msgbox.askretrycancel('Retry / Cancel','temporary error has occured. try again?')
    print('response :',response) # True, False, None => 예, 아니오, 취소
    if response == 1: # 재시도
        print('재시도')
    elif response == 0: # 취소
        print("취소")

def yesno():
    msgbox.askyesno('Yes / No','The seat you have choosen is reverse ticket. Do you want to continue?')

def yesnocancel():
    response = msgbox.askyesnocancel(title=None,message='reservation information did not saved yet.\ndo you want save it and exit?')
    # 예 : 저장 후 종료
    # 아니오 : 저장하지 않고 종료
    # 취소 : 프로그램 종료 취소(해당 화면에서 계속 작업)
    print('response :',response) # True, False, None => 예, 아니오, 취소
    if response == 1:
        print('Yes')
    elif response == 0:
        print("No")
    else:
        print('Cancel')
Button(root,command=info, text='Alarm').pack()
Button(root,command=warn, text='Warning').pack()
Button(root,command=error, text='Error').pack()

Button(root,command=okcancel, text='OK Cancel').pack()
Button(root,command=retrycancel, text='Retry').pack()
Button(root,command=yesno, text='Yes No').pack()
Button(root,command=yesnocancel, text='Yes No Cancel').pack()



root.mainloop()