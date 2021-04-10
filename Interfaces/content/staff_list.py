from tkinter.ttk import Combobox

from tools import *
from Interfaces.init import *


def show_select(frame):
    menu2 = Frame()
    content = Label(menu2)
    menu2.place(relx=0.24, rely=0, relwidth=0.76, relheight=1)
    menu2['bg'] = 'red'
    menu2['width'] = '500'

    fontExample = ("Courier", 16, "bold")
    comboExample = Combobox(menu2,
                            values=[
                                "January",
                                "February",
                                "March",
                                "April"],
                            font=fontExample)

    menu2.option_add('*TCombobox*Listbox.font', fontExample)

    comboExample.grid(column=0, row=1)
    content.grid(row=0, column=3, sticky="nsew")
    content.pack()
