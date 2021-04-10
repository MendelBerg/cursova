from tkinter import *

root = Tk()
root.title('Text')
root.geometry('400x400')

options = [
    'a',
    'b',
    'c'
]

clicked = StringVar()
clicked.set(options[1])

drop = OptionMenu(root, clicked, *options)
drop.pack(pady=20)

root.mainloop()
