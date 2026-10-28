soma=0
while True:
    x=int(input("digite um número: "))
    if x<0:
        break
    soma+=1
print(f"quantidade de numeros digitados: {soma}")