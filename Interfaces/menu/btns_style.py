from Interfaces.menu.btns_func import *

menu = Frame(window)

btn_main = Button(menu, text="Головна", borderwidth='3', relief='groove',
                     command=lambda: btn_active(btn_click_main)(btn_main))
btn_put = Button(menu, text="Створити запис", borderwidth='3', relief='groove',
                    command=lambda: btn_active(btn_click_put)(btn_put))
btn_get_staff = Button(menu, text="Список працівників", borderwidth='3', relief='groove',
                          command=lambda: btn_active(btn_click_staff)(btn_get_staff))
btn_get_age = Button(menu, text="Середній вік", borderwidth='3', relief='groove',
                        command=lambda: btn_active(btn_click_age)(btn_get_age))
btn_get_exp = Button(menu, text="Найменший стаж", borderwidth='3', relief='groove',
                        command=lambda: btn_active(btn_click_exp)(btn_get_exp))

btn_main.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_put.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_get_age.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_get_staff.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
btn_get_exp.grid(row=4, column=0, sticky="ew", padx=5, pady=5)

menu.grid(row=0, column=0, sticky="ns")
menu['bg'] = '#9A9A9A'

menu_btn_arr = [btn_main, btn_put, btn_get_staff, btn_get_age, btn_get_exp]


def passive_btn():
    for btn in menu_btn_arr:
        btn['borderwidth'] = 3
        btn['relief'] = 'groove'


def btn_active(func):
    def wrapper(btn):
        passive_btn()
        btn['borderwidth'] = 3
        btn['relief'] = "solid"
        func()

    return wrapper


btn_active(btn_click_main)(btn_main)
