valor_da_compra= float(input ('Digite o valor da compra '))
valor_do_frete = float(input('Digite o valor do frete'))
fidelidade = str(input ("Digite "S" para sim ou "N" para não "))

if valor_da_compra > 100 and valor_do_frete > 100:
    print("O cupom de desconto pode ser utilizado")
else:
    print("O cupom não pode ser utilizado.")