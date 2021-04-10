from Interfaces.init import *
from tkinter import *


def create_frame_content():
    menu2 = Frame()
    content = Label(menu2)
    content.pack()
    menu2.place(relx=0.24, rely=0, relwidth=0.76, relheight=1)
    menu2['bg'] = 'red'
    menu2['width'] = '500'

    return content

