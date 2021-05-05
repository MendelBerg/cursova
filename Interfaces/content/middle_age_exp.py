from tools import *


def get_small_exp():
    min_exp_staff = []
    min_exp = 0

    for unit in get_units():
        workers = filter_by_unit(unit)
        for i in range(1, len(workers)):
            if workers[min_exp].exp > workers[i].exp:
                min_exp = i

        min_exp_staff.append(workers[min_exp])
        min_exp = 0

    return sort_dict_arr(min_exp_staff, 4)


def get_middle_age():
    from datetime import datetime as date
    middle_age_arr = []

    for unit in get_units():
        workers = filter_by_unit(unit)
        middle_age_arr.append([
            unit,
            date.now().year - round(
                sum([worker.birth_year for worker in workers]) / len(workers)
            )
        ])

    return sort_dict_arr(middle_age_arr, 0)


def fill_content(frame, flag='exp'):
    data = get_middle_age() if flag == 'age' else get_small_exp()
    text_arr = []
    for worker in data:
        year = add_end_year(worker[1] if len(data[0]) == 2 else worker.exp)
        end_of_line = f'"{worker[0]}", {worker[1]} {year}' if len(data[0]) == 2 \
            else f'"{worker.unit}":\n{worker.name} - {worker.exp} {year} стажу'

        text_arr.append(f'Підрозділ ' + end_of_line + '\n\n')

    label = create_label(frame, ''.join(text_arr).strip())
    label.pack(pady=30)


def add_end_year(num):
    return 'рік' if num % 10 == 1 and num != 11 \
        else 'роки' if num % 10 == 2 and num != 12 or \
                       num % 10 == 3 and num != 13 or \
                       num % 10 == 4 and num != 14 \
        else 'років'
