numero = int(input("Digite um numero: "))
if numero % 3 == 0:
    print("'Fizz'" "(Multiplo de 3)")
elif numero % 5 ==0:
    print("'Buzz'" "(Multiplo de 5)")
elif numero % 3 == 0 and numero % 5 ==0:
    print("'FizzBuzz'" "(Multiplo de 3 e Multiplo 5)")
else:
    print("... ")
