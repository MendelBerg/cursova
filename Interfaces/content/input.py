from Interfaces.init import *

def create_input():
    menu2 = Frame()
    content = Label(menu2, text='Put data')
    content.grid(row=0, column=3, sticky="nsew")
    content.pack()
    menu2.place(relx=0.24, rely=0, relwidth=0.76, relheight=1)
    menu2['bg'] = 'red'
    menu2['width'] = '500'
    #
    # Список ярлыков полей.
    labels = [
        "Имя:",
        "Фамилия:",
        "Адрес 1:",
        "Адрес 2:",
        "Город:",
        "Регион:",
        "Почтовый индекс:",
        "Страна:",
    ]

    # Цикл для списка ярлыков полей.
    for idx, text in enumerate(labels):
        # Создает ярлык с текстом из списка ярлыков.
        label = Label(master=menu2, text=text)
        # Создает текстовое поле которая соответствует ярлыку.
        entry = Entry(master=menu2, width=50)
        # Использует менеджер геометрии grid для размещения ярлыков и
        # текстовых полей в строку, чей индекс равен idx.
        label.pack()
        entry.pack()

    # Создает новую рамку `frm_buttons` для размещения в ней
    # кнопок "Отправить" и "Очистить". Данная рамка заполняет
    # все окно в горизонтальном направлении с
    # отступами в 5 пикселей горизонтально и вертикально.

    frm_buttons = Button(menu2, text='Clear')
    frm_buttons.pack(side=LEFT, padx=80, ipadx=10)
    #
    # Создает кнопку "Отправить" и размещает ее
    # справа от рамки `frm_buttons`.
    btn_submit = Button(menu2, text="Submit")
    btn_submit.pack(side=RIGHT, padx=80, ipadx=10)


