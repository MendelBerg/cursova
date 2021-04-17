from tools import *

labels = ["Код", "ПІБ", "Рік народження", "Посада",
          "Підрозділ", "Досвід роботи (в роках)", "Зарплатня"]

for person in sort_dict_arr(get_arr_notes('../../'), 0):
    for data in range(len(person)):
        print(f'{labels[data]}: {person[data]}', end=' | ')
    print()
