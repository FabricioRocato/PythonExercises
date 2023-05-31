# Ler a cotação do dólar
cotacao_dolar = float(input("Digite a cotação do dólar: "))

# Ler a quantidade de reais disponível
quantidade_reais = float(input("Digite a quantidade de reais disponível: "))

# Calcular o valor da conversão em dólares
valor_conversao = quantidade_reais / cotacao_dolar

# Apresentar o valor da conversão em dólares
print("O valor da conversão em dólares é: US$", valor_conversao)
