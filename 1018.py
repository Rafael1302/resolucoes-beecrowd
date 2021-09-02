N = input()
N = int(N)

aux = N

cem = aux//100
aux -= (cem*100)

cinq = aux//50
aux -= (cinq*50)

vin = aux//20
aux -= (vin*20)

dez = aux//10
aux -= (dez*10)

cinc = aux//5
aux -= (cinc*5)

dois = aux//2
aux -= (dois*2)

um = aux//1

print(N)
print('%d nota(s) de R$ 100,00' % cem)
print('%d nota(s) de R$ 50,00' % cinq)
print('%d nota(s) de R$ 20,00' % vin)
print('%d nota(s) de R$ 10,00' % dez)
print('%d nota(s) de R$ 5,00' % cinc)
print('%d nota(s) de R$ 2,00' % dois)
print('%d nota(s) de R$ 1,00' % um)