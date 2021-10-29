numb = int(0)
pos = int(0)

for i in range(0,100):
    n = int(input())
    if n>numb:
        numb = n
        pos = i+1

print(numb)
print(pos)
    