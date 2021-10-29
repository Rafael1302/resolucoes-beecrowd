n = int(input())
c = int(0)
r = int(0)
s = int(0)
total = int(0)

for i in range(0, n):
    animal = input().split(" ")
    total += int(animal[0])
    if animal[1] == "C":
        c += int(animal[0])
    if animal[1] == "R":
        r += int(animal[0])
    if animal[1] == "S":
        s += int(animal[0])

print("Total: %d cobaias"%total)
print("Total de coelhos: %d"%c)
print("Total de ratos: %d"%r)
print("Total de sapos: %d"%s)
p_c = (c*100)/total
print("Percentual de coelhos: %.2f %%"%p_c)
p_r = (r*100)/total
print("Percentual de ratos: %.2f %%"%p_r)
p_s = (s*100)/total
print("Percentual de sapos: %.2f %%"%p_s)