#Le prenotazioni per la partecipazione a un convegno sono memorizzate secondo l'ordine di arrivo.
#Scrivi un programma che comprenda due funzionalità:
# - l'operazione per registrare i dati dei partecipanti;
# - l'operazione per visualizzare i nomi dei partecipanti a cui si deve inviare una lettera di conferma: si 
# tratta dei nomi dell'elenco, eliminando quelli ai quali la lettera è già stata inviata e che sono registrati 
# in un apposito elenco. La funzione che produce l'elenco deve anche aggiornare l'elenco dei partecipanti 
# ai quali è già stata inviata la lettera.

partecipanti = []
lettera_inviata = []
lettera_mancante = []
coda = int(input("Quanti partecipanti sono in coda? " ))
n = 1

for i in range(coda):
    print("Come si chiama il partecipante numero", n,"? ")
    partecipante = input()
    n += 1
    età = int(input("Quanti anni ha? "))
    sesso = input("Maschio o femmina? ")
    lettera = input("Ha ricevuto la lettera?(rispondere solo con Sì, con l'accento, o No) ").upper()
    partecipante = {'nome': partecipante,
                    'età': età,
                    'sesso': sesso}
    partecipanti.append(partecipante)
    
    if lettera == "SÌ":
        lettera_inviata.append(partecipante)
    elif lettera == "NO":
        lettera_mancante.append(partecipante)
    else:
        print("ERRORE: la risposta non è stata scritta in modo corretto.")
        break

print()
print("Questo è l'elenco dei dati di tutti i partecipanti:")
print(partecipanti)
print("Questo è l'elenco dei dati dei partecipanti ai quali deve ancora essere inviata la lettera di conferma:")
print(lettera_mancante)
print("Questo è l'elenco dei dati dei partecipanti ai quali è già stata inviata la lettera di conferma:")
print(lettera_inviata)
