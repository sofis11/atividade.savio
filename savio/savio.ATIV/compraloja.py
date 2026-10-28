nome=input("Digite seu nome: ")
preço__produto=float(input("Digite o preço do produto: "))
quantidade_comprada=int(input("Digite a quantidade comprada: "))
desconto=float(input("Digite o valor do desconto: "))
parcela=input("Digite a quantidade de parcelas: ")
bruto=preço__produto*quantidade_comprada
valor_desconto=bruto*desconto/100
valor_final=bruto-valor_desconto
parcela_final=valor_final/int(parcela)
print("O valor bruto da compra é: R$",bruto)
print("O valor do desconto é: R$",valor_desconto)
print("O valor final da compra é: R$",valor_final)
print("O valor de cada parcela é: R$",parcela_final)