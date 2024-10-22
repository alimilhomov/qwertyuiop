# user = input(">>>").lower()
# buyurtma= [ ]



# menyu={ 'lavash':30_000,
#          'pizza':45_000,
#           'cola':18_000,
#         'sprite':14_000,
#         'hot_dog':20_000
#     }

# if user in menyu:
#     buyurtma.append(user.title())
# else:
#     print('Kechrasiz! Bizda bunday toam mavjud emas!')
#     print( buyurtma)



# menyu={
#     'Pizza':{'Danar pizza':60_000,
#              'peperoniy':45_000,
#              'oddiy':35_000,
#              },

#     'lavash':{'Pishloqli':35_000,
#               'Oddiy':25_000,
#     },
#     'ichimliklar':{'cola': 18_000,
#                    'sprite': 15_000,
#                    'fanta':15_000,
#     },
#      'hot_dog':{'kattasi':25_000,
#                 'ortanchasi':20_000,
#                 'kichigi':15_000,
#      },
# }

# zakaz=[]
# narx=0
# print("Assalom alaykum!")
# print("Mana munyu:")
# for i in menyu:
#      x=1
#      print(f"{i}:")
#      for j in menyu [i]:
#          print(f" {x}.{j}")
#          x +=1
# print("/n")
# while True:
  
#         z=input( 'nimadir zakaz qilasizmi:').lower()
#         for i in menyu:
#              if z in menyu[i]:
#               print(f'narx {menyu[i][z]}')
#               zakaz.append (z)
#               narx+=menyu[i][z]
#              break
#         else:
#              if z in menyu['boldi','stop','yoq']:
#                break
#              else:        
#                   print('menyuda buyurtmangiz yoq')
#                   print('kodi toxtatish uchun(boldi,stop,yoq)yozing')
#                   print("yana",end=" ")
#                   print("Buyurtmalaringiz:")
        # for i in zakaz:
        #  if zakaz[-1]!=i:
        #   print(i,end=",")
        # else :
        #   print(i,end="./n")
        #   print(f"Obshiy narx:{narx}som")

    
    
              
def add (x,y):
        return x+y
def subtract (x,y):
        return x-y
def multiply (x,y):
        return x*y
def divide (x,y):
        if y !=0:
                return x/y
        else:
                return" Xatolik: nolga bolishda"
        
def calculator():
        print('operatsiya tanlang:')
        print('1. Qoshish')       
        print('2. Ayirish')
        print('3.kopaytirish')
        print('4.Bolish')

user =input('Operatsiya nomerini korsating(1/2/3/4):')
if user in ['1','2','3','4',]:
    num1=float(input('birinchi raqamni korsating:'))
    num2=float(input('Ikkinchi raqaminikorsating:'))
if user == '1':
        print(f'Natija:{add(num1,num2)}')
elif user =='2':
        print(f'Natija:{subtract(num1,num2)}')
elif user =='3':
        print(f'Natija:{multiply(num1,num2)}')
elif user =='4':
        print(f'Natija:{divide(num1,num2)}')    
else:
        print('Notogri tanlash. 1: dan 4: gach bolgan operatsiyani tanlang.')    
   











