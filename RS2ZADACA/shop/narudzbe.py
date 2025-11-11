from shop.proizvodi import skladiste


class Narudzba:
    def __init__(self, naruceniProizvodi, ukupnaCijena):
        self.naruceniProizvodi = naruceniProizvodi
        self.ukupnaCijena = ukupnaCijena

    def ispisNarudzbe(self):
        artikli = ", ".join(
            [f"{p['naziv']} x {p['narucenaKolicina']}" for p in self.naruceniProizvodi]
        )
        print(f"Naručeni proizvodi: {artikli}, Ukupna cijena: {self.ukupnaCijena} €")


narudzbe = []


def napraviNarudzbu(naruceniProizvodi):
    if not isinstance(naruceniProizvodi, list):
        print("Greška: naruceniProizvodi mora biti lista!")
        return None
    if not naruceniProizvodi:
        print("Greška: lista naručenih proizvoda ne smije biti prazna!")
        return None

    for p in naruceniProizvodi:
        if not isinstance(p, dict):
            print("Greška: svaki element mora biti rječnik!")
            return None
        if not all(k in p for k in ("naziv", "cijena", "narucenaKolicina")):
            print("Greška: nedostaje ključ u nekom proizvodu!")
            return None

    for p in naruceniProizvodi:
        proizvodUSkladistu = next((s for s in skladiste if s.naziv == p["naziv"]), None)
        if proizvodUSkladistu is None or proizvodUSkladistu.dostupnaKolicina < p["narucenaKolicina"]:
            print(f"Proizvod {p['naziv']} nije dostupan!")
            return None

    ukupnaCijena = sum(p["cijena"] * p["narucenaKolicina"] for p in naruceniProizvodi)
    novaNarudzba = Narudzba(naruceniProizvodi, ukupnaCijena)
    narudzbe.append({"narudzba": novaNarudzba})
    return novaNarudzba