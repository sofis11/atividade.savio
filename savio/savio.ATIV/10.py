altura=input("Digite sua altura em metros: ")
peso=input("Digite seu peso em kg: ")
imc=float(peso)/float(altura)**2
if imc<18.5:
    print("Abaixo do peso")
elif imc>=18.5 and imc<25:
    print("Peso normal")
elif imc>=25 and imc<30:
    print("Sobrepeso")
elif imc>=30 and imc<35:
    print("Obesidade grau 1")
elif imc>=35 and imc<40:
    print("Obesidade grau 2")
else:
    print("Obesidade grau 3")