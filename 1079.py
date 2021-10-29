n = int(input())
avg = []
sum = int(0)

for i in range(0, n):
    numb = input().split(" ")
    sum = (float(numb[0])*2) + (float(numb[1])*3) + (float(numb[2])*5)
    res = sum/10
    avg.append(res)

for i in range(0,n):
    print("%.1f"%avg[i])
