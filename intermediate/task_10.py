#10. Помножити, якщо: помножити числа на Y, якщо вони більші за X.
a=[2, 56, 8, 76, 56, -9, -32, 90, -2, 0, 23, -45, 23]
x=10
y=3
for i in a:
    if i>x:
        print(i*y, end=" ")