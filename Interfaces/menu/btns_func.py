from tools import create_frame_content
from Interfaces.content.middle_age_exp import fill_content


def btn_click_main():
    create_frame_content('Антарктичний м\'ясокомбінат\n"Снігова корова"')


def btn_click_put():
    from Interfaces.content.input import create_input
    create_input(create_frame_content('Створити запис')['frame'])


def btn_click_staff():
    from Interfaces.content.staff_list import create_select
    create_select(create_frame_content('Список працівників\n\nОберіть категорію')['frame'])


def btn_click_age():
    fill_content(create_frame_content('Cередній вік працівників')['frame'], 'age')


def btn_click_exp():
    fill_content(create_frame_content('Працівники з найменшим досвідом')['frame'])


def btn_click_struct():
    from Interfaces.content.struct import show_struct
    show_struct()


def btn_del_note():
    from Interfaces.content.delete_note import show_del_modal
    show_del_modal()


def btn_click_exit():
    from Interfaces.init import window
    from Interfaces.content.struct import root as struct
    struct.destroy()
    window.destroy()
