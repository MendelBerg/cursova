from tkinter import Entry, LEFT, RIGHT
from tools import create_btn, create_label
from Interfaces.content.errors import *


def put_data(entries_arr):
    notes = [e.get() for e in entries_arr]

    if not find_errors(entries_arr):
        with open(f"../data/notes.txt", "a") as file:
            file.write(', '.join(notes).strip(', ') + '\n')

        messagebox.showinfo(title='Готово!', message='Дані збережено!')
        clear_data(entries_arr)


def clear_data(entries_arr):
    for entry in entries_arr:
        entry.delete(0, 'end')

    entries_arr[0].focus_set()


def create_input(frame):
    entries_arr = []
    for text in labels:
        create_label(frame, text, size=11).pack(pady=5)
        entry = Entry(frame, width=25)
        entry.pack()
        entries_arr.append(entry)

    frm_buttons = create_btn(frame, 'Очистити', lambda: clear_data(entries_arr))
    frm_buttons.pack(side=LEFT, padx=80, ipadx=10)

    btn_submit = create_btn(frame, "Зберегти", lambda: put_data(entries_arr))
    btn_submit.pack(side=RIGHT, padx=80, ipadx=10)
