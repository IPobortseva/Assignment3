#2. Середнє додатних чисел: Знайдіть середнє додатних чисел.
a = list(map(int,input("Введіть цілі числа через пробіл: ").split( )))
new=[]
for i in a:
    if i>0:
        new.append(i)
print(sum(new)/len(new))
