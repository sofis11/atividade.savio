n1=int(input("Digite a primeira nota: "))
n2=int(input("Digite a segunda nota: "))
n3=int(input("Digite a terceira nota: "))
media=(n1*2+n2*3+n3*5)/10
if media>=7:
    print("Aprovado com média",media)
elif media>=5 and media<7:
    print("Recuperação com média",media)
else:
    print("Reprovado com média",media)