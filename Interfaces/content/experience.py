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

    return sort_data(min_exp_staff)


def sort_data(staff):
    for top in range(1, len(staff)):
        i = top
        while i > 0 and staff[i - 1]['name'] > staff[i]['name']:
            staff[i], staff[i - 1] = staff[i - 1], staff[i]
            i -= 1

    return staff
