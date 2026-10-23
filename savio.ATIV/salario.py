nome=input("Digite seu nome: ")
salario=float(input("Digite seu salário: "))
inss=float(input("Digite o valor do INSS: "))
plano_saude=float(input("Digite o valor do plano de saúde: "))
vinss=salario*inss/100
vplano_saude=salario*plano_saude/100
desconto=vinss+vplano_saude
salario_liquido=salario-desconto
print("O valor do INSS é: R$",vinss)
print("O valor do plano de saúde é: R$",vplano_saude)
print("O valor total de descontos é: R$",desconto)
print("O salário líquido é: R$",salario_liquido)    