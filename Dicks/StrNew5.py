text = (input("Введите ваши данные"))
result = text.split()
list = []
count = 0
count1 = 0
for i in result:
    length = len(i)
    list.append(length)
    length_max = max(list)
    index_of_length_max = list.index(length_max)
    length_min = min(list)
    index_of_length_min = list.index(length_min)
tou = result[index_of_length_max]
tou1 = result[index_of_length_min]
for o in list:
    if length_max == o:
        count += 1
    elif length_min == o:
        count1 += 1
if count == 1:
    print(tou, tou1, count1)
elif count1 == 1:
    print(tou, tou1, count)
else:
    print(tou, tou1, count, count1)
        
#print(count)
#for o in list:
    #if length_min == o:
        #count1 += 1
#print(count1)
#tou = result[index_of_length_max]
#tou1 = result[index_of_length_min]
# print(length_min, index_of_length_min, length_max, index_of_length_max)
#print(tou, tou1, count, count1)
#print(tou1)
  #  type_i = type(i)
   # type_length = type(length)
  #  print(length, type_length, i, type_i)