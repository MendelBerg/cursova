from tkinter import Frame, Button
from Interfaces.menu.btns_func import *
from tools import create_btn


def passive_btn():
    for BTN in menu_btn_arr:
        BTN['borderwidth'] = 3
        BTN['relief'] = 'groove'


def btn_active(func):
    def wrapper(button):
        passive_btn()
        button['relief'] = "solid"
        func()
    return wrapper


menu = Frame(bg='#9A9A9A')
menu.grid(row=0, column=0, sticky="ns")


btn_main = create_btn(menu, "Головна", lambda: btn_active(btn_click_main)(btn_main))
btn_put = create_btn(menu, "Створити запис", lambda: btn_active(btn_click_put)(btn_put))
btn_get_staff = create_btn(menu, "Список працівників", lambda: btn_active(btn_click_staff)(btn_get_staff))
btn_get_age = create_btn(menu, "Середній вік", lambda: btn_active(btn_click_age)(btn_get_age))
btn_get_exp = create_btn(menu, "Найменший стаж", lambda: btn_active(btn_click_exp)(btn_get_exp))

menu_btn_arr = [btn_main, btn_put, btn_get_staff, btn_get_age, btn_get_exp]

for row, btn in enumerate(menu_btn_arr):
    btn.grid(row=row, column=0, sticky="ew", padx=5, pady=5)

btn_active(btn_click_main)(btn_main)
