from Interfaces.init import *
from tools import *
import Interfaces.content.main_content as c


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
    c.content['text'] = show_small_exp()
