from tools import *

label_exists = None


def get_workers_name(unit):
    text_arr = []
    for worker in filter_by_unit(unit):
        text_arr.append(f'{worker.name}.\n')

    return ''.join(sort_arr(text_arr)).strip()


def create_select(frame):
    options = sort_arr([*get_units()])

    clicked = StringVar()
    clicked.set(options[0])

    drop = OptionMenu(frame, clicked, *options)
    drop.pack(anchor=NW, side=LEFT)

    btn = create_btn(frame, 'select',
                     lambda: create_label(frame, get_workers_name(clicked.get())))
    btn.pack(anchor=NE)


def create_label(frame, text):
    global label_exists

    if label_exists:
        label_exists.destroy()

    label_exists = Label(frame, text=text, bg=content_bg, font='Georgia')
    label_exists.pack()
