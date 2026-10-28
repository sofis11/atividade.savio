nota=float(input("Digite sua nota: "))
faltas=int(input("Digite o número de faltas: "))
if nota>=7 and faltas<=10:
    print("aprovado")
elif nota>=5 and faltas<=10:
    print("recuperação")
else:
    print("reprovado")