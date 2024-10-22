my = ['ona','ota',[15,56,[25,'opa','uka'],['aka']],2,5,8,'akam']

def natija(my):
    for i in my:
        if type (i)== int:
            print(i,end=" ")
        elif type (i)== str:
            print(i.upper(),end=" ")
        elif type (i)== list:
            for j in i :
                if type (j)== int:
                    print(j,end=" ")     
                elif type (j) == str:
                    print(j.upper(),end=" ")
                elif type(j)== list:
                    for t in j :
                        if type(t)== int:
                            print(t, end=" ")
                        elif type (t) == str:
                            print(t.upper(),end=" ")
natija(my)
