from tools import *
from datetime import datetime as date


def show_middle_age():
    middle_age_arr = []

    for unit in get_units():
        workers = filter_by_unit(unit)
        middle_age_arr.append(
            {'unit': unit,
             "years": date.now().year - round(
                 sum([worker.birth_year for worker in workers]) / len(workers)
             )
             }
        )

    return sort_data(middle_age_arr)


def sort_data(arr):
    for top in range(1, len(arr)):
        i = top
        while i > 0 and arr[i - 1]["unit"] > arr[i]["unit"]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
    return arr
