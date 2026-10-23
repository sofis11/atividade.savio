x=input("digite um valor para x: ")
if x in "abcdefghijklmnopqrstuvwxyz":
    print("O valor de x é uma letra minuscula")
elif x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    print("O valor de x é uma letra maiuscula")
elif x in "0123456789":
    print("O valor de x é um número")
else:
    print("O valor de x é um símbolo")