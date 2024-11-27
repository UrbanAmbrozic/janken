import random

class Janken:
    def __init__(self) -> None:
        print("Hello! Igrajva JANKEN! ")

        self.poteze: dict =  {"kamen": "trd kamen", "papir": "mehek papir", "škarje": "ostre škarje"}  # Definirane poteze igre in odgovarjajoči simboli
        self.dovoljene_poteze: list[str] = list(self.poteze.keys())   # Definiranje dovoljenih potez, ki jih specificiramo kot {ključe} s seznama 'poteze'

    def igra(self) -> None:
        poteza_igralca: str = input("Izberi kamen, papir ali škarje: ").lower()
        poteza_rač: str = random.choice(self.dovoljene_poteze)  # Uporaba seznama dovoljenih potez za generacijo naključne poteze računalnika

        if poteza_igralca in ["izhod", "prekini", "x"]:    # Možnost izhoda
            print("Nasvidenje.")
            exit()
        
        if poteza_igralca not in self.dovoljene_poteze:   # Zajem nepravilnega odgovora
            print("Nisem te razumel. Prosim, ponovi svojo potezo.")
            return self.igra()  # Nazaj na začetek loop-a 'igra'
        
        self.pokaži_poteze(poteza_igralca, poteza_rač)    # Trigger za print potez igre
        self.rezultat(poteza_igralca, poteza_rač)     # Trigger za preverjanje rezultata igre
        self.nadaljevanje()

    def pokaži_poteze(self, poteza_igralca: str, poteza_rač: str) -> str:  # Print statements za status potez
        print("---------------------------------------")
        print("---------------------------------------")
        print(f"    Tvoja poteza:   {self.poteze[poteza_igralca]}")
        print(f"    Moja poteza:    {self.poteze[poteza_rač]}")
        print("---------------------------------------")
    
    def rezultat(self, poteza_igralca: str, poteza_rač: str) -> str:   # Preverjanje rezultata
        if poteza_igralca == poteza_rač:
            print("    Izenačena igra...")
        elif poteza_igralca == 'kamen' and poteza_rač == 'papir':
            print("    Več sreče prihodnjič.")
        elif poteza_igralca == 'papir' and poteza_rač == 'škarje':
            print("    Več sreče prihodnjič.")
        elif poteza_igralca == 'škarje' and poteza_rač == 'kamen':
            print("    Več sreče prihodnjič.")
        else:
            print("    Zmaga je tvoja!")
        
        print("---------------------------------------")
        print("---------------------------------------")
    
    def nadaljevanje(self) -> bool:                                     # Možnost nadaljevanja
        odgovor: str = input("Ali želiš igrati ponovno? (da/ne): ")
        if odgovor == "da":
            return self.igra()
        elif odgovor in ["ne", "izhod", "prekini", "x"]:
            print("Hvala za igro.")
            exit()
        else:
            print("Nisem razumel tvojega odgovora.")
            return self.nadaljevanje()



if __name__ == '__main__':
    nova_igra = Janken()    # Nova instanca igre, glede na definicijo "class"-a

    while True:     # Tek igre do preklica
        nova_igra.igra()    # Trigger za začetek igre (po definiciji iz "class"-a)


