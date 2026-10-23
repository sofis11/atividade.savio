x=int(input("Digite um número inteiro: "))
if x%3 == 0:
    print("o numero",x,"é múltiplo de 3")
elif x%5 == 0:
    print("o numero",x,"é múltiplo de 5")
elif x%3 == 0 and x%5 == 0:
    print("o numero",x,"é múltiplo de 3 e 5")
else:
    print("o numero",x,"não é múltiplo de 3 nem de 5")