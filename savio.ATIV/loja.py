compra=input("Digite o valor da compra: ")
compra=int(compra)  
if compra<100:
    print("O valor da compra é menor que R$100,00. Não há desconto.")
elif compra<=300:
    desconto=compra*0.10
    print("O valor da compra é R$",compra,". O desconto é de R$",desconto,". O valor final é R$",compra-desconto)
else: 
    desconto=compra*0.15
    print("O valor da compra é R$",compra,". O desconto é de R$",desconto,". O valor final é R$",compra-desconto)
    