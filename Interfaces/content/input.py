from tkinter import (Label, Entry, messagebox,
                     LEFT, RIGHT)
from tools import create_btn


def put_data(entries_arr):
    notes = [e.get() for e in entries_arr]
    if '' in notes:
        messagebox.showwarning(title='Обережно!', message='Ви заповнили не всі поля!')
    else:
        with open(f"../data/notes.txt", "a") as file:
            file.write(', '.join(notes).strip(', ') + '\n')

        messagebox.showinfo(title='Title', message='Дані збережено!')
        clear_data(entries_arr)


def clear_data(entries_arr):
    for entry in entries_arr:
        entry.delete(0, 'end')

    entries_arr[0].focus_set()


def create_input(frame):
    labels = ["Код:", "ПІБ:", "Рік народження:", "Посада:",
              "Підрозділ", "Досвід роботи (в роках)", "Зарплатня"]

    entries_arr = []
    for text in labels:
        Label(master=frame, text=text).pack(pady=5)
        entry = Entry(frame, width=25)
        entry.pack()
        entries_arr.append(entry)

    frm_buttons = create_btn(frame, 'Clear', lambda: clear_data(entries_arr))
    frm_buttons.pack(side=LEFT, padx=80, ipadx=10)

    btn_submit = create_btn(frame, "Submit", lambda: put_data(entries_arr))
    btn_submit.pack(side=RIGHT, padx=80, ipadx=10)
