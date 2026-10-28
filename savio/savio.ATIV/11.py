l1=int(input("Digite o primeiro lado: "))
l2=int(input("Digite o segundo lado: "))
l3=int(input("Digite o terceiro lado: "))
if l1==l2 and l2==l3:
    print("O triângulo é equilátero")
elif l1==l2 or l2==l3 or l1==l3:
    print("O triângulo é isósceles")
else:
    print("O triângulo é escaleno") 
    