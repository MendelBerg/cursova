from Interfaces.init import *
from tools import *


def get_arr_notes():
    with open('../data/notes.txt', 'r') as file:
        return [
            Notes(
                *[int(y) if y.strip().isdigit() else y for y in x.split(', ')]
            ) for x in file
        ]


def sort_data(staff):
    for top in range(1, len(staff)):
        i = top
        while i > 0 and staff[i - 1] > staff[i]:
            staff[i], staff[i - 1] = staff[i - 1], staff[i]
            i -= 1

    return staff


def get_units():
    return sort_data([*set([x.unit for x in get_arr_notes()])])


def get_workers_name(click):
    workers = [worker for worker in get_arr_notes() if worker.unit == click]
    text_arr = []
    for worker in workers:
        text_arr.append(f'{worker.name}.\n')

    return [''.join(sort_data(text_arr)).strip(), click]

    # myLabel = Label(frame)
    # myLabel['text'] = ''.join(sort_data(text_arr)).strip()
    # myLabel.pack()





def show_select():
    menu2 = Frame()
    content = Label(menu2, text='Choose unit')
    content.pack()

    menu2.place(relx=0.24, rely=0, relwidth=0.76, relheight=1)
    menu2['bg'] = 'red'
    menu2['width'] = '500'

    options = get_units()

    clicked = StringVar()
    clicked.set(options[0])

    drop = OptionMenu(menu2, clicked, *options)
    drop.pack(pady=20)

    btn = Button(menu2, text='select', command=lambda: create_label(menu2, *get_workers_name(clicked.get())))
    btn.pack(pady=20)




def create_label(frame, text, click):
    myLabel = Label(frame)
    myLabel['text'] = text
    myLabel.pack()
