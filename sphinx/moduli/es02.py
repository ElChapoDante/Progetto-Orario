lista_nomi = []
lista_orario = []
lista_spazio = [""]



def OrarioDocente(nome):
    '''
    Funzione: orario di un determinato docente e numero totale delle ore del docente
    Parametri: nome
    return: vuoto
    '''
    
    file = open('C:\\Users\\20346\\Desktop\\sphinx\\moduli\\OrarioTabellaGlobale.csv','r')
    leggi_riga = file.readline().strip()
    
    while leggi_riga != "":
        lista_riga = leggi_riga.split(',')
        for i in range(len(lista_riga)):
            lista_riga[i] = lista_riga[i].strip()
        lista_nomi.append(lista_riga[0])
        leggi_riga = file.readline().strip()
        
    lista_nomi.pop(0)
    lista_nomi.pop(0)
        
        
    file.close()

    uscita = False

    file = open('C:\\Users\\20346\\Desktop\\sphinx\\moduli\\OrarioTabellaGlobale.csv','r')
    while not uscita:
        if  leggi_riga == lista_spazio:
            uscita = True
        else:
            lista_orario.append(leggi_riga[2:])
            leggi_riga = file.readline().strip().split(',')
        
    lista_giorni = []
    lista_giorni.append(lista_orario[0])
    lista_orario.pop(0)

    lista_giorni.append(lista_orario[0])
    lista_orario.pop(0)

    lista_orario.pop(0)


    file.close()
    
    dizionario = dict(zip(lista_nomi, lista_orario))
    print(dizionario[nome])
	
    return



#nome = input("Inserisci il Cognome Nome: ").upper()
#OrarioDocente(nome)
#print("lista nomi: ", lista_nomi)
#print("lista oraio: ", lista_orario)
#dizionario = dict(zip(lista_nomi, lista_orario))


#print(dizionario)
#print(dizionario[nome])

    
