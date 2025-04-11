#Calcula desconto


# Entrada
quantidadevenda = int(input("quantas camisetas o senhor comprou? "))

# Processamento
desconto = 83 * 0.13
preço = 83
aplicação = (preço - desconto)
vendatotal = (quantidadevenda * aplicação)

# Saida
print('O desconto da camiseta vai ser ', desconto, ". Já o valor da camiseta será ", aplicação, ", e agora sua venda deu um valor total de", vendatotal, ",vai ser no Credito ou Debito?")
