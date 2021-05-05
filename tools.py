from collections import namedtuple
from tkinter import *

Notes = namedtuple("Notes", "code name birth_year position unit exp money")
content_bg = '#D5D5D5'
font_title = 18

labels = ["Код", "ПІБ", "Рік народження", "Посада",
          "Підрозділ", "Досвід роботи (в роках)", "Зарплатня ($)"]


def create_frame_content(title, size=font_title):
    content = Frame()
    label = create_label(content, title, "#1A2026", size, 'bold')
    label.pack()
    content.place(relx=0.24, rely=0, relwidth=0.76, relheight=1)
    content['bg'] = content_bg
    content['width'] = '500'

    return {'label': label, 'frame': content}


def create_btn(frame, text, command, bg=content_bg):
    return Button(frame, text=text, command=command, bg=bg)


def create_label(frame, text, clr='#000', size=14, weight='normal'):
    return Label(frame, text=text, bg=content_bg, font=f"Georgia {size} {weight}", fg=clr)


def get_arr_notes(path='../'):
    with open(f'{path}data/notes.txt', 'r') as file:
        return [
            Notes(
                *[int(y) if y.strip().isdigit() else y.title() for y in x.split(', ')]
            ) for x in file
        ]


def sort_arr(staff):
    for top in range(1, len(staff)):
        i = top
        while i > 0 and staff[i - 1] > staff[i]:
            staff[i], staff[i - 1] = staff[i - 1], staff[i]
            i -= 1

    return staff


def sort_dict_arr(staff, key):
    for top in range(1, len(staff)):
        i = top
        while i > 0 and staff[i - 1][key] > staff[i][key]:
            staff[i], staff[i - 1] = staff[i - 1], staff[i]
            i -= 1
    return staff


def get_units():
    return set([x.unit for x in get_arr_notes()])


def filter_by_unit(unit):
    return [worker for worker in get_arr_notes() if worker.unit == unit]
