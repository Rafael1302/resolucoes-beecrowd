A, B, C = (input().split(" "))
A = int(A)
B = int(B)
C = int(C)

maior = 0
medio = 0
menor = 0

if A > B and A > C:
    maior = A
    if B > C:
        menor = C
        medio = B
    else:
        menor = B
        medio = C

if B > A and B > C:
    maior = B
    if A > C:
        menor = C
        medio = A
    else: 
        menor = A
        medio = C

if C > A and C > B:
    maior = C
    if A > B:
        menor = B
        medio = A
    else: 
        menor = A
        medio = B

print(menor)
print(medio)
print(maior)
print()
print(A)
print(B)
print(C)