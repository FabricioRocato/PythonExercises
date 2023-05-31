# Ler a cotação do dólar
cotacao_dolar = float(input("Digite a cotação do dólar: "))

# Ler a quantidade de dólares disponível
quantidade_dolares = float(input("Digite a quantidade de dólares disponível: "))

# Calcular o valor da conversão em reais
valor_conversao = cotacao_dolar * quantidade_dolares

# Apresentar o valor da conversão em reais
print("O valor da conversão em reais é: R$", valor_conversao)
