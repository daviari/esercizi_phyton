lancio1=float(input("inserisci la lunghezza del primo lancio"))
lancio2=float(input("inserisci la lunghezza del secondo lancio"))
lancio3=float(input("inserisci la lunghezza del terzo lancio"))
lancio4=float(input("inserisci la lunghezza del quarto lancio"))
lancio5=float(input("inserisci la lunghezza del quinto lancio"))
if (lancio1==0):
    print("il lancio è nullo ")
    media1=((lancio2+lancio3+lancio4+lancio5)/4)
    print(f"la media è{media1}")
elif(lancio1>0):
    media2=((lancio1+lancio2+lancio3+lancio4+lancio5)/5)
    print(f"la media è{media2}")
elif(lancio2==0):
    print("il lancio è nullo ")
    media3=((lancio1+lancio3+lancio4+lancio5)/4)
    print(f"la media è{media3}")
elif(lancio2>0):
    media4=((lancio1+lancio2+lancio3+lancio4+lancio5)/5)
    print(f"la media è{media4}")
elif(lancio3==0):
    print("il lancio è nullo ")
    media5=((lancio1+lancio2+lancio4+lancio5)/4)
    print(f"la media è{media5}")
elif(lancio3>0):
    media6=((lancio2+lancio3+lancio4+lancio5)/5)
    print(f"la media è{media6}")
elif(lancio4==0):
    print("il lancio è nullo ")
    media7=((lancio1+lancio2+lancio5)/4)
    print(f"la media è{media7}")
elif(lancio4>0):
    media8=((lancio1+lancio2+lancio3+lancio4+lancio5)/5)
    print(f"la media è{media8}")
elif(lancio5==0):
    print("il lancio è nullo ")
    media9=((lancio1+lancio2+lancio4+lancio3)/4)
    print(f"la media è{media9}")
elif(lancio5>0):
    media10=((lancio1+lancio3+lancio4+lancio5)/5)
    print(f"la media è{media10}")





