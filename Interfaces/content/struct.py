import tkinter.ttk as ttk
from tools import *


class Table(Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)

        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"] = headings
        table["displaycolumns"] = headings

        for head in headings:
            table.heading(head, text=head, anchor=CENTER)
            table.column(head, anchor=CENTER)

        for row in rows:
            table.insert('', END, values=tuple(row))

        scrolltable = Scrollbar(self, bg='#1A2026', command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=RIGHT, fill=Y)
        table.pack(expand=YES, fill=BOTH)


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
    table_struct = Tk()
    table_struct.title("Список працівників")
    table_struct['bg'] = content_bg

    struct_notes = get_struct(0)

    table = Table(table_struct, headings=labels, rows=(
        tuple(struct_notes.values())
    ))
    table.pack(expand=YES, fill=BOTH)
    table_struct.mainloop()



