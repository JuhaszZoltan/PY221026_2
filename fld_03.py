nev:str = input('név: ')
max_pont:int = int(input('elérhető pontszám: '))
akt_pont:int = int(input('elért pontszám: '))

if akt_pont > max_pont:
    print('hibás adatokat adtál mmeg!')
else:
    sz = akt_pont / max_pont * 100
    oszt = '-'
    if sz < 51: oszt = 'elégtelen'
    elif sz < 65: oszt = 'elégséges'
    elif sz < 77: oszt = 'közepes'
    elif sz < 90: oszt = 'jó'
    else: oszt = 'jeles'
    print(f'{nev} {round(sz, 2)}%-ot ért el, osztályzata: {oszt}')