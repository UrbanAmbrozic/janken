import random

def zmaga(vnos: str, poteza_prog: str) -> bool | None:
    if vnos == poteza_prog:
        return(None)
    elif vnos == 'papir' and poteza_prog == 'kamen':
        return(True)
    elif vnos == 'kamen' and poteza_prog == 'škarje':
        return(True)
    elif vnos == 'škarje' and poteza_prog == 'papir':
        return(True)
    else:
        return(False)
    
def sporočilo(vnos: str, poteza_prog: str, rezultat: bool) -> None:
    print("---------------------------------------")
    print("---------------------------------------")
    print(f"    Tvoja poteza:    {vnos}")
    print(f"    Moja poteza:     {poteza_prog}")
    print("---------------------------------------")

    if rezultat is None:
        print("    Izenačena igra...")
    elif rezultat is True:
        print("    Zmaga je tvoja!")
    elif rezultat is False:
        print("    Več sreče prihodnjič.")
    
    print("---------------------------------------")
    print("---------------------------------------")
    
def main() -> None:
    poteze: list[str] = ['kamen', 'papir', 'škarje']
    
    print("Hello! Igrajva JANKEM! ")

    while True:
        poteza_prog: str = random.choice(poteze)
        vnos: str = input("Izberi kamen, papir ali škarje: ").lower()

        if vnos not in poteze:
            print("Nisem te razumel. Prosim, ponovi svojo potezo.")
            continue

        rezultat = zmaga(vnos, poteza_prog)

        sporočilo(vnos, poteza_prog, rezultat)

        while True:
            odgovor = input("Ali želiš igrati ponovno? (da/ne): ")

            if odgovor == 'da':
                break
            elif odgovor == 'ne':
                print("Hvala za igro.")
                exit()
            else:
                print("Nisem razumel tvojega odgovora.")
                pass

if __name__ == '__main__':
    main()
                

            

    


    
    

