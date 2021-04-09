from  tkinter import *

window = Tk()
window.title("Підприємство \"Снігова корова\"")
window['bg'] = '#6A6A6A'
window.geometry('750x450')

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)