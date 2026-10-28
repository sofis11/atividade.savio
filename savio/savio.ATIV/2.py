numero= int(input("Digite um número: "))
if numero % 2 == 0 and numero >0:
    print("O número é par e positivo.")
elif numero % 2 == 0 and numero < 0:
    print("O número é par e negativo.")
elif numero % 2 != 0 and numero > 0:
    print("O número é ímpar e positivo.")
else:
    print("O número é ímpar e negativo.")
