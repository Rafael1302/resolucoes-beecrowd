d = input()
d = int(d)

a = 0
m = 0
dias = 0

if d>365:
    a = d//365
    d -= (a*365)

if d>30:
    m = d//30
    d -= (m*30)

if d>1:
    dias = d

print('%d ano(s)'% a)
print('%d mes(es)'% m)
print('%d dia(s)'% dias)
