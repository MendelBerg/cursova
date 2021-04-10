from Interfaces.init import *
from tools import *


def get_arr_notes(func):
    def wrapper():
        with open('../data/notes.txt', 'r') as file:
            return func([
                Notes(
                    *[int(y) if y.strip().isdigit() else y for y in x.split(', ')]
                ) for x in file
            ]
            )
    return wrapper


def sort_data(staff):
    for top in range(1, len(staff)):
        i = top
        while i > 0 and staff[i-1] > staff[i]:
            staff[i], staff[i - 1] = staff[i - 1], staff[i]
            i -= 1

    return staff

@get_arr_notes
def get_units(staff):
    units = sort_data([*set([x.unit for x in staff])])
    print(units)

def show_select(frame):
    menu2 = Frame()
    content = Label(menu2, text="Choose your favourite month")
    menu2.place(relx=0.24, rely=0, relwidth=0.76, relheight=1)
    menu2['bg'] = 'red'
    menu2['width'] = '500'

    def callbackFunc():
        # myLabel = Label(menu2, text=clicked.get()).pack()
        get_units()
    options = [
        'a',
        'b',
        'c'
    ]

    clicked = StringVar()
    clicked.set(options[0])

    drop = OptionMenu(menu2, clicked, *options)
    drop.pack(pady=20)

    btn = Button(menu2, text='select', command=callbackFunc)
    btn.pack(pady=20)

