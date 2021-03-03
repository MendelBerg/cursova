from collections import namedtuple

Notes = namedtuple("Notes", "code name birth_year position unit exp money")


# def put_data():
#     a = []
#     for x in range(int(input('Amount of staff: '))):
#         b = []
#         print(f'The person #{x + 1}:')
#         a.append(b.append(input('Code: '))),
#         a.append(b.append(input('Name: '))),
#         a.append(b.append(input('Birth year: '))),
#         a.append(b.append(input('Position: '))),
#         a.append(b.append(input('Unit: '))),
#         a.append(b.append(input('Experience: '))),
#         a.append(b.append(input('Money: ')))
#         print()
#     with open(f"data/notes.txt", "a") as file:
#         for x in a:
#             file.write(', '.join(x))...


# def input_note():
#     put_data([
#                 Notes(
#                     input(f'\nThe person #{_ + 1}\nCode: '),
#                     input('Name: '),
#                     input('Birth year: '),
#                     input('Position: '),
#                     input('Unit: '),
#                     input('Experience: '),
#                     input('Money: ')
#                 )
#                 for _ in range(
#                     int(input('Amount of staff: '))
#                 )
#             ])

def put_data(staff):
    with open(f"data/notes.txt", "w") as file:
        for worker in staff:
            file.write(
                f'{worker.code}, {worker.name}, {worker.birth_year}, {worker.position}, '
                f'{worker.unit}, {worker.exp}, {worker.money}\n'
            )


def input_note():
    put_data([
        Notes(
            input(f'\nThe person #{_ + 1}\nCode: '),
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
    ])


def get_arr_notes():
    with open('data/notes.txt', 'r') as file:
        return [
            Notes(
                *x.split(', ')[:2],
                int(x.split(', ')[2]),
                *x.split(', ')[3:-2],
                int(x.split(', ')[-2]),
                int(x.split(', ')[-1])
            ) for x in file
        ]


def get_notes_filter(unit, staff):
    workers = [worker for worker in staff if worker.unit == unit]
    return workers if len(workers) != 0 else 0


def show_notes_filter(filtered_notes):
    if filtered_notes:
        print(*[worker.name for worker in filtered_notes], sep='\n')
    else:
        print('Error!\nThis unit does not exists.')


def get_middle_age_staff(staff):
    from datetime import datetime as date
    print(date.now().year - round(sum(
        [
            worker.birth_year for worker in staff
        ]) / len(staff))
          )


# get_middle_age_staff(get_notes_filter('a', get_arr_notes()))


def small_exp(staff):
    for bypass in range(1, len(staff)):
        for i in range(len(staff) - bypass):
            if staff[i].exp > staff[i + 1].exp:
                staff[i], staff[i + 1] = staff[i + 1], staff[i]

    for x in staff[:int(len(staff) * .5)]:
        print(x.exp)


# small_exp(get_arr_notes())
