Numbers = input("Введите ваше число")
Numbers1 = Numbers.split( )
print(Numbers1)
pov = Numbers1.count(0)
pov1 = Numbers1.count(1)
pov2 = Numbers1.count(2)
pov3 = Numbers1.count(3)
pov4 = Numbers1.count(4)
pov5 = Numbers1.count(5)
pov6 = Numbers1.count(6)
pov7 = Numbers1.count(7)
pov8 = Numbers1.count(8)
pov9 = Numbers1.count(9)
Er = [pov, pov1, pov2, pov3, pov4, pov5, pov6, pov7, pov8, pov9]
Answer = sum(Er)
if Answer != 0:
    print("False")
else:
    print("True")
print(pov, pov1, pov2, pov3, pov4, pov5, pov6, pov7, pov8, pov9) 