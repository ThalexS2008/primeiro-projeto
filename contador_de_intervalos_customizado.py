num1 = int(input("Digite um valor inicial: "))

num2 = int(input("Digite um valor final: "))

num3 = int(input("Digte o valor dos intervalos: "))

for c in range(num1, num2, num3):
    print(c)

numero = 0

for i in range(1, 101):

    if i % 2 != 0 and i % 3 == 0:
        numero += i

        print(numero)


