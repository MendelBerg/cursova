from Interfaces.init import *


def show_select(frame):
    menu2 = Frame()
    content = Label(menu2, text="Choose your favourite month")
    menu2.place(relx=0.24, rely=0, relwidth=0.76, relheight=1)
    menu2['bg'] = 'red'
    menu2['width'] = '500'

    def callbackFunc():
        myLabel = Label(menu2, text=clicked.get()).pack()

    options = [
        'a',
        'b',
        'c'
    ]

    clicked = StringVar()
    clicked.set(options[1])

    drop = OptionMenu(menu2, clicked, *options)
    drop.pack(pady=20)

    btn = Button(menu2, text='select', command=callbackFunc)
    btn.pack(pady=20)

