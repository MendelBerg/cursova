from Interfaces.init import *
import tools as t
import Interfaces.content.experience as e
import Interfaces.content.middle_age as m
import Interfaces.content.staff_list as s
import Interfaces.content.input as i


def btn_click_main():
    content = t.create_frame_content()[0]
    content['text'] = 'Дані про працівників ТОВ "Снігова корова"'


def btn_click_put():
    window['bg'] = 'blue'
    i.create_input()


def btn_click_staff():
    s.show_select()


def btn_click_age():
    content = t.create_frame_content()[0]
    text_arr = []
    for unit, age in m.show_middle_age():
        year = add_end_year(age)
        text_arr.append(f'Підрозділ "{unit.capitalize()}", {age} {year}.\n')

    content['text'] = ''.join(text_arr).strip()


def add_end_year(num):
    return 'рік' if num % 10 == 1 and num != 11 \
        else 'роки' if num % 10 == 2 and num != 12 or \
                       num % 10 == 3 and num != 13 or \
                       num % 10 == 4 and num != 14 \
        else 'років'


def btn_click_exp():
    content = t.create_frame_content()[0]
    text_arr = []
    for worker in e.show_small_exp():
        year = add_end_year(worker.exp)
        text_arr.append(f'Працівник {worker.name}, підрозділ "{worker.unit.capitalize()}", стаж {worker.exp} {year}.\n')

    content['text'] = ''.join(text_arr).strip()
