# matn='Fundation'
# print(matn[4::-1].capitalize()+' '+matn[-1:4:-1])
# print(matn[5::-2].capitalize()+' '+matn[-3:1:-1])
# s=input(">>>>>>>")
# print("a"in s)
# print (f"A:{s.count('a')}/nB:{s.count('b')}/nC:{s.count('c')}/nD:{s.count('d')}/nF:{s.count('f')}")


# r=input(">>>")
# print(len(r))
# son=int(input(">>>"))
# # print (f"""
# # 1x{son}={son*son}
# # {son}x1={son*1}
# # """)

# print (f"""
# {son}X 1={son*1}
# {son} x2={son*2}
# {son}X 3={son*3}
# {son}X 4={son*4}
# {son}X 5={son*5}
# {son}X 6={son*6}
# {son}X 7={son*7}
# {son}X 8={son*8}
# {son}X 9={son*9}
# {son}X 10={son*10}""")


# bozorlik=['sabzi', 'kortoshka','yog','olma','nok','banan','uzum',]
# mevalar=bozorlik.pop(3)
# sabzavotlar=bozorlik.pop(1)
# print(mevalar)
# print(sabzavotlar) 
# del bozorlik[0]
# print(bozorlik)
# bozorlik.insert(1,"qalampir")
# print(bozorlik)


# cars=['malibu','trecker','mers','damas','cobolt','damas',]

# # for car in cars:
# #     if car[0].lower()=='m':
# #         print(car)
# # cars.remove("malibu")
# # print(cars)
# # # cars.remove("damas")

# # print(cars)
# # del cars[2]
# # print(cars)
# # cars.append('tico')
# # print(cars)
# # cars.extend ( [ 'wolsvagen'])
# # print(cars)


# range
# numbers=list(range(100,1500))
# # print(numbers)
# for num in numbers:
#     if num % 2 == 0:
#         print(num) 




# def hisobla():
#     jami = 0
#     while True:
#         mahsulot_narxi = input("Mahsulot narxini kiriting (yoki 'x' tugmasini bosing): ")
        
#         if mahsulot_narxi.lower() == 'x':
#             break
#         try:
#             mahsulot_narxi = float(mahsulot_narxi)
#             jami += mahsulot_narxi
#         except ValueError:
#             print("Iltimos, to'g'ri qiymat kiriting.")
    
#     print(f"Jami to'lanishi kerak bo'lgan summa: {jami} so'm")
    
# hisobla()
# uyga vazifa

# mexmonlar=('Abdulla', 'Said', 'Boxodir', 'Nodir', 'Iborixim', )
# for i in mexmonlar:
#     print(f"Assalom aleykum hurmatli: {i.title()}\n"
#           f"Sizni lutfan 26.01.2025 boladigan naxorgi oshga taklif etamiz!\n"
#           f"Hurmat bilan ___________________________________________lar oilasi!\n"
#           f"Manzil Koshona Toyxonasi!\n\n")  

# cars =('ferari', 'mers', 'lomborghini', 'bmw', 'mclaren', 'toyota', 'tesla', )
# (alimjon,*raxmatilla,ibo,boxo)=cars   

# print(f"alimjon:{alimjon}")
# print(f"raxmatilla:{raxmatilla}")
# print(f"boxo:{boxo}")
# print(f"ibo:{ibo}")

# a1=('qwerty', 'oiuytree' )
# a2=('asdfgh', 'kjhgfds')
# a3=('zxcvb', 'mnbvcx')
# a4 = a1,a2,a3
# for i in a4:
#     print(a4)


# comand = ('Arsenal', 'Man Sity', 'Real', 'Totemxem', 'Paxtakor', 'Shortan', 'Navbaxor')
# print(comand[0::3])
# print(comand[0:3])





# juft_sonlar = list(range(100,1500,2))
# print(juft_sonlar)
# print(sum(juft_sonlar))

# toq_sonlar = list(range(101,1500,2))
# print(sum(toq_sonlar))
# print(toq_sonlar)

# comand = ('Arsenal', 'Man Sity', 'Real', 'Totemxem', 'Paxtakor', 'Shortan', 'Navbaxor')
# print(sorted(comand))
# # print(sorted(comand, reverse=True))

# s2 =['Sultonmurodov Abdulla',28]
# s3 =[ 'jentra']
# print(f'Dostim {s2} yoshida yangi{s3} moshina sotip oldi')

lst=[3,6,7,8,6,36,11,12,24,14,]
son=1
for i in lst:
    if i % 6 == 0 :
        lst[lst.index(i)]=son
        son+=1
print(lst)



# lst=(3,6,7,8,9,10,11,12,13,14,)
# lst=list(lst)
# son=1
# for i in lst:
#     if i % 6 == 0 :
#         lst[lst.index(i)]=son
#         son+=1
# lst=tuple(lst)
# print(lst)

