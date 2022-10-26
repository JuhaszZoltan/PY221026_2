import random

talalat = 0
for i in range(5):
    x:int = random.randint(10, 99)
    y:int = random.randint(10, 99)
    s = x + y
    d = x - y
    if d < 0: d *= -1
    print(f'{i + 1}. kör:')
    print(f'  a két szám összege: {s}, különbsége: {d}. Mi lehet ez?')
    tx = int(input('    egyik szám: '))
    ty = int(input('    másik szám: '))
    if (tx == x and ty == y) or (tx == y and ty == x):
        print('  helyes!')
        talalat += 1
    else:
        print(f'  sajnos nem, a két szám: {x} és {y}')
print(f'végeztünk, helyes találataid száma: {talalat}')