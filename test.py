import main as m

print('Save notes in file')
m.put_data(m.get_input_notes_arr())

print('Sort data')
m.show_notes_filter(
    m.get_notes_filter(
        input('Which unit do you find: '),
        m.get_arr_notes()
    )
)

print('Middle age')
m.get_middle_age_staff(
    m.get_notes_filter(
        input('Which unit do you find: '),
        m.get_arr_notes()
    )
)

print('Small experience')
m.show_small_exp(m.get_arr_notes())
