par = int(0)
imp = int(0)
pos = int(0)
neg = int(0)

for i in range(0, 5):
    n = int(input())
    if n % 2 == 0:
        par += 1
    elif n % 2 == 1:
        imp += 1
    if n > 0:
        pos += 1
    elif n < 0:
        neg += 1

print("%d valor(es) par(es)"%par)
print("%d valor(es) impar(es)"%imp)
print("%d valor(es) positivo(s)"%pos)
print("%d valor(es) negativo(s)"%neg)

