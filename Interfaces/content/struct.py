from tools import *

labels = ["Код", "ПІБ", "Рік народження", "Посада",
          "Підрозділ", "Досвід роботи (в роках)", "Зарплатня"]


def get_struct():
    dict_text = {}
    i = 0
    for person in sort_dict_arr(get_arr_notes('../'), 0):
        dict_text[i] = []
        for data in range(len(person)):
            dict_text[i].append(f'{labels[data]}: {person[data]}')
        i += 1
    return dict_text


def show_struct():
    root = Tk()
    root.title("Список працівників")
    root.geometry('1110x700')
    scrollbar = Scrollbar(root, bg='#1A2026')
    scrollbar.pack(side=RIGHT, fill=Y)

    my_list = Listbox(root, yscrollcommand=scrollbar.set, font=f"Georgia 20", bg=content_bg)
    d = get_struct()

    for line in d:
        for data in d[line]:
            my_list.insert(END, data)
        my_list.insert(END, '===========================')

    my_list.pack(side=LEFT, fill=BOTH, ipady=100, ipadx=1000)
    scrollbar.config(command=my_list.yview)
