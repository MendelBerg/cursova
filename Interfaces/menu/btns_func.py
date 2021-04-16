from tools import create_frame_content


def btn_click_main():
    create_frame_content('Антарктичний м\'ясокомбінат\n"Снігова корова"')


def btn_click_put():
    from Interfaces.content.input import create_input
    create_input(create_frame_content('Створити запис')['frame'])


def btn_click_staff():
    from Interfaces.content.staff_list import create_select
    create_select(create_frame_content('Список працівників\n\nОберіть категорію')['frame'])


def btn_click_age():
    from Interfaces.content.middle_age_exp import fill_content
    fill_content(create_frame_content('Cередній вік працівників')['frame'], 'age')


def btn_click_exp():
    from Interfaces.content.middle_age_exp import fill_content
    fill_content(create_frame_content('Працівники з найменшим досвідом')['frame'])
