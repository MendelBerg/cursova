from collections import namedtuple

Notes = namedtuple("Notes", "code name position subcharpet exp money")


def put_data(staff):
    with open(f"data/notes.txt", "w") as file:
        for worker in staff:
            file.write(
                f'{worker.code}, {worker.name}, {worker.position}, '
                f'{worker.subcharpet}, {worker.exp}, {worker.money}\n'
            )


def input_note():
    put_data([
                Notes(
                    input(f'\nThe person #{_ + 1}\nCode: '),
                    input('Name: '),
                    input('Position: '),
                    input('Subcharpet: '),
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
                        code=worker[0],
                        name=worker[1],
                        position=worker[2],
                        subcharpet=worker[3],
                        exp=worker[4],
                        money=int(worker[5].replace('\n', ''))
                    )
                    for worker in [
                        file.readline().split(', ')
                        for _ in range(
                            sum(1 for _ in open(f'data/notes.txt', 'r'))
                        )
                    ]
                ]


def get_notes_filter(subcharpet):
    workers = [worker for worker in get_arr_notes() if worker.subcharpet == subcharpet]
    return workers if len(workers) != 0 else 0


def show_notes_filter(filtered_notes):
    if filtered_notes:
        print(*[worker.name for worker in filtered_notes], sep='\n')
    else:
        print('Error!\nThis subcharpet does not exists.')


# you need to put 'year' into Notes to working this func!!!
def get_middle_age_staff(staff):
    from datetime import datetime as date
    return date.now().year - sum([worker.year for worker in staff]) / len(staff)
