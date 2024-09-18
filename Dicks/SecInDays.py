Numbers = int(input("Введите ваше количество секунд"))
days = Numbers // 86400
days1 = days*86400
hours = (Numbers - days1) // 3600
hours1 = hours*3600
minutes = ((Numbers - days1)-hours1) // 60
minutes1 = minutes*60
seconds = (((Numbers - days1)-hours1)-minutes1) // 1
print(days, ":", hours, ":", minutes, ":", seconds)