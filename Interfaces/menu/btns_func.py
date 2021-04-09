from Interfaces.init import *
import Interfaces.content.main_content as c
import Interfaces.content.experience as e


def btn_click_main():
    window['bg'] = 'green'


def btn_click_put():
    window['bg'] = 'blue'


def btn_click_staff():
    window['bg'] = 'brown'


def btn_click_age():
    window['bg'] = 'yellow'


def btn_click_exp():
    window['bg'] = 'pink'
    content = c.create_frame_content()
    text_arr = []
    for worker in e.show_small_exp():
        year = 'рік' if worker.exp % 10 == 1 \
            else 'роки' if worker.exp % 10 == 2 or worker.exp % 10 == 3 or worker.exp % 10 == 4 \
            else 'років'
        text_arr.append(f'Працівник {worker.name}, підрозділ {worker.unit}, стаж {worker.exp} {year}.\n')

    content['text'] = ''.join(text_arr).strip()
