#4. Агрегована умовна сума: сума чисел, які діляться на Y.
a = list(map(int,input("Введіть цілі числа через пробіл: ").split( )))
y = int(input("Введіть ціле число: "))
new=[]
for i in a:
    if i%y==0:
        new.append(i)
print(sum(new))

