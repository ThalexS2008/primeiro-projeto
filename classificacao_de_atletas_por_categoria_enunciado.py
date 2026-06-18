idade=int(input("Digite a idade do atleta: "))
if idade<=9:
    print("Categoria mirim")
elif idade<=14:
    print("Categoria infantil")
elif idade>=19:
    print("Categoria junior")
elif idade<=25:
    print("Categoria senior")
else:
    print("Categoria master")

