

# my = ['ona','ota',[15,56,[25,'opa','uka'],['aka']],2,5,8,'akam']
# def natija(my):
#     for i in my:
#         if type (i)== int:
#             print(i,end=" ")
#         elif type (i)== str:
#             print(i.upper(),end=" ")
#         elif type (i)== list:
#             for j in i :
#                 if type (j)== int:
#                     print(j,end=" ")     
#                 elif type (j) == str:
#                     print(j.upper(),end=" ")
#                 elif type(j)== list:
#                     for t in j :
#                         if type(t)== int:
#                             print(t, end=" ")
#                         elif type (t) == str:
                            # print(t.upper(),end=" ")
# natija(my)

son = int(input('Neshta odamni malumotini kiritmoq chisiz:'))
for i in range(son):
    
    t_yil = int(input(f"{i+1}-odamning tug'ilgan yilingizni kiriting: "))
    t_joy = input(f"{i+1}-odamning tug'ilgan joyingizni kiriting: ")
    email = input(f"{i+1}-odamning elektron manzilingizni kiriting: ")
    t_raq= int(input(f"{i+1}-odamning telefon raqamingizni kiriting: "))
    # jovob = input('Dasturni tugatishga(yes,no)kiriting:')
    # if jovob == "no":
        # break

    # ism +=1

    A1={
        "Tug'ilgan yil": t_yil,
        "Tug'ilgan joy": t_joy,
        "Elektron manzil": email,
        "Telefon raqam": t_raq}


for kalit, qiymat in A1.items():
    
    print(f"{son}{kalit}: {qiymat}")















