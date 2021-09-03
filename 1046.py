I, F = (input().split())

I = int(I)
F = int(F)
r = int(1)

if I > F:
    r = (24 + F)-I
if F > I:
    r = F - I
if F == I:
    r = 24

print("O JOGO DUROU %d HORA(S)"% r)