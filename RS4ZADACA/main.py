import asyncio
import aiohttp
import time
import re
import random


def izbornik():
    print("\n/// Izbornik zadataka (1–6) ///")
    print("Odaberi broj zadatka koji želiš pokrenuti:")

    try:
        zadatak = int(input("Unesi broj zadatka: "))
    except ValueError:
        print("Neispravan unos! Potrebno je unijeti broj od 1 do 6.")
        return izbornik()
    pokreni_zadatak(zadatak)

# //////////////////////////////////////////////////// PRVI ZADATAK

async def fetchUsers(session):
    response = await session.get('https://jsonplaceholder.typicode.com/users')
    return await response.json()

async def prviZadatak():
    start = time.perf_counter()

    async with aiohttp.ClientSession() as session:
        userKorutine = [fetchUsers(session) for i in range(5)]
        listeKorisnika = await asyncio.gather(*userKorutine)

    korisnici = [korisnik for listaKorisnika in listeKorisnika for korisnik in listaKorisnika]

    imena = [korisnik['name'] for korisnik in korisnici]
    print(imena)
    emaili = [korisnik['email'] for korisnik in korisnici]
    print(emaili)
    usernami = [korisnik['username'] for korisnik in korisnici]
    print(usernami)

    end = time.perf_counter()
    print(f'Program se izvodio {round(end - start, 2)} sekundi.')

# //////////////////////////////////////////////////// DRUGI ZADATAK

async def getCatFact(session):
    response = await session.get('https://catfact.ninja/fact')
    data = await response.json()
    return data.get('fact', '')

async def filterCatFact(listaCatFacts: list):
    pattern = re.compile(r'cat|cats', re.IGNORECASE)
    filtriraniCatFacts = [fact for fact in listaCatFacts if pattern.search(fact)]
    return filtriraniCatFacts

async def drugiZadatak():
    start = time.perf_counter()

    async with aiohttp.ClientSession() as session:
        catFactTaskovi = [asyncio.create_task(getCatFact(session)) for _ in range(20)]
        catFactRezultati = await asyncio.gather(*catFactTaskovi)

        filtriraniCatFacts = await filterCatFact(catFactRezultati)
        print(filtriraniCatFacts)

    end = time.perf_counter()
    print(f'Program se izvodio {round(end - start, 2)} sekundi.')

# //////////////////////////////////////////////////// TRECI ZADATAK

async def getDogFact(session):
    response = await session.get('https://dogapi.dog/api/v2/facts')
    data = await response.json()
    return data.get('data', [{}])[0].get('attributes', {}).get('body')

async def mixFacts(dogFacts: list, catFacts: list):
    mixLista = [max(dogFact, catFact, key=len) for dogFact, catFact in zip(dogFacts, catFacts)]
    return mixLista

async def treciZadatak():
    start = time.perf_counter()

    async with aiohttp.ClientSession() as session:
        catFactTaskovi = [asyncio.create_task(getCatFact(session)) for _ in range(5)]
        dogFactTaskovi = [asyncio.create_task(getDogFact(session)) for _ in range(5)]
        animalFactRezultati = await asyncio.gather(*dogFactTaskovi, *catFactTaskovi)

        dogFactsRezultati = animalFactRezultati[:5]
        catFactsRezultati = animalFactRezultati[5:]

        mixaniRezultati = await mixFacts(dogFactsRezultati, catFactsRezultati)
        print(mixaniRezultati)

    end = time.perf_counter()
    print(f'Program se izvodio {round(end - start, 2)} sekundi.')

# //////////////////////////////////////////////////// CETVRTI ZADATAK

korisnici = {
    "korisnik1": "lozinka1",
    "korisnik2": "lozinka2",
    "korisnik3": "lozinka3",
    "korisnik4": "lozinka4",
    "korisnik5": "lozinka5",
}

async def autentifikacija(username: str, password: str, cekanje: int = 2) -> bool:
    await asyncio.sleep(cekanje)

    if username in korisnici and korisnici[username] == password:
        print('Autentifikacija')
        return True
    else:
        raise ValueError(f'Autentifikacija neuspjesna za korisnika: {username} (Neispravni podaci)')

async def autentifikacijaSimulacijaTimeout():
    await asyncio.sleep(4)
    return True

async def cetvrtiZadatakPrviDio():
    start = time.perf_counter()

    testPodaci = [
        ("korisnik1", "lozinka1", 2),
        ("korisnik2", "lozinka2", 2),
        ("korisnik3", "lozinka3", 2),
        ("korisnik4", "lozinka4", 2),
        ("korisnik5", "lozinka5", 2),
        ("sporiservis", "timeout", 4),
    ]
    authKorutine = [autentifikacija(username, password, cekanje) for username, password, cekanje in testPodaci]

    try:
        authRezultati = await asyncio.gather(*authKorutine)
        print(f'Svi korisnici autenticirani ', authRezultati)
    except ValueError as e:
        print(f'Greska izvodjenja programa', e)
        print('Iako je jedan od zahtjeva neuspjesan, ostali se i dalje nastavljaju u pozadini')

    end = time.perf_counter()
    print(f'Program se izvodio {round(end - start, 2)} sekundi.')

async def cetvrtiZadatakDrugiDio():
    start = time.perf_counter()

    try:
        rezultatSimulacija = await asyncio.wait_for(autentifikacijaSimulacijaTimeout(), timeout=3)
        print(f'Uspjesni poziv: {rezultatSimulacija}')
    except asyncio.TimeoutError as e:
        print('Neuspjesan poziv. Ne odgovara na vrijeme')


    end = time.perf_counter()
    print(f'Program se izvodio {round(end - start, 2)} sekundi.')

# //////////////////////////////////////////////////// PETI ZADATAK

async def fetchUrl(session, url: str) -> str:
    async with session.get(url, timeout = 5) as response:
        content = await response.text()
        return content

async def petiZadatak():
    start = time.perf_counter()

    urls = [
        "https://example.com",
        "https://httpbin.org/get",
        "https://api.github.com"
    ]

    async with aiohttp.ClientSession() as session:
        fetchKorutine = [fetchUrl(session, url) for url in urls]
        fetchRezultati = await asyncio.gather(*fetchKorutine)

    for url, content in zip(urls, fetchRezultati):
        print(f'Fetched {len(content)} characters from {url}')

    end = time.perf_counter()
    print(f'Program se izvodio {round(end - start, 2)} sekundi.')

# //////////////////////////////////////////////////// SESTI ZADATAK

async def fetchWeatherData(stationId: int) -> float | None:
    cekanje = random.uniform(1, 5)

    print(f'Stanica {stationId}: Pokrenuto. Ocekivano kasnjenje: {cekanje:2f}s')

    try:
        await asyncio.wait_for(asyncio.sleep(cekanje), timeout=2)

        temperatura = random.uniform(20, 25)
        print(f'Stanica {stationId}: Uspjesno dohvacena temperatura ({temperatura:.2f}°C).')
        return temperatura
    except asyncio.TimeoutError as e:
        print(f'Stanica {stationId}: Timeout. Neuspjesan odgovor u predvidjenom vremenu (preko 2s).')
        return None

async def sestiZadatak():
    start = time.perf_counter()

    stationIds = list(range(1, 11))

    async with aiohttp.ClientSession() as session:
        weatherTaskovi = [asyncio.create_task(fetchWeatherData(stationId)) for stationId in stationIds]
        fetchRezultati = await asyncio.gather(*weatherTaskovi)

    noneFilterTemperature = [temp for temp in fetchRezultati if temp is not None]

    if noneFilterTemperature:
        prosjecnaTemperatura = sum(noneFilterTemperature) / len(noneFilterTemperature)
        neuspjesnePostaje = len(fetchRezultati) - len(noneFilterTemperature)
    else:
        prosjecnaTemperatura = 0.0
        neuspjesnePostaje = len(fetchRezultati)

    print(f'Ukupno analiziranih stanica: {len(stationIds)}')
    print(f'Uspjesno dohvaceno: {len(noneFilterTemperature)}')
    print(f'Neuspjesne postaje: {neuspjesnePostaje}')
    print(f'Prosjecna temperatura: {prosjecnaTemperatura:.2f}°C')

    end = time.perf_counter()
    print(f'Program se izvodio {round(end - start, 2)} sekundi.')

# ////////////////////////////////////////////////////

def pokreni_zadatak(zadatak):
    match zadatak:
        case 1:
            try:
                asyncio.run(prviZadatak())
            except Exception as e:
                print(f"Greška u zadatku 1: {e}")
                return izbornik()

        case 2:
            try:
                asyncio.run(drugiZadatak())
            except Exception as e:
                print(f"Greška u zadatku 2: {e}")
                return izbornik()

        case 3:
            try:
                asyncio.run(treciZadatak())
            except Exception as e:
                print(f"Greška u zadatku 3: {e}")
                return izbornik()

        case 4:
            try:
                asyncio.run(cetvrtiZadatakPrviDio())
                asyncio.run(cetvrtiZadatakDrugiDio())
            except Exception as e:
                print(f"Greška u zadatku 4: {e}")
                return izbornik()

        case 5:
            try:
                asyncio.run(petiZadatak())
            except Exception as e:
                print(f"Greška u zadatku 5: {e}")
                return izbornik()

        case 6:
            try:
                asyncio.run(sestiZadatak())
            except Exception as e:
                print(f"Greška u zadatku 6: {e}")
                return izbornik()

        case _:
            print("Neispravan broj zadatka! Odaberi između 1 i 6.")
            return izbornik()

    ponovi = input("\nŽeliš li se vratiti na glavni izbornik? (da/ne): ").lower()
    if ponovi == "da":
        izbornik()


if __name__ == "__main__":
    izbornik()