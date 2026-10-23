nome= input("Digite seu nome:")
km= int(input("Digite a quantidade de km percorridos:"))
litros= int(input("Digite a quantidade de litros consumidos:"))
preço= float(input("Digite o preço do combustível:"))
consumo= km/litros
gasto= litros*preço
print("consumo medio:",consumo)
print("gasto total:",gasto)