n1=float(input("Digite a primeira nota: "))
n2=float(input("Digite a segunda nota: "))
n3=float(input("Digite a terceira nota: "))
n4=float(input("Digite a quarta nota: "))
if n1>n2 and n1>n3 and n1>n4:
    remover = n1
elif n2>n1 and n2>n3 and n2>n4:
    remover = n2
elif n3>n1 and n3>n2 and n3>n4:
    remover = n3
else:
    remover = n4
if n1<n2 and n1<n3 and n1<n4:
    menor = n1
elif n2<n1 and n2<n3 and n2<n4:
    menor = n2
elif n3<n1 and n3<n2 and n3<n4:
    menor = n3
else:
    menor = n4
media = (n1+n2+n3+n4-remover-menor)/2
print("A média das notas é: ", media)