numero=float(input("digite um numero: "))
inteira=int(numero)
decimal=(numero-inteira)
if inteira>decimal:
    print("A parte inteira é maior que a parte decimal")
elif inteira<decimal:
    print("A parte decimal é maior que a parte inteira")
else:
    print("A parte inteira é igual a parte decimal")
