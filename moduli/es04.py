def OraSpecifica(Giorno,Ora):
    lista_nomi = []
    lista_spazio = [""]
    lista_orario = []
    

    f = open('C:\\Users\\20346\\Desktop\\sphinx\\moduli\\OrarioTabellaGlobale.csv','r')

    indice_ore = {"Lunedi":0, "Martedi":8, "Mercoledi":16, "Giovedi":24, "Venerdi":32}

    Ora = int(Ora)

    indice = indice_ore[Giorno] + Ora - 1
    docenti_ora_giorno = []
    cont = 0

    for i in range(len(lista_orario)):
        if lista_orario[i][indice] != '   ':
            docenti_ora_giorno.append(lista_nomi[i])
            cont += 1
    f.close()
    file = open("OraSpecifica.txt",'w')
    for elmento in docenti_ora_giorno:
        file.write(elmento + "\n")
    file.write(f"Il numero di professori a lezione il {Giorno} alla {Ora} ora sono {cont}")
    
    file.close()
    return



