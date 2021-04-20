from tools import *
from tkinter import messagebox


def del_note(code):
    notes = [note for note in get_arr_notes() if note.code != code]

    with open(f"../data/notes.txt", "w") as file:
        for note in notes:
            file.write(', '.join([str(e) for e in note]) + '\n')

    messagebox.showinfo(title='Готово!', message='Дані збережено!')


def show_del_modal():
    root = Tk()
    entry = Entry(root, width=17)
    entry.pack()
    btn = create_btn(root, 'Видалити', lambda: del_note(int(entry.get())))
    btn.pack(side=LEFT, padx=80, ipadx=10)
    root.mainloop()
