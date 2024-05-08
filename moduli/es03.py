def OreADisposizione(nome):
    lista_nomi = []
    lista_orario = []
    lista_spazio = [""]
    
    file = open('C:\\Users\\20346\\Desktop\\sphinx\\moduli\\OrarioTabellaGlobale.csv','r')
    leggi_riga = file.readline().strip()
    
    while leggi_riga != "":
        lista_riga = leggi_riga.split(',')
        for i in range(len(lista_riga)):
            lista_riga[i] = lista_riga[i].strip()
        lista_nomi.append(lista_riga[0])
        leggi_riga = file.readline()
    
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


    
    ####################
    lista_nomi = lista_nomi[2:]
    lista_orario = lista_orario[2:]

    #print(lista_orario)
    orario_docente = lista_orario[lista_nomi.index(nome)]
    
    
    D = orario_docente.count(' D ')

    print("Il numero di ore a disposizione è: ", D)
    file = open("OrarioDisposizione.txt", "w")

    file.close()
    return



