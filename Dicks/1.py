number_of_day = input("Введите ваше число")
dict_week = {'1': "Понедельник", 'Вторник': 2, 'Среда': 3, 'Четверг': 4, 'Пятница': 5, 'Суббота': 6, 'Воскресенье': 7}
answer = dict_week.get(number_of_day)
print(answer)