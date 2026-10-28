x=input("digite um caractere:")
if x in "aeiou":
    print("O caractere",x,"é uma vogal")
elif x in "bcdfghjklmnpqrstvwxyz":
    print("O caractere",x,"é uma consoante")
elif x in "0123456789":
    print("O caractere",x,"é um número")
else:
    print("O caractere",x,"é um símbolo")