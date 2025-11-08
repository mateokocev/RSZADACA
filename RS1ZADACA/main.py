import random
def izbornik():
    print("\n/// Izbornik zadataka (1–16) ///")
    print("Odaberi broj zadatka koji želiš pokrenuti:")
    try:
        zadatak = int(input("Unesi broj zadatka: "))
    except ValueError:
        print("Neispravan unos! Potrebno je unijeti broj od 1 do 16.")
        return izbornik()
    pokreni_zadatak(zadatak)


def pokreni_zadatak(zadatak):
    match zadatak:
        case 1:
            try:
                print("Jadni kalkulator.")
                djeljenik = float(input("Unesi djeljenik (prvi broj): "))
                djelitelj = float(input("Unesi djelitelj (drugi broj): "))
                operator = input("Unesi operator (+, -, *, /): ")

                match operator:
                    case '+':
                        rezultat = djeljenik + djelitelj
                        print(f"Rezultat je {rezultat}")
                    case '-':
                        rezultat = djeljenik - djelitelj
                        print(f"Rezultat je {rezultat}")
                    case '*':
                        rezultat = djeljenik * djelitelj
                        print(f"Rezultat je {rezultat}")
                    case '/':
                        if djelitelj == 0:
                            print("Dijeljenje s nulom nije dozvoljeno!")
                            return izbornik()
                        else:
                            rezultat = djeljenik / djelitelj
                            print(f"Rezultat operacije {djeljenik} / {djelitelj} je {rezultat}")
                    case _:
                        print("Nepodržani operator!")
                        return izbornik()
            except ValueError:
                print("Neispravan unos broja!")
                return izbornik()

        case 2:
            try:
                print("Provjera prijestupne godine.")
                godina = int(input("Unesi godinu za provjeru: "))

                if (godina % 4 == 0 and godina % 100 != 0) or (godina % 400 == 0):
                    print(f"Godina {godina}. je prijestupna.")
                else:
                    print("Godina {godina}. nije prijestupna.")
            except ValueError:
                print("Neispravan unos godine!")
                return izbornik()

        case 3:
            try:
                tajniBroj = random.randint(1, 100)
                print(tajniBroj)
                uspjesniPogodak = False
                pokusaji = 0

                while not uspjesniPogodak:
                    try:
                        pogodak = int(input("Unesi broj za pokušaj (1–100): "))
                        pokusaji += 1

                        if pogodak < tajniBroj:
                            print("Traženi broj je veći.")
                        elif pogodak > tajniBroj:
                            print("Traženi broj je manji.")
                        else:
                            uspjesniPogodak = True
                            print(f"Bravo, pogodio si u {pokusaji} pokušaja.")
                    except ValueError:
                        print("Neispravan unos! Potrebno je unijeti broj.")
                        continue
            except Exception:
                print("Došlo je do pogreške!")
                return izbornik()

        case 4:
            try:
                zbroj = 0
                while True:
                    broj = int(input("Unesi cijeli broj (0 za kraj): "))
                    if broj == 0:
                        break
                    zbroj += broj
                print(f"Zbroj unesenih brojeva je {zbroj}.")
            except ValueError:
                print("Neispravan unos! Potrebno je unijeti cijeli broj.")
                return izbornik()

        case 5:
            return
        case 6:
            return
        case 7:
            return
        case 8:
            return
        case 9:
            return
        case 10:
            return
        case 11:
            return
        case 12:
            return
        case 13:
            return
        case 14:
            return
        case 15:
            return
        case 16:
            return
        case _:
            print("Neispravan broj zadatka! Odaberi između 1 i 16.")
            return izbornik()

    ponovi = input("\nŽeliš li se vratiti na glavni izbornik? (da/ne): ").lower()
    if ponovi == "da":
        izbornik()


if __name__ == "__main__":
    izbornik()
