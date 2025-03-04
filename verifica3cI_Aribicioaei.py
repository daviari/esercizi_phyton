citta=['milano','roma','napoli']
tMax=[28,31,34]
tMin=[18,21,24]
mediaMax=31
mediaMin=21

while True:
    c=input("inserisci la città (milano roma napoli. inserisci stop per concludere): ")
    if c == "stop":
        print(" inserimento concluso")
        break

while True:
    t=int(input("inserisci la temperatura della città in ordine inserito (inserisci 00 per terminare): "))
    if t == 00:
        print("ERRORE")
        break
    print("la temperatura media massima è:" ,mediaMax)
    print("la temperatura media massima è:" ,mediaMin)
    print("la città più calda è :" ,citta[2])
    print("la città meno calda è :" ,citta[0])
