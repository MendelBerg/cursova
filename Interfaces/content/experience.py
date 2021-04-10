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


@get_arr_notes
def show_small_exp(staff):
    units = set([x.unit for x in staff])
    min_exp_staff = []
    min_exp = 0
    for unit in units:
        workers_by_unit = [worker for worker in staff if worker.unit == unit]

        for i in range(1, len(workers_by_unit)):
            if workers_by_unit[min_exp].exp > workers_by_unit[i].exp:
                min_exp = i

        min_exp_staff.append([workers_by_unit[min_exp].unit, workers_by_unit[min_exp].exp, workers_by_unit[min_exp].name])
        min_exp = 0

    return sort_data(min_exp_staff)


def sort_data(staff):
    for top in range(1, len(staff)):
        i = top
        while i > 0 and staff[i - 1][2] > staff[i][2]:
            staff[i], staff[i - 1] = staff[i - 1], staff[i]
            i -= 1

    return staff


