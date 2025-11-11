from radnik import Radnik

class Manager(Radnik):
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department

    def work(self):
        print(f"Radim na poziciji {self.pozicija} u odjelu {self.department}")

    def giveRaise(self, radnik, povecanje):
        radnik.placa += povecanje
        print(f"Plaća radnika {radnik.ime} povećana je na {radnik.placa}.")