import asyncio
import time
import random


#/////////////////////////////////////////////////////////////////////////// PRVI ZADATAK

async def simulacijaWebRequesta():
    print('Web zahtjev započet.')
    await asyncio.sleep(3)
    podaci = [i for i in range(1, 11)]
    print("Podaci dohvaćeni.")
    return podaci

#/////////////////////////////////////////////////////////////////////////// DRUGI ZADATAK

async def getWebKorisnike():
    print('Web zahtjev započet.')
    await asyncio.sleep(3)
    podaci = [
        {'user': 'Marko', 'email': 'marko@gmail.com', 'password': 'nekihash123'},
        {'user': 'Stevo', 'email': 'stevo@gmail.com', 'password': 'nekihash123'},
        {'user': 'Leo', 'email': 'leo@gmail.com', 'password': 'nekihash123'},
    ]
    print("Podaci dohvaćeni.")
    return podaci

async def getWebProizvode():
    print('Web zahtjev započet.')
    await asyncio.sleep(5)
    podaci = [
        {'imeProizvoda': 'Crocs', 'opisProizvoda': 'Plasticne slape', 'productPrice': '13.99'},
        {'imeProizvoda': 'Mrkva', 'opisProizvoda': 'Povrce', 'productPrice': '17.99'},
        {'imeProizvoda': 'Jabuka', 'opisProizvoda': 'Voce', 'productPrice': '2.99'},
    ]
    print("Podaci dohvaćeni.")
    return podaci

async def drugiZadatak():
    timerOne = time.perf_counter()
    zadaci = [getWebKorisnike(), getWebProizvode()]
    rezultat = await asyncio.gather(*zadaci)
    timerTwo = time.perf_counter()
    print(f'Program se izvodio {round(timerTwo - timerOne, 2)} sekundi.')
    return rezultat

#/////////////////////////////////////////////////////////////////////////// TRECI ZADATAK

baza_korisnika = [
{'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
{'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
{'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
{'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]
baza_lozinka = [
{'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
{'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
{'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
{'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]

async def autorizacija(korisnik, lozinka):
    await asyncio.sleep(2)
    lozinkaDb = next((n for n in baza_lozinka if n['korisnicko_ime'] == korisnik['korisnicko_ime']), None)

    if lozinkaDb and lozinkaDb['lozinka'] == lozinka:
        return f'Korisnik {korisnik['korisnicko_ime']}: Autorizacija uspjesna.'
    else:
        return f'Korisnik {korisnik['korisnicko_ime']}: Autorizacija neuspjesna.'


async def autentifikacija(korisnik: dict):
    await asyncio.sleep(3)
    korisnikDb = next((n for n in baza_korisnika if n['korisnicko_ime'] == korisnik['korisnicko_ime'] and n['email'] == korisnik['email']), None)

    if korisnikDb:
        return await autorizacija(korisnikDb, korisnik['lozinka'])
    else:
        return f'Korisnik {korisnik['korisnicko_ime']} nije pronaden.'


async def treciZadatak():
    testKorisnik = {
        'korisnicko_ime': 'mirko123',
        'email': 'mirko123@gmail.com',
        'lozinka': 'lozinka123'
    }
    #testKorisnik = {
    #    'korisnicko_ime': 'ana_anic',
    #    'email': 'aanic@gmail.com',
    #    'lozinka': 'krivalozinka123'
    #}
    print("Pokrecem autentifikaciju...")
    timerOne = time.perf_counter()
    rezultat = await autentifikacija(testKorisnik)
    timerTwo = time.perf_counter()
    print(f'Program se izvodio {round(timerTwo - timerOne, 2)} sekundi.')
    return rezultat


#/////////////////////////////////////////////////////////////////////////// CETVRTI ZADATAK

async def provjeriParnost(brojZaProvjeru):
    await asyncio.sleep(2)

    if brojZaProvjeru % 2 == 0:
        return f'Broj {brojZaProvjeru} je paran.'
    else:
        return f'Broj {brojZaProvjeru} je neparan.'

async def cetvrtiZadatak():
    listaNasumicnihBrojeva = [ random.randrange(1, 101) for _ in range(10) ]
    timerOne = time.perf_counter()
    zadaci = [ provjeriParnost(n) for n in listaNasumicnihBrojeva]
    rezultat = await asyncio.gather(*zadaci)
    timerTwo = time.perf_counter()
    print(f'Program se izvodio {round(timerTwo - timerOne, 2)} sekundi.')
    return rezultat

#/////////////////////////////////////////////////////////////////////////// PETI ZADATAK

async def secureData(osjetljiviPodaci: dict):
    await asyncio.sleep(3)
    return {
        'prezime': osjetljiviPodaci['prezime'],
        'broj_kartice': hash(str(osjetljiviPodaci['broj_kartice'])),
        'CVV': hash(str(osjetljiviPodaci['CVV']))
    }

async def petiZadatak():
    listaOsjetljivihPodataka = [
        {'prezime': 'Horvat', 'broj_kartice': '4923910293120391', 'CVV': '123'},
        {'prezime': 'Anic', 'broj_kartice': '1111222233334444', 'CVV': '321'},
        {'prezime': 'Kos', 'broj_kartice': '9999888877776666', 'CVV': '999'},
    ]

    timerOne = time.perf_counter()
    zadaci = [secureData(p) for p in listaOsjetljivihPodataka]
    rezultat = await asyncio.gather(*zadaci)
    timerTwo = time.perf_counter()

    print(f'Program se izvodio {round(timerTwo - timerOne, 2)} sekundi.')
    return rezultat

#/////////////////////////////////////////////////////////////////////////// SESTI ZADATAK

async def fetch_data(param):
    print(f"Nešto radim s {param}...")
    await asyncio.sleep(param)
    print(f'Dovršio sam s {param}.')
    return f"Rezultat za {param}"

async def sestiZadatak():
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    result1 = await task1
    print("Fetch 1 uspješno završen.")

    await asyncio.sleep(3)

    return result1


#///////////////////////////////////////////////////////////////////////////

def izbornik():
    print("\n/// Izbornik zadataka (1–7) ///")
    print("Odaberi broj zadatka koji želiš pokrenuti:")

    try:
        zadatak = int(input("Unesi broj zadatka: "))
    except ValueError:
        print("Neispravan unos! Potrebno je unijeti broj od 1 do 7.")
        return izbornik()
    pokreni_zadatak(zadatak)


def pokreni_zadatak(zadatak):
    match zadatak:
        case 1:
            try:
                rezultat = asyncio.run(simulacijaWebRequesta())
                print(f"Rezultat dohvaćanja: {rezultat}")

            except Exception as e:
                print(f"Dogodila se pogreška!: {e}")
                return izbornik()

        case 2:
            try:
                rezultat = asyncio.run(drugiZadatak())
                print(f"Rezultat dohvaćanja: {rezultat}")
            except Exception as e:
                print(f"Dogodila se pogreška!: {e}")
                return izbornik()

        case 3:
            try:
                rezultat = asyncio.run(treciZadatak())
                print(f"Rezultat dohvaćanja: {rezultat}")
            except Exception as e:
                print(f"Dogodila se pogreška!: {e}")
                return izbornik()

        case 4:
            try:
                rezultat = asyncio.run(cetvrtiZadatak())
                print(f"Rezultat dohvaćanja: {rezultat}")
            except Exception as e:
                print(f"Dogodila se pogreška!: {e}")
                return izbornik()

        case 5:
            try:
                rezultat = asyncio.run(petiZadatak())
                print(f"Rezultat dohvaćanja: {rezultat}")
            except Exception as e:
                print(f"Dogodila se pogreška!: {e}")
                return izbornik()

        case 6:
            try:
                # Kod je sam po sebi nepotrebno mjenjati ali za dokaz je dodan sleep od 3 sekunde kako bi schedulani task 2 imao vremena da se izvede. await task1 blokira main funkciju ali ne i sam loop, te se u tom periodu izvrsava task 2.
                # Produzavajuci lifecycle event loopa daje task2 dovoljno vremena da se izvede bez da ga moramo awaitat.
                timerOne = time.perf_counter()

                rezultat = asyncio.run(sestiZadatak())
                print(f"Rezultat dohvaćanja: {rezultat}")

                timerTwo = time.perf_counter()
                print(f'Program se izvodio {round(timerTwo - timerOne, 2)} sekundi.')
            except Exception as e:
                print(f"Dogodila se pogreška!: {e}")
                return izbornik()

        case 7:
            try:
                pass
                # .run(main) inicijalizira event loop i prebacuje kontrolu u main.
                # .create_task(Timer...) registrira 3 instance korutine i schedula ih u loop.
                # await asyncio.gather(*timers) privremeno zaustavi main te ceka izvrsavanje event loopa.
                # sve 3 korutine ispisu u istoj iteraciji loopa 'n sekundi preostalo', pauziraju na sekundu i ponavljaju sve dok ne zavrse i izadju iz schedula.
                # nakon sto je event loop rotirao sve korutine do kraja izvrsavanja, gather() zavrsava, gasi se event loop, i zavrsava main.
            except Exception:
                print("Dogodila se pogreška!")
                return izbornik()

        case _:
            print("Neispravan broj zadatka! Odaberi između 1 i 7.")
            return izbornik()

    ponovi = input("\nŽeliš li se vratiti na glavni izbornik? (da/ne): ").lower()
    if ponovi == "da":
        izbornik()


if __name__ == "__main__":
    izbornik()