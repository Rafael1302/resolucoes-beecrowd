count = int(0)
sum = int(0)

for i in range(0, 6):
    n = float(input())
    if n > 0:
        count = count+1
        sum += n

avg = sum/count

print("%d valores positivos"%count)
print("%.1f"%avg)