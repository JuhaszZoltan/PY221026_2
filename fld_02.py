a:int = int(input('a = '))
b:int = int(input('b = '))
c:int = int(input('c = '))

if a+b<=c or a+c<=b or b+c<=a:
    print('nem létezik ilyen 3szög')
else:
    k = a + b + c
    s = k / 2
    t = (s*(s-a)*(s-b)*(s-c)) ** .5
    print(f'háromszög kerülete: {k}')
    print(f'háromszög területe: {t}')