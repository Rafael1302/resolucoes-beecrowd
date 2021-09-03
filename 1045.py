A, B, C = input().split(" ")
MAIOR = float(1)
MEDIO = float(1)
MENOR = float(1)
A = float(A)
B = float(B)
C = float(C)

if A >= B and A >= C:
    MAIOR = A
    if B >= C:
        MEDIO = B
        MENOR = C
    else:
        MEDIO = C
        MENOR = B
if B >= A and B >= C:
    MAIOR = B
    if A >= C:
        MEDIO = A
        MENOR = C
    else:
        MEDIO = C
        MENOR = A

if C >= A and C >= B:
    MAIOR = C
    if A >= B:
        MEDIO = A
        MENOR = B
    else:
        MEDIO = B
        MENOR = A             

if A == B and B == C:
    MAIOR = A
    MEDIO = B
    MENOR = C

A = MAIOR
B = MEDIO
C = MENOR

if A >= (B + C):
    print('NAO FORMA TRIANGULO')
else:
    if (A ** 2) == (B ** 2 + C ** 2):
        print('TRIANGULO RETANGULO')
    if (A ** 2) > (B ** 2 + C ** 2):
        print('TRIANGULO OBTUSANGULO')
    if (A ** 2) < (B ** 2 + C ** 2):
        print('TRIANGULO ACUTANGULO')
    if (A == B == C):
        print('TRIANGULO EQUILATERO')
    if A == B != C or B == C != A or A == C != B:
        print('TRIANGULO ISOSCELES')