n = int(input())
dentro = int(0)
fora = int(0)

for i in range(0, n):
    num = int(input())
    if num >= 10 and num<=20:
        dentro += 1
    else:
        fora += 1

print("%d in"% dentro)
print("%d out"% fora)