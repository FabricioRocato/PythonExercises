# Definindo o intervalo de números naturais
inicio = 1
fim = 100

# Inicializando a variável de soma
soma = 0

# Calculando a soma dos números no intervalo
for num in range(inicio, fim+1):
    soma += num

# Imprimindo o intervalo e o resultado da soma
print("Intervalo:", inicio, "-", fim)
print("Soma:", soma)
