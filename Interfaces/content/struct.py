from tools import *

labels = ["Код", "ПІБ", "Рік народження", "Посада",
          "Підрозділ", "Досвід роботи (в роках)", "Зарплатня"]


def get_struct():
    arr = []
    i = 0
    for person in sort_dict_arr(get_arr_notes('../'), 0):
        for data in range(len(person)):
            arr.append(f'{labels[data]}: {person[data]}')
        i += 1
    return arr


def show_struct():
    root = Tk()
    root.title("Список працівників")
    root.geometry('1110x700')
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)

    my_list = Listbox(root, yscrollcommand=scrollbar.set, font=f"Georgia 20", bg=content_bg)

    for line in get_struct():
        my_list.insert(END, line)

    my_list.pack(side=LEFT, fill=BOTH, ipady=100, ipadx=1000)
    scrollbar.config(command=my_list.yview)
