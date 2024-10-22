lst = [6,8,9,25,36,44,75,89]
son=1
for i in lst:
    if i % 6 == 0 :
        lst[lst.index(i)]=son
    son+=1
print(lst)