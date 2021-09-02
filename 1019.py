t = input()
t = int(t)

h=0
m=0
s=0

if (t/3600) > 0 :
    h = t//3600
    t = t - (h*3600)

if (t/60) > 0 :
    m = t//60
    t = t - (m*60)
    
if t>s:
    s = t

print(repr(h)+":"+repr(m)+":"+repr(s)),
