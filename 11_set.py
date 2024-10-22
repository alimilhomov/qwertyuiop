my = ['ona', 'ota', 'aka', [13,45,['toga',16,'opa'],['amma']],3,67,'tom']
for i in my :
    if type(i) != list:
        if isinstance(i, int):
            print(i, end=' ')
        else:
            print(i.upper(),end=' ')
    elif type(i) == list:
        for j in i :
            if type(j) == list:
                for k in j :
                    if isinstance(k, int):
                        print(k, end=' ')
                    else:
                        print(k.upper(), end=' ')
            elif type(j) == list:
                if isinstance(j, int):
                    print(j, end=' ')
                else:
                    print(j.upper(), end=' ')                     


# for i in my [2][2]:
#     if isinstance(i, int):
#             print(i)
#     elif i == my[2][2][-1]:
#             print(i.upper())
#     else:
#             print(i.title())





