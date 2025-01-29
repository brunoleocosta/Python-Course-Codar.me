# Solicita ao usuário um número inteiro
n = int(input("Digite um número inteiro: "))

# Verifica se o número é válido (maior ou igual a 1)
if n >= 1:
    print(f"Números pares de 1 até {n}:")
    # Usa um loop para iterar de 1 até n
    for i in range(1, n + 1):
        # Verifica se o número é par
        if i % 2 == 0:
            print(i)
else:
    print("Por favor, digite um número inteiro maior ou igual a 1.")