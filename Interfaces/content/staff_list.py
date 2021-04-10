from tools import *

label_exists = None


def get_workers_name(unit):
    workers = [worker for worker in get_arr_notes() if worker.unit == unit]
    text_arr = []
    for worker in workers:
        text_arr.append(f'{worker.name}.\n')

    return ''.join(sort_data(text_arr)).strip()


def create_select(frame):
    options = get_units()

    clicked = StringVar()
    clicked.set(options[0])

    drop = OptionMenu(frame, clicked, *options)
    drop.pack(pady=20)

    btn = Button(frame, text='select',
                 command=lambda: create_label(frame, get_workers_name(clicked.get())))
    btn.pack(pady=20)


def create_label(frame, text):
    global label_exists

    if label_exists:
        label_exists.destroy()

    label_exists = Label(frame, text=text)
    label_exists.pack()
