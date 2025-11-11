from datetime import datetime

class Automobil:
    def __init__(self, marka, model, godinaProizvodnje, kilometraza):
        self.marka = marka
        self.model = model
        self.godinaProizvodnje = godinaProizvodnje
        self.kilometraza = kilometraza


    def ispis(self):
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Godina proizvodnje: {self.godinaProizvodnje}")
        print(f"Kilometraza: {self.kilometraza}")

    def starost(self):
        trenutnaGodina = datetime.now().year
        godinaStarosti = trenutnaGodina - self.godinaProizvodnje
        print(f"Automobil je star {godinaStarosti} godina.")