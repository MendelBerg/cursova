from Interfaces.menu.btns_func import *
from Interfaces.init import *


def passive_btn():
    for btn in menu_btn_arr:
        btn['borderwidth'] = 3
        btn['relief'] = 'groove'


def btn_active(func):
    def wrapper(btn):
        passive_btn()
        btn['relief'] = "solid"
        func()
    return wrapper


menu = Frame(bg='#9A9A9A')
menu.grid(row=0, column=0, sticky="ns")

btn_main = Button(menu, text="Головна", command=lambda: btn_active(btn_click_main)(btn_main))
btn_put = Button(menu, text="Створити запис", command=lambda: btn_active(btn_click_put)(btn_put))
btn_get_staff = Button(menu, text="Список працівників", command=lambda: btn_active(btn_click_staff)(btn_get_staff))
btn_get_age = Button(menu, text="Середній вік", command=lambda: btn_active(btn_click_age)(btn_get_age))
btn_get_exp = Button(menu, text="Найменший стаж", command=lambda: btn_active(btn_click_exp)(btn_get_exp))

menu_btn_arr = [btn_main, btn_put, btn_get_staff, btn_get_age, btn_get_exp]

for row, btn in enumerate(menu_btn_arr):
    btn.grid(row=row, column=0, sticky="ew", padx=5, pady=5)

btn_active(btn_click_main)(btn_main)
