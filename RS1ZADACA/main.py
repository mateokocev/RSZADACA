import random
from sympy import isprime, primerange
import heapq

def izbornik():
    print("\n/// Izbornik zadataka (1–17) ///")
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
            # 1. petlja definira in range(1,2) gdje je gornja granica isključiva. Dakle petlja će ispisati samo broj 1 i zaustaviti se, što pobija svrhu implementacije iteracije u kojem je garantirano da ispisuje samo 1. element u svakom slučaju.
            # 2. petlja ide od nižeg do višeg broja sa prijestupom od 2, pošto je početni broj 10 viši od ciljanog broja 1, petlja neće ispisati ništa.
            # 3. petlja će ispisati brojeve 10,9,8,7,6,5,4,3,2 bez broja 1 pošto je ciljava granica isključiva.
        case 6:
            try:
                zbroj = 0
                for i in range(2, 101, 2):
                    zbroj += i
                print(f"Zbroj svih parnih brojeva od 1 do 100 je {zbroj}.")

                zbroj = 0
                i = 2
                while i <= 100:
                    zbroj += i
                    i += 2
                print(f"Zbroj svih parnih brojeva od 1 do 100 je {zbroj}.")

                neparni = [i for i in range(1, 20, 2)]
                for broj in reversed(neparni):
                    print(broj)

                neparni = [i for i in range(1, 20, 2)]
                i = len(neparni) - 1
                while i >= 0:
                    print(neparni[i])
                    i -= 1

                a, b = 0, 1
                print(a)
                print(b)
                for _ in range(1000):
                    sljedeci = a + b
                    if sljedeci > 1000:
                        break
                    print(sljedeci)
                    a, b = b, sljedeci

                a, b = 0, 1
                print(a)
                print(b)
                while True:
                    sljedeci = a + b
                    if sljedeci > 1000:
                        break
                    print(sljedeci)
                    a, b = b, sljedeci


            except Exception:
                print("Došlo je do pogreške!")
                return izbornik()

        case 7:
            try:
                def provjeraLozinke(lozinka):

                    if "password" in lozinka.lower() or "lozinka" in lozinka.lower():
                        print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'.")
                        return

                    if len(lozinka) < 8 or len(lozinka) > 15:
                        print("Lozinka mora sadržavati između 8 i 15 znakova.")
                        return

                    imaVeliko = any(slovo.isupper() for slovo in lozinka)
                    imaBroj = any(slovo.isdigit() for slovo in lozinka)
                    if not (imaVeliko and imaBroj):
                        print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj.")
                        return

                lozinka = input("Unesi lozinku: ")
                provjeraLozinke(lozinka)

            except Exception:
                print("Došlo je do pogreške prilikom unosa lozinke!")
                return izbornik()

        case 8:
            try:
                def filtrirajParne(lista):
                    return list(filter(lambda x: x % 2 == 0, lista))

                lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                print(f"Originalna lista: {lista}")
                print(f"Parni brojevi: {filtrirajParne(lista)}")

            except Exception:
                print("Došlo je do pogreške prilikom obrade liste!")
                return izbornik()

        case 9:
            try:
                def ukloniDuplikate(lista):
                    return list(set(lista))

                lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
                print(f"Originalna lista: {lista}")
                print(f"Lista bez duplikata: {ukloniDuplikate(lista)}")

            except Exception:
                print("Došlo je do pogreške prilikom obrade liste!")
                return izbornik()

        case 10:
            try:
                def brojanjeRijeci(tekst):
                    rijeci = tekst.split()
                    rezultat = {}
                    for rijec in rijeci:
                        if rijec in rezultat:
                            rezultat[rijec] += 1
                        else:
                            rezultat[rijec] = 1
                    return rezultat

                tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
                print(f"Tekst: {tekst}")
                print(brojanjeRijeci(tekst))

            except Exception:
                print("Došlo je do pogreške prilikom obrade teksta!")
                return izbornik()

        case 11:
            try:
                grupirajPoParitetu = lambda lista: {
                    'parni': list(filter(lambda x: x % 2 == 0, lista)),
                    'neparni': list(filter(lambda x: x % 2 != 0, lista))
                }

                lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                print(f"Originalna lista: {lista}")
                print(grupirajPoParitetu(lista))

            except Exception:
                print("Došlo je do pogreške prilikom obrade liste!")
                return izbornik()

        case 12:
            try:
                def obrniRjecnik(rjecnik):
                    return {vrijednost: kljuc for kljuc, vrijednost in rjecnik.items()}

                rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}
                print(f"Originalni rječnik: {rjecnik}")
                print(f"Obrnuti rječnik: {obrniRjecnik(rjecnik)}")

            except Exception:
                print("Došlo je do pogreške prilikom obrade rječnika!")
                return izbornik()

        case 13:
            try:
                prviZadnji = lambda lista: (lista[0], lista[-1])
                lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                print(prviZadnji(lista))


                maksMin = lambda lista: (max(lista), min(lista))
                lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]
                print(maksMin(lista))

                presjek = lambda prviSkup, drugiSkup: prviSkup & drugiSkup
                prviSkup = {1, 2, 3, 4, 5}
                drugiSkup = {4, 5, 6, 7, 8}
                print(presjek(prviSkup, drugiSkup))

            except Exception:
                print("Došlo je do pogreške prilikom obrade liste!")
                return izbornik()

        case 14:
            try:
                isPrime = lambda n: isprime(n)
                primesInRange = lambda start, end: list(primerange(start, end))

                print(isPrime(7))
                print(isPrime(10))
                print(primesInRange(1, 10))

            except Exception:
                print("Došlo je do pogreške prilikom obrade brojeva!")
                izbornik()

        case 15:
            try:


                countVowelsConsonants = lambda tekst: {
                    "vowels": sum(1 for slovo in tekst if slovo in vowels),
                    "consonants": sum(1 for slovo in tekst if slovo in consonants),
                }

                vowels = "aeiouAEIOU"
                consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
                tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
                print(countVowelsConsonants(tekst))

            except Exception:
                print("Došlo je do pogreške prilikom obrade stringa!")
                izbornik()

        case 16:
            try:
                def dijkstra(graph, start):
                    daljine = {cvor: float('inf') for cvor in graph}
                    daljine[start] = 0
                    pq = [(0, start)]

                    while pq:
                        trenutacnaDaljina, trenutacniCvor = heapq.heappop(pq)

                        if trenutacnaDaljina > daljine[trenutacniCvor]:
                            continue

                        for susjed, tezina in graph[trenutacniCvor]:
                            daljina = trenutacnaDaljina + tezina

                            if daljina < daljine[susjed]:
                                daljine[susjed] = daljina
                                heapq.heappush(pq, (daljina, susjed))

                    return daljine

                graph = {
                    'A': [('B', 1), ('C', 4)],
                    'B': [('A', 1), ('C', 2), ('D', 5)],
                    'C': [('A', 4), ('B', 2), ('D', 1)],
                    'D': [('B', 5), ('C', 1)]
                }
                print(dijkstra(graph, 'A'))

            except Exception:
                print("Došlo je do pogreške prilikom izvršavanja algoritma!")
                return izbornik()

        case 17:
            try:
                def validirajBrojTelefona(broj: str):
                    fiksni = {
                        "01": "Grad Zagreb i Zagrebačka županija",
                        "020": "Dubrovačko-neretvanska županija",
                        "021": "Splitsko-dalmatinska županija",
                        "022": "Šibensko-kninska županija",
                        "023": "Zadarska županija",
                        "031": "Osječko-baranjska županija",
                        "032": "Vukovarsko-srijemska županija",
                        "033": "Virovitičko-podravska županija",
                        "034": "Požeško-slavonska županija",
                        "035": "Brodsko-posavska županija",
                        "040": "Međimurska županija",
                        "042": "Varaždinska županija",
                        "043": "Bjelovarsko-bilogorska županija",
                        "044": "Sisačko-moslavačka županija",
                        "047": "Karlovačka županija",
                        "048": "Koprivničko-križevačka županija",
                        "049": "Krapinsko-zagorska županija",
                        "051": "Primorsko-goranska županija",
                        "052": "Istarska županija",
                        "053": "Ličko-senjska županija"
                    }

                    mobilni = {
                        "091": "A1 Hrvatska",
                        "092": "Tomato",
                        "095": "Telemach",
                        "097": "bonbon",
                        "098": "Hrvatski Telekom",
                        "099": "Hrvatski Telekom"
                    }

                    posebni = {
                        "0800": "Besplatni pozivi",
                        "060": "Komercijalni pozivi",
                        "061": "Glasovanje telefonom",
                        "064": "Usluge s neprimjerenim sadržajem",
                        "065": "Nagradne igre",
                        "069": "Usluge namijenjene djeci",
                        "072": "Jedinstveni pristupni broj"
                    }

                    rezultat = {
                        "pozivni_broj": None,
                        "broj_ostatak": None,
                        "vrsta": None,
                        "mjesto": None,
                        "operater": None,
                        "validan": False
                    }

                    ocisti = lambda brojTelefona: "".join(broj for broj in brojTelefona if broj.isdigit() or broj == "+")
                    isValidLength = lambda s, dozvoljene: s.isdigit() and len(s) in dozvoljene

                    broj = ocisti(broj)

                    for prefiks in ("+385", "00385", "385", "0"):
                        if broj.startswith(prefiks):
                            broj = broj[len(prefiks):]
                            break

                    if not broj.startswith("0"):
                        broj = "0" + broj

                    svi = {**fiksni, **mobilni, **posebni}
                    pozivni = next((poz for poz in sorted(svi, key=len, reverse=True) if broj.startswith(poz)), None)

                    if not pozivni:
                        return rezultat

                    ostatak = broj[len(pozivni):]
                    rezultat["pozivni_broj"] = pozivni
                    rezultat["broj_ostatak"] = ostatak

                    match pozivni:
                        case pozivni if pozivni in fiksni:
                            rezultat["vrsta"] = "fiksna mreža"
                            rezultat["mjesto"] = fiksni[pozivni]
                            rezultat["operater"] = None
                            rezultat["validan"] = isValidLength(ostatak, (6, 7))

                        case pozivni if pozivni in mobilni:
                            rezultat["vrsta"] = "mobilna mreža"
                            rezultat["mjesto"] = None
                            rezultat["operater"] = mobilni[pozivni]
                            rezultat["validan"] = isValidLength(ostatak, (6, 7))

                        case pozivni if pozivni in posebni:
                            rezultat["vrsta"] = "posebne usluge"
                            rezultat["mjesto"] = None
                            rezultat["operater"] = None
                            rezultat["validan"] = isValidLength(ostatak, (6,))

                    return rezultat

                print(validirajBrojTelefona("+385989876543"))

            except Exception:
                print("Ipak ništa od telefonina.")
                return izbornik()

        case _:
            print("Neispravan broj zadatka! Odaberi između 1 i 17.")
            return izbornik()

    ponovi = input("\nŽeliš li se vratiti na glavni izbornik? (da/ne): ").lower()
    if ponovi == "da":
        izbornik()


if __name__ == "__main__":
    izbornik()
