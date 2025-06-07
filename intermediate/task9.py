#9. Об’єднати чергування: об’єднувати рядки по черзі з двох списків.
a=["book", "bread", "sugar", "knot", "pen", "flower"]
b=["berry", "cool", "story", "phone", "car", "tree"]
x=1
for i in range (1, len (a)+len(b), 2):
    a.insert(i, b[i-x])
    x+=1
print(a)

