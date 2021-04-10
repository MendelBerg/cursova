from tkinter.ttk import Combobox

from Interfaces.init import *
import Interfaces.content.main_content as c
import Interfaces.content.experience as e
import Interfaces.content.middle_age as m
import Interfaces.content.staff_list as s
import Interfaces.content.input as i


def btn_click_main():
    content = c.create_frame_content()
    content['text'] = 'Дані про працівників ТОВ "Снігова корова"'


def btn_click_put():
    window['bg'] = 'blue'
    # content = c.create_frame_content()
    i.create_input()

def btn_click_staff():
    # window['bg'] = 'brown'
    # content = c.create_frame_content()
    # frame = c.create_frame_content()
    s.show_select()


def btn_click_age():
    content = c.create_frame_content()
    text_arr = []
    for unit, age in m.show_middle_age():
        year = 'рік' if age % 10 == 1 \
            else 'роки' if age % 10 == 2 or age % 10 == 3 or age % 10 == 4 \
            else 'років'
        text_arr.append(f'Підрозділ "{unit.capitalize()}", {age} {year}.\n')

    content['text'] = ''.join(text_arr).strip()


def btn_click_exp():
    content = c.create_frame_content()
    text_arr = []
    for worker in e.show_small_exp():
        year = 'рік' if worker.exp % 10 == 1 \
            else 'роки' if worker.exp % 10 == 2 or worker.exp % 10 == 3 or worker.exp % 10 == 4 \
            else 'років'
        text_arr.append(f'Працівник {worker.name}, підрозділ "{worker.unit.capitalize()}", стаж {worker.exp} {year}.\n')

    content['text'] = ''.join(text_arr).strip()
