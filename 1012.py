A, B, C = (input().split(" "))

A = float(A)
B = float(B)
C = float(C)

t = (A*C)/2
cir = 3.14159*(C)*(C)
trap = ((A+B)*C)/2
quad = B*B
ret = A*B


print('TRIANGULO: %.3f' % t)
print('CIRCULO: %.3f' % cir)
print('TRAPEZIO: %.3f' % trap)
print('QUADRADO: %.3f' % quad)
print('RETANGULO: %.3f' % ret)
