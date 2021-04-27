import tkinter as tk
import tkinter.ttk as ttk
from tools import *

btn = None
table = None
flag = False
table_struct = None


class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)

        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"] = headings
        table["displaycolumns"] = headings

        for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER)

        for row in rows:
            table.insert('', tk.END, values=tuple(row))

        scrolltable = tk.Scrollbar(self, bg='#1A2026', command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)


def get_struct(option):
    dict_text = {}
    i = 0
    for person in sort_dict_arr(get_arr_notes('../'), option):
        dict_text[i] = []
        for data in range(len(person)):
            dict_text[i].append(person[data])
        i += 1
    return dict_text


def show_struct():
    global btn, table, flag
    if btn and table:
        table.destroy()
        btn.destroy()

    if flag:
        struct_notes = get_struct(4)
        flag = False
    else:
        struct_notes = get_struct(0)
        flag = True

    table = Table(table_struct, headings=labels, rows=(
        struct_notes.values()
    ))
    table.pack(expand=tk.YES, fill=tk.BOTH)
    # btn = Button(text='OK', command=lambda: table_struct.destroy())
    # btn.pack()


def f():
    global table_struct
    table_struct = tk.Tk()
    table_struct.title("Список працівників")
    table_struct['bg'] = content_bg
    # Button(text='Сортувати', command=lambda: show_struct()).pack()

    show_struct()

    table_struct.mainloop()

f()
