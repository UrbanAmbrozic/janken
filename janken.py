import random

poteze: list[str] = ['kamen', 'papir', 'škarje']

poteza_prog: str = str()



def zmaga(vnos, poteza_prog) -> bool | None:
    if vnos == poteza_prog:
        return(None)
    elif vnos == 'papir' and poteza_prog == 'škarje':
        return(False)
    elif vnos == 'papir' and poteza_prog == 'kamen':
        return(True)
    elif vnos == 'kamen' and poteza_prog == 'papir':
        return(False)
    elif vnos == 'kamen' and poteza_prog == 'škarje':
        return(True)
    elif vnos == 'škarje' and poteza_prog == 'kamen':
        return(False)
    elif vnos == 'škarje' and poteza_prog == 'papir':
        return(True)


print("Hello! Igrajva JANKEM! ")



while True:
    poteza_prog: str = random.choice(poteze)
    vnos: str = input("Izberi kamen, papir ali škarje: ").lower()

    if vnos not in poteze:
        print("Nisem te razumel. Prosim, ponovi svojo potezo.")
        continue

    result = zmaga(vnos, poteza_prog)

    print("---------------------------------------")
    print("---------------------------------------")
    print(f"Moja poteza:     {poteza_prog}")
    print(f"Tvoja poteza:    {vnos}")
    print("---------------------------------------")

    if result is None:
        print("Izenačena igra...")
    elif result is True:
        print("Zmaga je tvoja!")
    elif result is False:
        print("Več sreče prihodnjič.")
    
    print("---------------------------------------")
    print("---------------------------------------")

    while True:
        odgovor = input("Ali želiš igrati ponovno? (da/ne) ")

        if odgovor == 'da':
            break
        elif odgovor == 'ne':
            print("Hvala za igro.")
            exit()
        else:
            print("Nisem razumel tvojega odgovora.")
            pass

                

            

    


    
    

