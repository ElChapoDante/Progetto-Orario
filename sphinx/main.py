import sys
sys.path.insert(1, "C:\\Users\\20346\\Desktop\\sphinx\\moduli")
import es01
import es02
import es03
import es04

def main():
    
    classe = input("Inserisci il nome della classe: ").upper()
    es01.ElencoDocentiClasse(classe)
     
    nome = input("Inserisci il Cognome Nome del prof di cui vuoi sapere le ore: ").upper()
    es02.OrarioDocente(nome)
    
    nome = input("Inserisci il Cognome Nome del prof di cui vuoi sapere le ore a disposizione: ").upper()
    es03.OreADisposizione(nome)
    
    Giorno = input("Inserisci il nome del giorno: ")
    Ora = input("Inserisci il numero dell'ora: ")
    es04.OraSpecifica(Giorno,Ora)
        
    
    return

main()