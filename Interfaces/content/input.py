from tkinter import messagebox

from Interfaces.init import *


def create_input():
    menu2 = Frame()
    content = Label(menu2, text='Put data')
    content.grid(row=0, column=3, sticky="nsew")
    content.pack()
    menu2.place(relx=0.24, rely=0, relwidth=0.76, relheight=1)
    menu2['bg'] = 'red'
    menu2['width'] = '500'

    labels = [
        "Код:",
        "Имя:",
        "Рік народження:",
        "Посада:",
        "Підрозділ",
        "Досвід роботи (в роках)",
        "Зарплатня",
    ]

    entries_arr = []
    for text in labels:
        Label(master=menu2, text=text).pack(pady=5)
        entry = Entry(menu2, width=25)
        entry.pack()
        entries_arr.append(entry)

    frm_buttons = Button(menu2, text='Clear', command=lambda: clear_data(entries_arr))
    frm_buttons.pack(side=LEFT, padx=80, ipadx=10)

    btn_submit = Button(menu2, text="Submit", command=lambda: put_data(entries_arr))
    btn_submit.pack(side=RIGHT, padx=80, ipadx=10)


def put_data(entries_arr):
    notes = [e.get() for e in entries_arr]
    if '' in notes:
        messagebox.showwarning(title='Обережно!', message='Ви заповнили не всы поля!')
    else:
        with open(f"../data/notes.txt", "a") as file:
            file.write(', '.join(notes).strip(', ') + '\n')

        messagebox.showinfo(title='Title', message='Данні збереглися!')
        clear_data(entries_arr)


def clear_data(entries_arr):
    for entry in entries_arr:
        entry.delete(0, 'end')

    entries_arr[0].focus_set()
