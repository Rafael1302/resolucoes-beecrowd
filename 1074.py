n = int(input())
numb = []

for i in range(0,n):
    aux = input()
    numb.append(aux)

for i in range(0,n):
    if int(numb[i])!=0:
        if int(numb[i])%2==0:
            print("EVEN ", end="")
        elif int(numb[i])%2==1:
            print("ODD ", end="")
        if int(numb[i])<0:
            print("NEGATIVE", end="")
        elif int(numb[i])>0:
            print("POSITIVE", end="")
    else:
        print("NULL", end="")
    print("")
    