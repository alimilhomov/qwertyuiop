def davlat_info(davlat,poytaxt,yer_moydoni,axolosi,pul_birligi):
    davlat ={'mamlakat': davlat,
            'poytaxt': poytaxt,
            'yer_moydoni': yer_moydoni,
            'axolosi': axolosi,
            'pul_birligi': pul_birligi}
    return davlat
def davlat_kirit(mamlakat, poytaxt,yer_moydoni,axolosi,pul_birligi):
    davlatlar =[]
    while True:
        mamlakat = input('Mamlakat nomini kiriting: ')
        axolosi = int(input('Axolisini kiriting:'))
        poytaxt = input('poytaxt nomini kiriting: ')
        yer_moydoni =int(input('Yer moydoni nomini kiriting: '))
        pul_birligi = input('pul_birligi kiriting: ')
        davlatlar.append(davlat_info(mamlakat,axolosi,poytaxt,yer_moydoni,pul_birligi))
        javob = input('Yana mamlakat kiritasizmi: yes/no: ')
        if javob.lower() == 'no':
            break
        return davlatlar

def info_davlatlar(davlat_info):
    print(f"{davlat_info['mamlakat'].title()}"
        f"{davlat_info['poytaxt'].title()}"
        f"{davlat_info['yer_moydoni']}"
        f"{davlat_info['pul_birligi'].upper()}")
    











