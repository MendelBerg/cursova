from tkinter import *

master = Tk()
master.title("Диалоговое окно в Tkinter")
master.columnconfigure(1, weight=1)
master.columnconfigure(3, pad=7)
master.rowconfigure(3, weight=1)
master.rowconfigure(5, pad=7)

lbl = Label(master, text="Окна")
lbl.grid(sticky=W, pady=4, padx=5)

area = Label(master,text="Окна2")
area.grid(row=0, column=1, columnspan=2, rowspan=4, padx=5, sticky=E + W + S + N)


master.mainloop()
