h1=input("Digite o primeiro horário (HH:MM): ")
h2=input("Digite o segundo horário (HH:MM): ")
pedaco=h1.split(":")
h1_h = int(pedaco[0])
h1_m = int(pedaco[1])
pedaco=h2.split(":")
h2_h = int(pedaco[0])
h2_m = int(pedaco[1])
if h1_h>h2_h:
    print("O primeiro horário é maior")
elif h1_h<h2_h:
    print("O segundo horário é maior")
else:
    if h1_m>h2_m:
        print("O primeiro horário é maior")
    elif h1_m<h2_m:
        print("O segundo horário é maior")
    else:
        print("Os horários são iguais")