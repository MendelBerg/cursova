from collections import namedtuple

Notes = namedtuple("Notes", "code name position subcharpet exp money")


def put_data(file_name, staff):
    with open(f"data/{file_name}.txt", "w") as file:
        for worker in staff:
            file.write(
                f'{worker.code}, {worker.name}, {worker.position}, '
                f'{worker.subcharpet}, {worker.exp}, {worker.money}\n'
            )


def input_note():
    put_data('notes', [
        Notes(
            input(f'The person #{_ + 1}\nCode: '),
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


def get_arr_notes(file_name):
    with open(f'data/{file_name}.txt', 'r') as file:
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
                    sum(1 for _ in open(f'data/{file_name}.txt', 'r'))
                )
            ]
        ]
