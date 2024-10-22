# import random

# # Qurollar va ularning zararlari
# weapons = {
#     "Qilich": (10, 20),  # Qilich zarari 10-20
#     "Bolta": (15, 25),   # Bolta zarari 15-25
#     "O'q-yoy": (5, 15)   # O'q-yoy zarari 5-15
# }

# # Foydalanuvchi sinfi
# class User:
#     def __init__(self, name):
#         self.name = name
#         self.health = 100

#     def attack(self, opponent):
#         # Tasodifiy qurol va zarar tanlash
#         weapon, damage_range = random.choice(list(weapons.items()))
#         damage = random.randint(damage_range[0], damage_range[1])
#         opponent.health -= damage
#         print(f"{self.name} {weapon} bilan hujum qilib, {damage} zarar berdi!")
#         print(f"{opponent.name}ning salomatligi: {opponent.health}")

# # Jang funksiyasi
# def fight(user1, user2):
#     print(f"Jang boshlanmoqda: {user1.name} vs {user2.name}")
    
#     # Har bir foydalanuvchi navbatma-navbat hujum qiladi
#     while user1.health > 0 and user2.health > 0:
#         user1.attack(user2)
#         if user2.health <= 0:
#             print(f"{user2.name} yutqazdi! {user1.name} g'olib!")
#             break
#         user2.attack(user1)
#         if user1.health <= 0:
#             print(f"{user1.name} yutqazdi! {user2.name} g'olib!")
#             break

# # Foydalanuvchilarni yaratamiz
# user1 = User("Alisher")
# user2 = User("Botir")

# # Jangni boshlaymiz
# fight(user1, user2)











# son1 = 0
# son2 = 1
# print(son1,end=" ")
# print(son2,end=" ")
# for i in range(10):
#     num = son1 + son2 
#     print(num,end=" ")
#     son1 = son2
#     son2 = num

def fib(n):
    a,b = 0,1
    for _ in range(n):
        a, b = b, a + b
        print(a, end=" ")
fib(10)