from tkinter import Entry, messagebox, LEFT, RIGHT
from tools import create_btn, create_label


def find_errors(entries_arr):
    notes = [e.get() for e in entries_arr]
    errors_messages = {}
    dict_errors = {
        'digits': 'Код повинен складатися лише з чисел!',
        'len': 'Код повинен складатися з чотирьох чисел!',
        'alphabetic': 'Поле має скаладтися лише з літер',
        'full name': 'Ви повинні ввести ПІБ',
        'full fname': 'Ім\'я повинне бути не менше 2-х симовлів',
        'full lname': 'Прізвище повинне бути не менше 2-х симовлів',
        'full father_name': 'По-батькові повинне бути на менше 6-ти символів'
    }

    for i in dict_errors:
        errors_messages[i] = []

    if '' in notes:
        print('Ви заповнили не всі поля!')

    for note in range(len(notes)):
        if notes[note] != '':
            if note == 0 or note == 2 or note == 5 or note == 6:
                if not notes[note].isdigit():
                    errors_messages['digits'].append(note)
            if note == 0 or note == 2:
                if not notes[note] != 4:
                    errors_messages['len'].append(note)
            if note == 1 or note == 3 or note == 4:
                if not notes[note].replace(' ', '').isalpha():
                    errors_messages['alphabetic'].append(note)

    if notes[1] != '':
        count = [len(x) for x in notes[1].strip().split(' ')]

        if len(notes[1].strip().split(' ')) != 3:
            errors_messages['full name'].append(1)
        else:
            if count[0] < 2:
                errors_messages['full lname'].append(1)
            if count[1] < 2:
                errors_messages['full fname'].append(1)
            if count[2] < 6:
                errors_messages['full father_name'].append(1)

    for x in errors_messages:
        print(f'{x} => \'{errors_messages[x]}\'')


def put_data(entries_arr):
    notes = [e.get() for e in entries_arr]
    find_errors(entries_arr)
    if '' in notes:
        messagebox.showwarning(title='Обережно!', message='Ви заповнили не всі поля!')
    else:
        with open(f"../data/notes.txt", "a") as file:
            file.write(', '.join(notes).strip(', ') + '\n')

        messagebox.showinfo(title='Готово!', message='Дані збережено!')
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
        create_label(frame, text, size=11).pack(pady=5)
        entry = Entry(frame, width=25)
        entry.pack()
        entries_arr.append(entry)

    frm_buttons = create_btn(frame, 'Очистити', lambda: clear_data(entries_arr))
    frm_buttons.pack(side=LEFT, padx=80, ipadx=10)

    btn_submit = create_btn(frame, "Зберегти", lambda: put_data(entries_arr))
    btn_submit.pack(side=RIGHT, padx=80, ipadx=10)
