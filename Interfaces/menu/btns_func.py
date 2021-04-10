from Interfaces.init import *
import tools as t
import Interfaces.content.experience as e
import Interfaces.content.middle_age as m
import Interfaces.content.staff_list as s
import Interfaces.content.input as i


def btn_click_main():
    t.create_frame_content('Дані про працівників ТОВ "Снігова корова"')


def btn_click_put():
    frame = t.create_frame_content('Створити запис')[1]
    i.create_input(frame)


def btn_click_staff():
    frame = t.create_frame_content('Список працівників\n\nОберіть категорію')[1]
    s.show_select(frame)


def btn_click_age():
    fill_content(m.show_middle_age(), 'середній вік')


def fill_content(data, title):
    content = t.create_frame_content('')[0]
    text_arr = []

    for row in data:
        year = add_end_year(row[1])
        text_arr.append(f'Підрозділ "{row[0].capitalize()}", {row[1]} {year}.\n'
                        if len(data[0]) == 2 else
                        f'Працівник {row[2]}, підрозділ "{row[0].capitalize()}", стаж {row[1]} {year}.\n '
                        )

    content['text'] = f"Данні про {title} працівників\n\n{''.join(text_arr).strip()}"


def btn_click_exp():
    fill_content(e.show_small_exp(), 'найменший досвід')


def add_end_year(num):
    return 'рік' if num % 10 == 1 and num != 11 \
        else 'роки' if num % 10 == 2 and num != 12 or \
                       num % 10 == 3 and num != 13 or \
                       num % 10 == 4 and num != 14 \
        else 'років'
