# x = 450
# y = 450
# natija = id(x) == id(y)
# print(natija)

# # t = (1,[2,3])
# t[1].append(4)
# print(t)

# x = [1,2]
# y = x
# n = id(x)==id(y)
# print(n)



# son = float(input('>>>>>>'))
# ildiz = son ** (1/2)
# print(f"{son}ning ildizi {ildiz} ga teng")



# radius = 5
# pi = 3.14159
# ayla = pi*radius**2
# print(ayla)
import math

def kalkulyator():
    print("Oddiy Kalkulyator")
    print("Qo'shish: + \nAyirish: - \nKo'paytirish: * \nBo'lish: / \nDarajaga ko'tarish: ^ \nKvadrat ildiz: sqrt")
    
    amal = input("Qanday amalni bajarishni xohlaysiz? (+, -, *, /, ^, sqrt): ")

    if amal == "sqrt":
        son = float(input("Sonni kiriting: "))
        print(f"{son} ning kvadrat ildizi: {math.sqrt(son)}")
    else:
        birinchi_son = int(input("Birinchi sonni kiriting: "))
        ikkinchi_son = int(input("Ikkinchi sonni kiriting: "))
        
        if amal == "+":
            print(f"Natija: {birinchi_son + ikkinchi_son}")
        elif amal == "-":
            print(f"Natija: {birinchi_son - ikkinchi_son}")
        elif amal == "*":
            print(f"Natija: {birinchi_son * ikkinchi_son}")
        elif amal == "/":
            if ikkinchi_son != 0:
                print(f"Natija: {birinchi_son / ikkinchi_son}")
            else:
                print("Xatolik: 0 ga bo'lish mumkin emas.")
        elif amal == "^":
            print(f"Natija: {birinchi_son ** ikkinchi_son}")
        else:
            print("Noto'g'ri amal kiritildi.")

kalkulyator()
