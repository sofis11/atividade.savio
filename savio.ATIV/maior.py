x=input("Digite o primeiro número: ")
y=input("Digite o segundo número: ")
x=int(x)
y=int(y)
if x>y:
    print(f"O número {x} é maior que {y}.")
elif y>x:
    print(f"O número {y} é maior que {x}.")
else:
    print(f"Os números {x} e {y} são iguais.")