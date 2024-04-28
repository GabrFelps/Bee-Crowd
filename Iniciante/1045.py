def main():
    A, B, C = input().split(" ")
    A = float(A)
    B = float(B)
    C = float(C)
    if A > 0 and B > 0 and C > 0:
        if A >= B + C:
            print("NAO FORMA TRIANGULO")
        else:
            if A**2 == B**2 + C**2:
                print("TRIANGULO RETANGULO")
            if A**2 > B**2 + C**2:
                print("TRIANGULO OBTUSANGULO")
            if A**2 < B**2 + C**2:
                print("TRIANGULO ACUTANGULO")
            if A == B and B == C:
                print("TRIANGULO EQUILATERO")
            if A == B and A != C or C == A and C != B or B == C and B != A:
                print("TRIANGULO ISOSCELES")
main()