from tools import *
from tkinter import messagebox
from Interfaces.content.errors import *


def del_note(code, root):
    errors_arr = is_error(code)

    if not errors_arr:
        code = int(code)
        notes = [note for note in get_arr_notes() if note.code != code]

        with open(f"../data/notes.txt", "w") as file:
            for note in notes:
                file.write(', '.join([str(e) for e in note]) + '\n')

        messagebox.showinfo(title='Готово!', message=f'Запис під номером {code} видалено!')
        root.destroy()
    else:
        messagebox.showerror(title='Помилка вводу', message='\n'.join(errors_arr))


def show_del_modal():
    root = Tk()
    root.title("Введіть код")
    entry = Entry(root, width=17)
    entry.pack()
    btn = create_btn(root, 'Видалити', lambda: del_note(entry.get(), root))
    btn.pack(side=LEFT, padx=80, ipadx=10)
    root.mainloop()


def is_error(code):
    errors = []
    not_exists = True

    if code == '':
        errors.append(dict_errors['empty'])
    else:
        if not code.isdigit():
            errors.append(dict_errors['digits'])
        if len(code) != 4:
            errors.append(dict_errors['len'])

    if not errors:
        for note in get_arr_notes():
            if note.code == int(code):
                not_exists = False

        if not_exists:
            errors.append('Працівника із вказаним кодом не існує')

    return errors
