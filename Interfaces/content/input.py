from Interfaces.init import *


def create_input():
    menu2 = Frame()
    content = Label(menu2, text='Put data')
    content.grid(row=0, column=3, sticky="nsew")
    content.pack()
    menu2.place(relx=0.24, rely=0, relwidth=0.76, relheight=1)
    menu2['bg'] = 'red'
    menu2['width'] = '500'

    labels = [
        "Код:",
        "Имя:",
        "Рік народження:",
        "Посада:",
        "Підрозділ",
        "Досвід роботи (в роках)",
        "Зарплатня",
    ]

    arr = []
    for text in labels:
        Label(master=menu2, text=text).pack(pady=5)
        entry = Entry(menu2, width=25)
        entry.pack()
        arr.append(entry)

    frm_buttons = Button(menu2, text='Clear', command=lambda: create_input())
    frm_buttons.pack(side=LEFT, padx=80, ipadx=10)

    btn_submit = Button(menu2, text="Submit", command=lambda: get_data())
    btn_submit.pack(side=RIGHT, padx=80, ipadx=10)

    def get_data():
        print([e.get() for e in arr])
