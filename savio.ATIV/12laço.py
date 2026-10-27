print("digite um número:")
soma=0
while True:
    n=int(input("->"))
    if n==0:
        break
    soma=soma+n
print(f"A soma dos números digitados é: {soma}")