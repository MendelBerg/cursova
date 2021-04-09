from tkinter import *
from tkinter import messagebox

root = Tk()


def btn_click():
    login = loginInput.get()
    password = passField.get()
    info_str = f'Data: {str(login)}, {str(password)}'
    messagebox.showinfo(title='Title', message=info_str)
    messagebox.showerror(title='', message='Error')


root['bg'] = 'blue'
root.title('Cursova Interface')
root.geometry('300x250')

root.resizable(width=False, height=False)

canvas = Canvas(root, height=300, width=250)
canvas.pack()

frame = Frame(root, bg='gray')
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

title = Label(frame, text='Text', bg='yellow', font=40)
title.pack()
btn = Button(frame, text='Button', bg='brown', command=btn_click, style='W.TButton')
btn.pack()

loginInput = Entry(frame, bg='white')
loginInput.pack()

passField = Entry(frame, bg='white', show='*')
passField.pack()

root.mainloop()
