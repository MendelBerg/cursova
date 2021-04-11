from tools import *


def get_small_exp():
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

    return sort_dict_arr(min_exp_staff)


def get_middle_age():
    from datetime import datetime as date
    middle_age_arr = []

    for unit in get_units():
        workers = filter_by_unit(unit)
        middle_age_arr.append({
            'unit': unit,
            'years': date.now().year - round(
                sum([worker.birth_year for worker in workers]) / len(workers)
            )
        })

    return sort_dict_arr(middle_age_arr)


def sort_dict_arr(staff):
    for top in range(1, len(staff)):
        i = top
        while i > 0 and staff[i - 1]['unit'] > staff[i]['unit']:
            staff[i], staff[i - 1] = staff[i - 1], staff[i]
            i -= 1
    return staff


def fill_content(frame, flag='exp'):
    data = get_middle_age() if flag == 'age' else get_small_exp()
    text_arr = []
    for worker in data:
        year = add_end_year(worker['years'])
        end_of_line = f'{worker["years"]} {year}' if len(data[0]) == 2 \
            else f'{worker["name"]} - {worker["years"]} {year} стажу'

        text_arr.append(f'Підрозділ "{worker["unit"]}", ' + end_of_line + '.\n\n')

    label = create_label(frame, ''.join(text_arr).strip())
    label.pack(pady=30)


def add_end_year(num):
    return 'рік' if num % 10 == 1 and num != 11 \
        else 'роки' if num % 10 == 2 and num != 12 or \
                       num % 10 == 3 and num != 13 or \
                       num % 10 == 4 and num != 14 \
        else 'років'
