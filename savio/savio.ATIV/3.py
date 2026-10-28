x=int(input("Digite um número: "))
y=int(input("Digite outro número: "))
z=int(input("Digite mais um número: "))
if x>y and x>z:
    print("O maior número é:", x)
elif y>x and y>z:
    print("O maior número é:", y)
else:
    print("O maior número é:", z)