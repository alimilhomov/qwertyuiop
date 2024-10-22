# a =  (5,'hi')
# ins = isinstance(a,(int,str))
# print (ins)

# stor = []
# while True:
#     command = input('Command:')
#     if command == '/add':
#         stor.append(
#             {
#                 'nomi':input('nomi:'),
#                 'narxi':int(input('narxi:')),
                
#                 'soni': int(input('soni:'))
#             }
#         )
#     elif command == '/royxat':
#         for i in stor:
#             print(f'Nomi: {i["nomi"]}, Narxi: {i["narxi"]}, Soni: {i["soni"]}ta')
#     elif command == len(stor) or command =='/exit':
#         print("Xardingiz uchun tashakur")
#         break





chaqiruv = []
a = int(input("Nechta osmir chaqirilgan!"))

for i in range(n):
    print(f"\n{i+1}-chaqiruvchi ma'lumotlarini kiriting:")
    ism = input("Ismi: ")
    yosh = int(input("Yosh: "))
    jins = input("Jinsi (erkak/ayol): ")
    sogliq = input("Sog'liq holati (yaxshi/o'rta/yomon): ")
    talim = input("Ta'lim darajasi (oliya/o'rta): ")

chaqiruv.append({
    "ism": ism,
    "yosh": yosh,
    "jins": jins,
    "sogliq": sogliq,
    "talim": talim,
})
min_yosh = 18
max_yosh = 27
jins = "erkak"
sogliq = "yaxshi"


yaroqli_chaqiruvchilar = []

for chaqiruv in yaroqli_chaqiruvchilar:
    if chaqiruv["yosh"] >= min_yosh and chaqiruv["yosh"] <= max_yosh and chaqiruv["jins"] == jins and chaqiruv["sogliq"] == sogliq:
        yaroqli_chaqiruvchilar.append(chaqiruv["ism"])






















