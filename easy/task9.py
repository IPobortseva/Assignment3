#9. Знайти всі паліндроми: видобути всі паліндромні рядки зі списку.
a=["koko", "ortro", "polylop", "three", "dddd", "o"]
for i in a:
    if i==i[::-1]:
        print(i, end=" ")


