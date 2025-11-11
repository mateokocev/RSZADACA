class Student(object):
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene

    def prosjek(self):
        return sum(self.ocjene) / len(self.ocjene)

    def ispis(self):
        print(f"Ime: {self.ime}")
        print(f"Prezime: {self.prezime}")
        print(f"Godine: {self.godine}")
        print(f"Ocjene: {self.ocjene}")
        print(f"Prosjek: {self.prosjek():.2f}")