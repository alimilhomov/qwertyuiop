# from math import pi
# print(pi)


import random
ishlar = ["uy tozalash","kir yuvish","uy supurish"]
ismlar = ["alim","raxmatilla","izzat"]
random.shuffle(ishlar)
random.shuffle(ismlar)
for ism,ishlar in zip(ishlar,ismlar):
    print(f"{ism} {ishlar} bilan shugulanadi")





















