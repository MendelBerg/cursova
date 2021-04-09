import tkinter as tk

window = tk.Tk()
window.title("Підприємство \"Снігова корова\"")
window['bg'] = '#6A6A6A'
window.geometry('750x450')

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

menu = tk.Frame(window)


def btn_active(func):
    def wrapper(btn):
        passive_btn()
        btn['borderwidth'] = 3
        btn['relief'] = "solid"
        func()

    return wrapper


@btn_active
def btn_click_main():
    window['bg'] = '#6A6A6A'


@btn_active
def btn_click_put():
    window['bg'] = 'blue'


@btn_active
def btn_click_staff():
    window['bg'] = 'brown'


@btn_active
def btn_click_age():
    window['bg'] = 'yellow'


@btn_active
def btn_click_exp():
    window['bg'] = 'pink'


btn_main = tk.Button(menu, text="Головна", borderwidth='3', relief='solid', command=lambda: btn_click_main(btn_main))
btn_put = tk.Button(menu, text="Створити запис", borderwidth='3', relief='groove', command=lambda: btn_click_put(btn_put))
btn_get_staff = tk.Button(menu, text="Список працівників", borderwidth='3', relief='groove', command=lambda: btn_click_staff(btn_get_staff))
btn_get_age = tk.Button(menu, text="Середній вік", borderwidth='3', relief='groove', command=lambda: btn_click_age(btn_get_age))
btn_get_exp = tk.Button(menu, text="Найменший стаж", borderwidth='3', relief='groove', command=lambda: btn_click_exp(btn_get_exp))

menu_btn_arr = [btn_main, btn_put, btn_get_staff, btn_get_age, btn_get_exp]


def passive_btn():
    for btn in menu_btn_arr:
        btn['borderwidth'] = 3
        btn['relief'] = 'groove'

btn_main.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_put.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_get_age.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_get_staff.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
btn_get_exp.grid(row=4, column=0, sticky="ew", padx=5, pady=5)

menu.grid(row=0, column=0, sticky="ns")
menu['bg'] = '#9A9A9A'

window.mainloop()
