import random

from mpmath.math2 import sqrt2, sqrt
from sympy import isprime, primerange, factorial
import heapq

def izbornik():
    print("\n/// Izbornik zadataka (1–5) ///")
    print("Odaberi broj zadatka koji želiš pokrenuti:")

    try:
        zadatak = int(input("Unesi broj zadatka: "))
    except ValueError:
        print("Neispravan unos! Potrebno je unijeti broj od 1 do 5.")
        return izbornik()
    pokreni_zadatak(zadatak)


def pokreni_zadatak(zadatak):
    match zadatak:
        case 1:
            try:
                nizBrojeva = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

                kvadriraj = lambda x : x ** 2
                print(kvadriraj(2))

                zbrojiPaKvadriraj = lambda x, y : (x + y) ** 2
                print(zbrojiPaKvadriraj(2, 2))

                kvadrirajDuljinu = lambda x : len(x) ** 2
                print(kvadrirajDuljinu(nizBrojeva))

                pomnoziPotenciraj = lambda x, y : (y * 5) ** x
                print(pomnoziPotenciraj(2, 2))

                paranBroj = lambda x : True if x % 2 == 0 else None
                print(paranBroj(3))
            except Exception:
                print("Dogodila se pogreška!")
                return izbornik()

        case 2:
            try:
                nizovi = ["jabuka", "kruška", "banana", "naranča"]
                brojevi = [1, 21, 33, 45, 2, 2, 1, -32, 9, 10]
                brojeviTransform = [10, 5, 12, 15, 20]
                studenti = [
                    {"ime": "Ivan", "prezime": "Ivić", "godine": 19},
                    {"ime": "Marko", "prezime": "Marković", "godine": 22},
                    {"ime": "Ana", "prezime": "Anić", "godine": 21},
                    {"ime": "Petra", "prezime": "Petrić", "godine": 13},
                    {"ime": "Iva", "prezime": "Ivić", "godine": 17},
                    {"ime": "Mate", "prezime": "Matić", "godine": 18}
                ]
                rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples",
                          "pjesma", "otorinolaringolog"]

                kvadriranjeDuljine = list(map(lambda x : len(x) ** 2, nizovi))
                print(kvadriranjeDuljine)

                veciOdPet = list(filter(lambda x : x > 5, brojevi))
                print(veciOdPet)

                transform = dict(map(lambda x : (x, x ** 2), brojeviTransform))
                print(transform)

                sviPunoljetni = all(map(lambda x : x["godine"] >= 18, studenti))
                print(sviPunoljetni)

                minDuljina = int(input("Unesite minimalnu duljinu riječi: "))
                dugeRijeci = list(filter(lambda x : len(x) > minDuljina, rijeci))
                print(dugeRijeci)
            except Exception:
                print("Dogodila se pogreška!")
                return izbornik()

        case 3:
            try:
                rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples",
                          "pjesma", "otorinolaringolog"]
                studenti = [
                    {"ime": "Ivan", "prezime": "Ivić", "bodovi": [12, 23, 53, 64]},
                    {"ime": "Marko", "prezime": "Marković", "bodovi": [33, 15, 34, 45]},
                    {"ime": "Ana", "prezime": "Anić", "bodovi": [8, 9, 4, 23, 11]},
                    {"ime": "Petra", "prezime": "Petrić", "bodovi": [87, 56, 77, 44, 98]},
                    {"ime": "Iva", "prezime": "Ivić", "bodovi": [23, 45, 67, 89, 12]},
                    {"ime": "Mate", "prezime": "Matić", "bodovi": [75, 34, 56, 78, 23]}
                ]

                parniKvadrati = [x ** 2 for x in range(20, 51)]
                print(parniKvadrati)

                DuljineAliSamoA = [len(x) for x in rijeci if "a" in x]
                print(DuljineAliSamoA)

                kuboviNeparnih = [{x : x ** 3 if x % 2 != 0 else x} for x in range(1,11)]
                print(kuboviNeparnih)

                korijeni = {x : round(sqrt(x),2) for x in range(50, 501, 50)}
                print(korijeni)

                zbrojeniBodovi = [{x["prezime"] : sum(x["bodovi"]) } for x in studenti]
                print(zbrojeniBodovi)

                faktorijeli = {x : [factorial(x) for x in range(1, x + 1)] for x in range(1, 11)}
                print(faktorijeli)
            except Exception:
                print("Dogodila se pogreška!")
                return izbornik()

        case 4:
            try:
                pass
            except Exception:
                print("Dogodila se pogreška!")
                return izbornik()

        case 5:
            try:
                pass
            except Exception:
                print("Dogodila se pogreška!")
                return izbornik()

        case _:
            print("Neispravan broj zadatka! Odaberi između 1 i 5.")
            return izbornik()

    ponovi = input("\nŽeliš li se vratiti na glavni izbornik? (da/ne): ").lower()
    if ponovi == "da":
        izbornik()


if __name__ == "__main__":
    izbornik()
