from tools import create_frame_content


def btn_click_main():
    create_frame_content('Дані про працівників ТОВ\n"Снігова корова"')


def btn_click_put():
    from Interfaces.content.input import create_input
    frame = create_frame_content('Створити запис')[1]
    create_input(frame)


def btn_click_staff():
    from Interfaces.content.staff_list import create_select
    frame = create_frame_content('Список працівників\n\nОберіть категорію')[1]
    create_select(frame)


def btn_click_age():
    from Interfaces.content.middle_age_exp import fill_content
    create_frame_content(fill_content('середній вік'))


def btn_click_exp():
    from Interfaces.content.middle_age_exp import fill_content
    create_frame_content(fill_content('найменший досвід'))
