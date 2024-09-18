Number = float(input("Введите ваше число"))
Answer = 0
for i in range(1,11):
    Answer = i * Number
    print(i, "*", Number, "=", Answer)