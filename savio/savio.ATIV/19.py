horario=input("Digite o horário (HH:MM): ")
dia=int(input("Digite o dia da semana (2-6): "))
if dia>=2 and dia<=6:
    if horario>="08:00" and horario<="18:00":
        print("O horário é útil")
    else:
        print("O horário não é útil")
