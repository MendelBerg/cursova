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
    put_data('data', [
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


input_note()
