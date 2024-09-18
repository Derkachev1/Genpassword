height = float(input("Введите ваш рост (м)"))
weight = float(input("Введите вашу массу (кг)"))
BMI = weight/(height**2)
if BMI < 16:
    print("Выраженный дефицит массы тела", BMI)
elif BMI < 18.5:
    print("Недостаточная (дефицит) масса тела", BMI)
elif BMI < 25:
    print("Норма", BMI)
elif BMI < 30:
    print("Избыточная масса тела (предожирение)", BMI)
elif BMI < 35:
    print("Ожирение первой степени", BMI)
elif BMI < 40:
    print("Ожирение второй степени", BMI)
elif BMI > 40:
    print("Ожирение третьей степени (морбидное)", BMI)