# 5. Список квадратів: створіть список квадратів кожного числа.
a = list(map(int,input("Введіть цілі числа через пробіл: ").split( )))
new=[]
for i in a:
    new.append(i**2)
print(new)
