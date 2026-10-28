max = int(input("Digite o 1° número: "))
min = max

for i in range(2, 11):
    x = int(input(f"Digite o {i}° número: "))

    if x > max:
max=x
    if x < min:
min=x
print(f"O maior é {max} e o menor é {min}")