
# def bolish(a, b):
#     if b == 0:
#         raise ZeroDivisionError("0 ga bo'lish mumkin emas.")
#     return a / b
# try:
#         natija = bolish(10, 0)
#         print(f"Natija: {natija}")
# except ZeroDivisionError as e:
#         print(f"Xatolik: {e}")
# bolish(12,6)





while True:
    try:
        matn = input("harf kiriting:")
        matn = float(matn)
        print("Xatolik! Harf kiritilmadi!")
        break
    except:
        print("Xarf kiritildi!")
        break