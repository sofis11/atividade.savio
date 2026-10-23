h1=(input("digite o primeiro horario: "))
m1=(input("digite o primeiro minuto: "))
h2=(input("digite o segundo horario: "))
m2=(input("digite o segundo minuto: "))
if (h1*3600+m1*60)>(h2*3600+m2*60):
    print("O primeiro horario é maior")
elif (h1*3600+m1*60)<(h2*3600+m2*60):
    print("O segundo horario é maior")
else:
    print("Os horarios são iguais") 