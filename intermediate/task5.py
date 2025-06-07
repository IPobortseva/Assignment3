#5. Об’єднати списки умовно: об’єднати два списки на основі умов.
list1=[9, -8, 76, 5, 0, 25, 32]
list2=[5, 87, 90, 4, -21, 5, 13]
new=[]
for i in list1:
    if (i**2)>70:
        new.append(i)
for i in list2:
    if (i/7)<6:
        new.append(i)
print(new)