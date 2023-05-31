# Ler a distância em quilômetros
distancia = float(input("Digite a distância percorrida em quilômetros: "))

# Ler o tempo decorrido em minutos
tempo = float(input("Digite o tempo decorrido em minutos: "))

# Calcular a velocidade em metros por segundo
velocidade = (distancia * 1000) / (tempo * 60)

# Apresentar o valor da velocidade em metros por segundo
print("A velocidade do projétil é:", velocidade, "metros por segundo.")
