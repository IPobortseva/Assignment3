#2. Зведення вкладених списків: зведення списку списків в єдиний список.
bidlist=[
    [3, 5, 7, 8],
    ["Berlin", "Spiderman", "GPA", "milk"],
    ["Bulochka", "is", "the", "best", "car"],
    [8, 10, 13, 4]
]
newlist=[]
for row in bidlist:
    for i in row:
        newlist.append(i)
print(newlist)
