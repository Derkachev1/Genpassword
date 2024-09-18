number_of_day = input("Введите ваше число")
dict_week = {'1': 'Понедельник', '2': 'Вторник', '3': 'Среда', '4': 'Четверг', '5': 'Пятница', '6': 'Суббота', '7': 'Воскресенье'}
answer = dict_week.get(number_of_day)
print(answer)