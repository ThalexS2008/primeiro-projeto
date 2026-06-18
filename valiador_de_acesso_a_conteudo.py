ano_nascimento = int(input("Digite o ano de nascimento: "))
idade = 2026 - ano_nascimento

if idade >= 16:
    print("Acesso liberado")
else:
    print("Acesso bloqueado: Conteúdo não recomendado para menores de 16 anos.")
