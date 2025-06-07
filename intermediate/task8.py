#8. Підрахувати довжину рядків: підрахувати кількість рядків довжиною
# більше X.
a=["berry", "contraversion", "story", "phone", "transparency", "tree", "phenomenology", "person", 
   "truth", "etymology", "poem"]
x=6
total=0
for i in a:
    if len(i)>x:
        total+=1
print(total)


