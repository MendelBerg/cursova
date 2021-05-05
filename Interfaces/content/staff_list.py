from tools import *

label_exists = None


def get_workers_name(unit):
    text_arr = []
    for worker in filter_by_unit(unit):
        text_arr.append(f'{worker.name}.\n\n')

    return ''.join(sort_arr(text_arr)).strip()


def create_select(frame):
    options = sort_arr([*get_units()])

    clicked = StringVar()
    clicked.set(options[0])

    btn = create_btn(frame, 'Обрати',
                     lambda: create_label_names(frame, get_workers_name(clicked.get())))
    btn.pack(anchor=NE, side=RIGHT, padx=5, pady=30)

    drop = OptionMenu(frame, clicked, *options)
    drop['width'] = 10
    drop.pack(anchor=NW, side=LEFT, padx=5, pady=30)


def create_label_names(frame, text):
    global label_exists

    if label_exists:
        label_exists.destroy()

    label_exists = create_label(frame, text)
    label_exists.pack(anchor=SW, pady=80, padx=20)
