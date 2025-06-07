#3. Складна маніпуляція рядками: виділіть і введіть великі літери в окремих
# підрядках.
a=["berry", "analysis", "story", "transparency", "parent", "phenomenology", "person", 
   "truth", "cave"]
for i in a:
    if len(i)>7:
        print(i.capitalize(), end=" ")