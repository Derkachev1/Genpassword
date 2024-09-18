text = (input("Введите ваши данные"))
result = text.split()
list = []
for i in result:
    length = len(i)
    list.append(length)
    length_max = max(list)
    index_of_length_max = list.index(length_max)
    length_min = min(list)
    index_of_length_min = list.index(length_min)
tou = result[index_of_length_max]
tou1 = result[index_of_length_min]
print(length_min, index_of_length_min, length_max, index_of_length_max)
print(tou)
print(tou1)
  #  type_i = type(i)
   # type_length = type(length)
  #  print(length, type_length, i, type_i)