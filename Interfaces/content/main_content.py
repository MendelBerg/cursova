from Interfaces.init import *
from tools import *

show_small_exp()

menu2 = Frame()
content = Label(menu2, text='text\nafdasdf')
content.grid(row=0, column=3, sticky="nsew")
content.pack()
menu2.place(relx=0.24, rely=0, relwidth=0.76, relheight=1)
menu2['bg'] = 'red'
menu2['width'] = '500'

