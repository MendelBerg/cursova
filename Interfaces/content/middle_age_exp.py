from tools import *


def show_small_exp():
    min_exp_staff = []
    min_exp = 0

    for unit in get_units():
        workers = filter_by_unit(unit)
        for i in range(1, len(workers)):
            if workers[min_exp].exp > workers[i].exp:
                min_exp = i

        worker = workers[min_exp]
        min_exp_staff.append({'name': worker.name, 'unit': worker.unit, 'years': worker.exp})
        min_exp = 0

    return sort_data_it(min_exp_staff, 'name')


def show_middle_age():
    from datetime import datetime as date
    middle_age_arr = []

    for unit in get_units():
        workers = filter_by_unit(unit)
        middle_age_arr.append({
            'unit': unit,
            "years": date.now().year - round(
                sum([worker.birth_year for worker in workers]) / len(workers)
            )
        })

    return sort_data_it(middle_age_arr, 'unit')


def sort_data_it(staff, key):
    for top in range(1, len(staff)):
        i = top
        while i > 0 and staff[i - 1][key] > staff[i][key]:
            staff[i], staff[i - 1] = staff[i - 1], staff[i]
            i -= 1
    return staff
