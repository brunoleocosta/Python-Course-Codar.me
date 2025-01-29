# Número secreto que o usuário precisa adivinhar
numero_secreto = 8

# Número de tentativas
tentativas = 3

print("Bem-vindo ao jogo 'Acerte o número'!")
print(f"Você tem {tentativas} tentativas para adivinhar o número secreto.")

# Loop para as tentativas
for tentativa in range(1, tentativas + 1):
    print(f"\nTentativa {tentativa} de {tentativas}")
    palpite = int(input("Digite um número: "))

    # Verifica se o palpite está correto
    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou o número secreto: {numero_secreto}.")
        break
    elif palpite < numero_secreto:
        print("O número secreto é maior que o seu palpite.")
    else:
        print("O número secreto é menor que o seu palpite.")

    # Se acabaram as tentativas
    if tentativa == tentativas:
        print(f"\nSuas tentativas acabaram. O número secreto era: {numero_secreto}.")