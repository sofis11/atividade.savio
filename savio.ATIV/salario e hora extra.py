# Leitura dos dados informados pelo usuário
salario_mensal = float(input("Digite o valor do salário mensal fixo (R$): "))
horas_trabalhadas = float(input("Digite a quantidade de horas regulares trabalhadas no mês: "))
horas_extras = float(input("Digite a quantidade de horas extras trabalhadas: "))
valor_por_hora_extra = float(input("Digite o valor pago por cada hora extra (R$): "))

# Cálculos
total_ganho_horas_extras = horas_extras * valor_por_hora_extra
salario_total = salario_mensal + total_ganho_horas_extras

# Exibição dos resultados na tela
print("\n--- RESUMO DO SALÁRIO ---")
print(f"Salário Mensal Fixo: R$ {salario_mensal:.2f}")
print(f"Horas Regulares Trabalhadas: {horas_trabalhadas:.1f}h") if 'horas_trabalhadas' in locals() else print(f"Horas Regulares Trabalhadas: {horas_trabalhadas:.1f}h")
print(f"Total Ganho com Horas Extras: R$ {total_ganho_horas_extras:.2f} ({horas_extras:.1f}h realizadas)")
print(f"Salário Total a Receber: R$ {salario_total:.2f}")
