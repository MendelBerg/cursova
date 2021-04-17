from tkinter import Entry, messagebox, LEFT, RIGHT
from tools import create_btn, create_label

labels = ["Код", "ПІБ", "Рік народження", "Посада",
          "Підрозділ", "Досвід роботи (в роках)", "Зарплатня"]


def find_errors(entries_arr):
    notes = [e.get() for e in entries_arr]
    errors_messages = {}
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

    for i in range(len(notes)):
        errors_messages[i] = []

    for note in range(len(notes)):
        if notes[note] == '':
            errors_messages[note].append('empty')

    for note in range(len(notes)):
        if notes[note] != '':
            if note == 0 or note == 2 or note == 5 or note == 6:
                if not notes[note].isdigit():
                    errors_messages[note].append('digits')
            if note == 0 or note == 2:
                if len(notes[note]) != 4:
                    errors_messages[note].append('len')
            if note == 1 or note == 3 or note == 4:
                if not notes[note].replace(' ', '').isalpha():
                    errors_messages[note].append('alphabetic')

    if notes[1] != '':
        count = [len(x) for x in notes[1].strip().split(' ')]

        if len(notes[1].strip().split(' ')) != 3:
            errors_messages[1].append('full name')
        elif notes[1].replace(' ', '').isalpha():
            if count[0] < 2:
                errors_messages[1].append('full lname')
            if count[1] < 2:
                errors_messages[1].append('full fname')
            if count[2] < 6:
                errors_messages[1].append('full father_name')

    errors_text = ''
    for field in errors_messages:
        if errors_messages[field]:
            errors_text += f'{labels[field]}:' + '\n' + \
                           '\n'.join([dict_errors[error] for error in errors_messages[field]]) + \
                           '\n\n'

    return messagebox.showwarning(title='Обережно!', message=errors_text) if errors_text else False


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
