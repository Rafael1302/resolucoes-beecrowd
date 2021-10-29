n = int(input())

for i in range(1,11):
    print("%d x "%i, end="")
    print("%d = "%n, end="")
    res = n*i
    print("%d"%res)