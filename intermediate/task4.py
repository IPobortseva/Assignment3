#4. Багаторівневе сортування: сортування за спаданням, потім за частотою.
a=[90, 7, 5, 67, 67, 5, 34, 56, 23, 23, 13, 0, 23, 45, 51, 5, 5]
a.sort(reverse=True)
new=[]
print(a)
for i in a:
    b=a.count(i)
    if b==4:
        new.append(i)
for i in a:
    b=a.count(i)
    if b==3:
        new.append(i)
for i in a:
    b=a.count(i)
    if b==2:
        new.append(i)
for i in a:
    b=a.count(i)
    if b==1:
        new.append(i)
print(new)

    

