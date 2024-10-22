# n =6
# for k in range(1,11):
#     print(f'{n}*{k}={n*k}')
# print('\n\n'.join([f"{n}:\n" + '\n'.join([f"{n} x {k} = {n * k}" for k in range(1, 11)]) for n in range(1, 10)]))




# def print_menu():
#     print("Меню:")
#     print("1. Бургер - 150 руб.")
#     print("2. Картошка фри - 80 руб.")
#     print("3. Кола - 60 руб.")
#     print("4. Выход")

# def calculate_total(order):
#     menu_prices = {
#         1: 150,  # Бургер
#         2: 80,   # Картошка фри
#         3: 60    # Кола
#     }
#     total = sum(menu_prices[item] for item in order)
#     return total

# def fast_food_cash_register():
#     order = []
#     while True:
#         print_menu()
#         choice = input("Выберите номер товара (или 4 для выхода): ")
        
#         if choice == '4':
#             break
        
#         if choice in ['1', '2', '3']:
#             order.append(int(choice))
#             print("Товар добавлен в корзину.")
#         else:
#             print("Неверный выбор. Пожалуйста, выберите номер от 1 до 4.")

#     total = calculate_total(order)
#     print(f"Вы заказали:")
#     print(f"- {order.count(1)} Бургер(ов)")
#     print(f"- {order.count(2)} Картошка фри")
#     print(f"- {order.count(3)} Кола(ы)")
#     print(f"Итоговая сумма: {total} руб.")

# # Запуск кассового приложения
# fast_food_cash_register()


# vil='Toshkent'
# shah= 'Toshkent'
# max='Toshkent'
# koch='Yusuf ota Xoshimov'

# print(  '\n',vil + 'viloyati', '\n', shah + 'shaxri', '\n',  max +'maxallasi',   
#      '\n', koch +'kochasida turaman',)


# print(  vil + 'viloyati',  shah + 'shaxri',   max +'maxallasi',   
#       koch +'kochasida turaman')


# print(vil,'viloyati:',shah,'shaxri:'.capitalize())
 
# # otam:
# ism= 'Qobiljon'
# fam='Yusupov'
# shar='Ilhomjon ogli'
# # ona:
# ism2='Valida'
# fam2='Yusupova'
# shar2='Qudrattila qizi'
# # akam:
# ism3='G\'ofirjon'
# fam3='Ilxomov'
# shar3='Qobiljon ogli'
# itogo=f'{fam}   {ism}   {shar}'
# itogo2=f'{fam2}   {ism2}   {shar2}'
# itogo3=f'{fam3}   {ism3}   {shar3}'
# # print('Ismim:',ism,'Familyam:',fam,'Sharifim',shar .capitalize())
# # print('Ismim:',ism2,'Familyam:',fam2,'Sharifim',shar2 .capitalize())
# # print('Ismim:',ism3,'Familyam:',fam3,'Sharifim',shar3 .capitalize())
# # print(itogo.lower())
# # print(itogo.upper())
# print(itogo.title())
# print(itogo2.title())
# print(itogo3.title())

# # ota:
# ism='Otam'
# # made='Mercedes Benz:'
# model='GLM.500'
# price=':60_000'

# buy="Men {} yangi {}  {} mashinasini {}  narxga sotib oldim "
# print( buy.format(ism,made,model,price))
# # onam:
# ism1='onam'
# a1='HAJ'
# a2='Bilet'
# a3='Inshaollox'
# a4='Men {} {} uchun {} safariga {} sotib olaman {}'
# print( a4.format( ism, ism1, a1, a2, a3).capitalize())
# # gf='qwertyuiopsdfghjklsdfghjksdfghjksdfqwertyasdfghwertysdfghqwertyqwertyasdfgqwert'
# # print(gf.count('qwerty'))
            
# sdf='qwertyuiasdfghjqwertyuasdfghasdfgqwertyasdfghqwertyuasdfghqwertysdfgsdfghasdfsdfgasdf'
# print( sdf.count('asd'))
