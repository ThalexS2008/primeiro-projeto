A = float(input("Digite o comprimento da reta A: "))
B = float(input("Digite o comprimento da reta B: "))
C = float(input("Digite o comprimento da reta C: "))

if A + B > C and A + C > B and B + C > A:
    print("As retas podem formar um triângulo!")

    if A == B == C:
        print("Tipo: triângulo equilátero")
    elif A == B or A == C or B == C:
        print("Tipo: triângulo isósceles")
    else:
        print("Tipo: triângulo escaleno")
else:
    print("As retas nao podem formar um triângulo.")

