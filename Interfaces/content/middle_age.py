from tools import *
from datetime import datetime as date


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
def show_middle_age(staff):
    units = set([x.unit for x in staff])
    middle_age_arr = []

    for unit in units:
        workers_by_unit = [worker for worker in staff if worker.unit == unit]
        middle_age_arr.append(
            {'unit': unit, "years":
                date.now().year - round(
                    sum([worker.birth_year for worker in workers_by_unit]) / len(workers_by_unit)
                )}
        )

    return sort_data(middle_age_arr)


def sort_data(arr):
    for top in range(1, len(arr)):
        i = top
        while i > 0 and arr[i - 1]["unit"] > arr[i]["unit"]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
    return arr
