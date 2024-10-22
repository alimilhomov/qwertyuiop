# def matn (ism:str,yosh:int):
#     print(f'{ism.capitalize()} ning yoshi:{2024-yosh} da!')
# # matn('alimjon',25)
# matn(input('Ismingizni kiriting:'),
#         int(input('Tugilgan yilingizni kiriting:')))


# def kv_kub (son):
#     print(f'{son} ning kvadrati:{son **2} ga teng\n {son} ning kubi:{son**3} ga teng')

# son = int(input( 'Son kiriting:'))
# # kv_kub(son)


# def son():
#     son = int(input('Son kiriting:'))
    
#     if son % 2 == 0 :
#         print('Kiritgan soningiz juft son:')
#     else:
#         print('Kiritilgan son toq son:')    

# son()

# def daraja():
#     son = int(input('Son kiriting:'))
#     dar = int(input('Darajasini kiriting:'))
#     natija = son ** dar
#     print(f'{son} ning {natija} darajasi')
# daraja()

# ___________________________________5______________________________________
# natija = int()
# for i in range(1, int(input(' Chegara:'))+1):
#     while i <=10:
#         natija += i
#         break
# print(f'1 dan 10 sonlar yigindisi {natija} ga teng')

#  katta < kichik
# def katta_kichik_son(son1,son2):
#   sonlar =[]
#     if son1 > son2:
#         return f'Eng katta son:{son1}',sonlar.append(son1)
#     elif son2 > son1:
#         return f'Eng katta son:{son2}',sonlar.append(son2)
#     else:
#         return f'Ikkala son teng.'

# son1 = int(input('Birinchi soni Kiriting:'))
# son2 = int(input('Ikkinchi soni Kiriting:'))

# natija = katta_kichik_son(son1 , son2 )
# print(natija)



# def sonlaar(son):
#     for i in range(2,11):
#         if son % i == 0:
#             if son :
#                 return f"{son} soni quyidagi sonlarga qoldiq siz bolinadi:"
#         else:
#             return f"{son} soni 2 va 10 orasidagi hech qanday songa bolinmaydi."
# son = int(input('Son kiriting:'))
# natija = sonlaar(son)
# print(natija)

# def sonlaar(son):
#     sonlaar = []
#     for i in range(2, 11):
#         if son % i == 0:
#             sonlaar.append(i)
    
#     if sonlaar:
#         return f"{son} soni quyidagi sonlarga qoldiqsiz bo'linadi: {sonlaar}"
#     else:
#         return f"{son} soni 2 va 10 orasidagi hech qanday songa qoldiqsiz bo'linmaydi."


# son = int(input("Sonni kiriting: "))
# natija = sonlaar(son)
# print(natija)

#  baxolash algaritmi::::

# fanlla = ["Algebra","Geometriya","Fizika","Kimyo","Biologiya"]
# baholla = []
# for i in fanlla:
#     baho = float(input(f"{i} fani uchun baxoni kiriting(1 dan 5 gacha):"))
#     baholla.append(baho)
# ort_baho = sum(baholla)/len(baholla)

# if ort_baho >= 4.5:
#     print("O\'quvchi Alochi! ")
# elif ort_baho >= 3.5:
#     print('O\'quvchi yaxshi!')
# else:
#     print('O\'quvchi qonoqarli! ')


# Yilni xisoblash::::

# yosh = int(input("Yoshingizni kiriting:"))
# print(f'{2024-yosh} siz shu yilda tugilgan siz:')

#  toq Sonlar ::::

# chegara = int(input("Son kiriting:"))3
# toq_son = []
# for son in range(chegara + 1):
#     if son % 2 != 0:
#         toq_son.append(son)
# print(f"0 dan {chegara} gacha bolgan toq sonlar :{toq_son}")


#  sortlash::::: shunsi  oxshamadi
# user = input('>>>>>>>')
# royxat = sorted(user )
# royxat = ""
# for i in royxat:
#     royxat += i
# print(f'Tatiblangan royxat {royxat}')

# #  yigindi ::::
# chegara = int(input("Son kiriting:"))
# natija = 0
# for son in range(1,chegara + 1 ):
#     natija += son
# print(f'1 dan {chegara} gacha bolgan sonlar yigindisi: {natija}')

