fruit = ["사과", "사과", "바나나", "포도", "귤", "귤", "귤"]

d = {}

for f in fruit:

    if f in d:
        d[f] = d[f] + 1
    else:
        d[f] = 1

print(d)
