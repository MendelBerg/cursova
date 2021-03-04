from collections import namedtuple

Notes = namedtuple("Notes", "code name birth_year position unit exp money")


def get_input_notes_arr():
    return [
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


def put_data():
    with open(f"data/notes.txt", "a") as file:
        for worker in get_input_notes_arr():
            file.write(
                f'{worker.code}, {worker.name}, {worker.birth_year}, {worker.position}, '
                f'{worker.unit}, {worker.exp}, {worker.money}\n'
            )


def get_arr_notes(func):
    def wrapper():
        with open('data/notes.txt', 'r') as file:
            staff = [
                Notes(
                    *x.split(', ')[:2],
                    int(x.split(', ')[2]),
                    *x.split(', ')[3:-2],
                    int(x.split(', ')[-2]),
                    int(x.split(', ')[-1])
                ) for x in file
            ]
        return func(staff)

    return wrapper


def get_notes_filter(func):
    @get_arr_notes
    def wrapper(staff):
        unit = input('Which unit do you find: ')
        workers = [worker for worker in staff if worker.unit == unit]
        notes = workers if len(workers) != 0 else 0
        return func(notes)

    return wrapper


@get_notes_filter
def show_notes_filter(notes):
    if notes:
        print(*[worker.name for worker in notes], sep='\n')
    else:
        print('Error!\nThis unit does not exists.')


@get_notes_filter
def get_middle_age_staff(staff):
    from datetime import datetime as date
    print(
        date.now().year - round(
            sum([worker.birth_year for worker in staff]) / len(staff)
        )
    )


@get_arr_notes
def show_small_exp(staff):
    for bypass in range(1, len(staff)):
        for i in range(len(staff) - bypass):
            if staff[i].exp > staff[i + 1].exp:
                staff[i], staff[i + 1] = staff[i + 1], staff[i]

    for x in staff[:int(len(staff) * .5)]:  # only 50% of staff
        print(x.name)
