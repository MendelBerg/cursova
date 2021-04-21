from tkinter import messagebox
from tools import *

dict_errors = {
    'empty': 'Поле повинно бути заповнене!',
    'digits': 'Поле повинно складатися лише з чисел!',
    'len': 'Поле повинно складатися з чотирьох чисел!',
    'alphabetic': 'Поле має скаладтися лише з літер',
    'full name': 'Ви повинні ввести ПІБ',
    'full fname': 'Ім\'я повинне бути не менше 2-х симовлів',
    'full lname': 'Прізвище повинне бути не менше 2-х симовлів',
    'full father_name': 'По-батькові повинне бути на менше 6-ти символів'
}

errors_messages = {}


def is_empty(notes):
    for note in range(len(notes)):
        if notes[note] == '':
            errors_messages[note].append('empty')


def is_digit(index_arr, notes):
    for note in index_arr:
        if not notes[note].isdigit() and notes[note] != '':
            errors_messages[note].append('digits')


def wrong_len(index_arr, notes):
    for note in index_arr:
        if len(notes[note]) != 4 and notes[note] != '':
            errors_messages[note].append('len')


def is_alpha(index_arr, notes):
    for note in index_arr:
        if not notes[note].replace(' ', '').isalpha() and notes[note] != '':
            errors_messages[note].append('alphabetic')


def check_name(index, notes):
    note = notes[index]
    count = [len(x) for x in note.strip().split(' ')]

    if note != '':
        if len(note.strip().split(' ')) != 3:
            errors_messages[index].append('full name')
        elif note.replace(' ', '').isalpha():
            if count[0] < 2:
                errors_messages[1].append('full lname')
            if count[1] < 2:
                errors_messages[1].append('full fname')
            if count[2] < 6:
                errors_messages[1].append('full father_name')


def find_errors(entries_arr):
    notes = [e.get() for e in entries_arr]
    for i in range(len(notes)):
        errors_messages[i] = []

    is_empty(notes)
    is_digit([0, 2, 5, 6], notes)
    wrong_len([0, 2], notes)
    is_alpha([1, 3, 4], notes)
    check_name(1, notes)

    errors_arr = []
    for field in errors_messages:
        if errors_messages[field]:
            errors_arr.append([f'{labels[field]}:',
                               [dict_errors[error] for error in errors_messages[field]]
                               ])

    return errors_modal(errors_arr) if errors_arr else False


def errors_modal(text):
    root = Tk()
    btn = create_btn(root, 'Ok', lambda: root.destroy())
    btn.pack(side=BOTTOM, padx=90, ipadx=10)
    root.title("Помилка вводу")
    root.geometry('750x470')

    scrollbar = Scrollbar(root, bg='#1A2026')
    scrollbar.pack(side=RIGHT, fill=Y)

    my_list = Listbox(root, yscrollcommand=scrollbar.set, font=f"Georgia 20", bg=content_bg)

    for error in text:
        my_list.insert(END, error[0])
        for line in error[1]:
            my_list.insert(END, line)

        my_list.insert(END, '')

    my_list.pack(side=LEFT, fill=BOTH, ipady=100, ipadx=1000)
    scrollbar.config(command=my_list.yview)

    root.mainloop()
    return True

