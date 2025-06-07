#1. Фільтрувати за умовою: витягувати зі списку числа, більші за X.
a = list(map(int,input("Введіть цілі числа через пробіл: ").split( )))
x = int(input("Введіть ціле число: "))
new=[]
for i in a:
    if i>x:
        print(i, end=" ")
    else:
        new.append(i)
print()
print(new)

