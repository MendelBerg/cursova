from collections import namedtuple
from tkinter import *

Notes = namedtuple("Notes", "code name birth_year position unit exp money")


def create_frame_content(title):
    menu2 = Frame()
    content = Label(menu2, text=title)
    content.pack()
    menu2.place(relx=0.24, rely=0, relwidth=0.76, relheight=1)
    menu2['bg'] = 'red'
    menu2['width'] = '500'

    return [content, menu2]


def get_input_notes_arr(func):
    def wrapper():
        func([
            Notes(
                input(f'The worker #{_ + 1}\nCode: '),
                input('Name: '),
                input('Birth year: '),
                input('Position: '),
                input('Unit: '),
                input('Experience: '),
                input('Money: ')
            )
            for _ in range(
                int(input('Amount of staff: '))
            )
        ]
        )

    return wrapper


@get_input_notes_arr
def put_data(notes):
    with open(f"data/notes.txt", "a") as file:
        for worker in notes:
            file.write(
                f'{worker.code}, {worker.name}, {worker.birth_year}, {worker.position}, '
                f'{worker.unit}, {worker.exp}, {worker.money}\n'
            )


# def get_arr_notes(func):
#     def wrapper():
#         with open('../data/notes.txt', 'r') as file:
#             return func([
#                     Notes(
#                         *[int(y) if y.strip().isdigit() else y for y in x.split(', ')]
#                     ) for x in file
#                 ]
#             )
#     return wrapper


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
    return set([x.unit for x in get_arr_notes()])


def filter_by_unit(unit):
    return [worker for worker in get_arr_notes() if worker.unit == unit]

# def get_notes_filter(func):
#     @get_arr_notes
#     def wrapper(staff):
#         unit = input('Which unit do you find: ')
#         workers = [worker for worker in staff if worker.unit == unit]
#         notes = workers if len(workers) != 0 else 0
#         return func(notes, unit)
#
#     return wrapper


# @get_notes_filter
# def show_notes_filter(notes):
#     if notes:
#         print(*[worker.name for worker in notes], sep='\n')
#     else:
#         print('Error!\nThis unit does not exist.')


# @get_notes_filter
# def show_middle_age(staff):
#     if not staff:
#         print('Error!\nThis unit does not exist.')
#     else:
#         from datetime import datetime as date
#         print(
#             date.now().year - round(
#                 sum([worker.birth_year for worker in staff]) / len(staff)
#             )
#         )


# @get_arr_notes
# def show_small_exp(staff):
#     min_exp = 0
#     for i in range(1, len(staff)):
#         if staff[min_exp].exp > staff[i].exp:
#             min_exp = i
#
#     print(staff[min_exp].name)
