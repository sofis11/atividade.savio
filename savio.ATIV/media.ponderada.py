av1=float(input("Digite a primeira avaliação: "))
av2=float(input("Digite a segunda avaliação: "))
av3=float(input("Digite a terceira avaliação: "))
media_ponderada=(av1*2+av2*3+av3*5)/(2+3+5)
print("A média ponderada é: ",media_ponderada)
if media_ponderada>=6:
    print("Aprovado")
else:
    print("Reprovado")