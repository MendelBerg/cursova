from tools import *


flag = False
global root, scrollbar, my_list


def get_struct(option):
    dict_text = {}
    i = 0
    for person in sort_dict_arr(get_arr_notes('../'), option):
        dict_text[i] = []
        for data in range(len(person)):
            dict_text[i].append(f'{labels[data]}: {person[data]}')
        i += 1
    return dict_text


def show_struct():
    global root, scrollbar, my_list
    root = Tk()
    root.title("Список працівників")
    root.geometry('750x470')

    scrollbar = Scrollbar(root, bg='#1A2026')
    my_list = Listbox(root, yscrollcommand=scrollbar.set, font=f"Georgia 20", bg=content_bg)

    btn = create_btn(root, 'Сортувати', lambda: struct_content())
    btn.pack(side=TOP, padx=80, ipadx=10)
    btn = create_btn(root, 'OK', lambda: root.destroy())
    btn.pack(side=BOTTOM, padx=30, ipadx=10)

    struct_content()


def struct_content():
    global scrollbar, my_list, root, flag
    scrollbar.destroy()
    my_list.destroy()
    scrollbar = Scrollbar(root, bg='#1A2026')
    scrollbar.pack(side=RIGHT, fill=Y)

    my_list = Listbox(root, yscrollcommand=scrollbar.set, font=f"Georgia 20", bg=content_bg)

    if flag:
        struct_notes = get_struct(4)
        flag = False
    else:
        struct_notes = get_struct(0)
        flag = True

    for line in struct_notes:
        for data in struct_notes[line]:
            my_list.insert(END, data)
        my_list.insert(END, '')

    my_list.pack(side=LEFT, fill=BOTH, ipady=100, ipadx=1000)
    scrollbar.config(command=my_list.yview)
