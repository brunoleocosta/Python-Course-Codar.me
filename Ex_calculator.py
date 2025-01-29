# Função que realiza o cálculo
def calculadora(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return "Erro: Divisão por zero!"
        else:
            return a / b
    else:
        return "Operador inválido!"

# Solicita os valores do usuário
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
op = input("Digite o operador (+, -, *, /): ")

# Realiza o cálculo e exibe o resultado
resultado = calculadora(a, b, op)
print("Resultado:", resultado)
