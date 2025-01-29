numero = int(input("Digite um número: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("'FizzBuzz' (Múltiplo de 3 e 5)")
elif numero % 3 == 0:
    print("'Fizz' (Múltiplo de 3)")
elif numero % 5 == 0:
    print("'Buzz' (Múltiplo de 5)")
else:
    print("... ")