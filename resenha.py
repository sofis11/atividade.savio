dias = ["segunda", "terca", "quarta", "quinta", "sabado"]
for dia in dias:
    if dia == "sábado" or dia=="domingo":
        print("resenha")
    elif dia == "quinta" or dia=="sábado" or dia=="domingo":
        print("Sofia e Ciço vão para a resenha")
    elif dia=="sexta" :
        print("jazz e racha")
    elif dia== "segunda" or dia=="terça" or dia== "quarta":
        print("senzala e presídio")
    else:
       print("não é dia da semana")