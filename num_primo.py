# Solicita ao usuário um número inteiro
n = int(input("Digite um número inteiro: "))

# Verifica se o número é maior que 1
if n > 1:
    # Assume que o número é primo até provar o contrário
    eh_primo = True
    # Itera de 2 até a raiz quadrada de n (arredondada para cima)
    for i in range(2, int(n**0.5) + 1):
        # Se n for divisível por i, não é primo
        if n % i == 0:
            eh_primo = False
            break
    # Exibe o resultado
    if eh_primo:
        print(f"{n} é um número primo.")
    else:
        print(f"{n} não é um número primo.")
else:
    print(f"{n} não é um número primo.")