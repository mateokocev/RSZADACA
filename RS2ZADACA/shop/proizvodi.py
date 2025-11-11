class Proizvod:
    def __init__(self, naziv, cijena, dostupnaKolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupnaKolicina = dostupnaKolicina

    def ispis(self):
        print(f"Naziv: {self.naziv}, Cijena: {self.cijena} €, Dostupno: {self.dostupnaKolicina} kom")

skladiste = [
    Proizvod("Laptop", 1200, 5),
    Proizvod("Monitor", 300, 8)
]

def dodajProizvod(naziv, cijena, dostupnaKolicina):
    noviProizvod = Proizvod(naziv, cijena, dostupnaKolicina)
    skladiste.append(noviProizvod)
