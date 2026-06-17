from selectors import SelectSelector

nota1 = float(input("Digite sua primeira nota:")) # 8.5
nota2 = float(input("Digite sua segunda nota:"))
nota3 = float(input("Digite sua terceira nota:"))

media = (nota1 + nota2 + nota3) / 3


if media >= 7:
    print(f"Aluno(a) aprovado(a) com média {media:.2f}")
elif media >= 3 and media < 7 :
    print(f"Aluno(a) reprovado(a) com média {media:.2f}")
    fez_recuperacao = input("Aluno já fez a recuperacao? s/n: ")
    if fez_recuperacao == "s":
        nota_recuperacao = float(input("Digite a nota da recuperacao: "))
        if nota_recuperacao >= 5:
          print("Aluno(a) aprovado pela recuperacao")
        else:
            print("Aluno(a) nao obteve nota suficiente para ser aprovado após a recuperacao.")
else:
    print(f"Aluno(a) Reprovado(a) com média {media:.2f}")

