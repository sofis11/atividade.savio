dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

if mes < 1 or mes > 12:
    print("Data inválida")

elif dia < 1:
    print("Data inválida")

elif mes == 2 and dia > 28:
    print("Data inválida")

elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia > 30:
        print("Data inválida")
    else:
        print("Data válida")

elif dia > 31:
    print("Data inválida")

else:
    print("Data válida")