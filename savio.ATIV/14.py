salario= int(input("Digite o salário do funcionário: "))
if salario<=1500:
    aumento=salario*0.2
    print("O novo salário é de R$",salario+aumento)
elif salario>1500 and salario<=3000:
    aumento=salario*0.15
    print("O novo salário é de R$",salario+aumento)
else:
    aumento=salario*0.1
    print("O novo salário é de R$",salario+aumento)