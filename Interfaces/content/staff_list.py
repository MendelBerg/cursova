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

    return ''.join(sort_data(text_arr)).strip()


label_exists = None


def show_select(frame):

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

    label_exists = Label(frame)
    label_exists['text'] = text
    label_exists.pack()
