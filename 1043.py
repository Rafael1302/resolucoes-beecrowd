A, B, C = (input().split(" "))

A = float(A)
B = float(B)
C = float(C)

if A < (B+C) and B < (A+C) and C < (A+B):
    Per = A + B + C
    print("Perimetro = %.1f"% Per)
else:
    Area = ((A+B)*C)/2
    print("Area = %.1f"% Area)