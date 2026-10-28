par=0
imp=0
for i in range (1,11):
    n=int(input(f"Digite um número {i}: "))
    if n%2==0:
        par=par+1
    else:
        imp=imp+1
print(f"Você digitou {par} números pares e {imp} números ímpares")