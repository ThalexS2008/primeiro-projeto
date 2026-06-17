# Casar ou Comprar uma Bicicleta ?

print(" Casar ou comprar uma Bicicleta ?")

resposta = input("Voce está gordo ? s/n")

if resposta == "s":
    quer_emagrecer = input("Voce quer emagrecer ?")
    if quer_emagrecer == "s":
        print("Compre uma bicicleta")
    else:
        print("Entao Case!")
else:
    quer_engordar = input("Voce quer engordar ? s/n")
    if quer_engordar == "s":
         print("Entao Case!")
    else:
        print("Compre uma bicicleta!")
