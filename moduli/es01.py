lista_nomi = []
lista_spazio = [""]

def ElencoDocentiClasse(classe):
     
    USCITA = False
    lista_nomi = []
    file = open('C:\\Users\\20346\\Desktop\\sphinx\\moduli\\OrarioTabellaGlobale.csv','r')

    r = file.readline().strip().split(',')
    while not(USCITA):
        if r == lista_spazio:
            USCITA = True
        else:
            if classe in r:
                lista_nomi.append(r[0].strip())
        
        r = file.readline().strip().split(',')

    print(lista_nomi)      

    file.close()
    return
