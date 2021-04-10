from collections import namedtuple
from tkinter import *

Notes = namedtuple("Notes", "code name birth_year position unit exp money")


def create_frame_content(title):
    content = Frame()
    label = Label(content, text=title)
    label.pack()
    content.place(relx=0.24, rely=0, relwidth=0.76, relheight=1)
    content['bg'] = 'red'
    content['width'] = '500'

    return [label, content]


def create_btn(frame, text, command):
    return Button(frame, text=text, command=command)


def get_arr_notes():
    with open('../data/notes.txt', 'r') as file:
        return [
            Notes(
                *[int(y) if y.strip().isdigit() else y for y in x.split(', ')]
            ) for x in file
        ]


def sort_arr(staff):
    for top in range(1, len(staff)):
        i = top
        while i > 0 and staff[i - 1] > staff[i]:
            staff[i], staff[i - 1] = staff[i - 1], staff[i]
            i -= 1

    return staff


def get_units():
    return set([x.unit for x in get_arr_notes()])


def filter_by_unit(unit):
    return [worker for worker in get_arr_notes() if worker.unit == unit]
