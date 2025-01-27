def verificar_cupom(valor_compra, valor_frete, cliente_fidelidade):
    # Verifica se o cliente é cadastrado no programa de fidelidade
    fidelidade = cliente_fidelidade.lower() == "s"
    
    # Verifica a condição para o uso do cupom
    if (valor_compra + valor_frete > 100) or fidelidade:
        return True
    else:
        return False

# Exemplo de uso
valor_compra = float(input("Digite o valor da compra: "))
valor_frete = float(input("Digite o valor do frete: "))
cliente_fidelidade = input("O cliente é cadastrado no programa de fidelidade? (s/n): ")

if verificar_cupom(valor_compra, valor_frete, cliente_fidelidade):
    print("O cupom pode ser utilizado.")
else:
    print("O cupom não pode ser utilizado.")