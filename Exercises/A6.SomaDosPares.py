# Ler os limites do intervalo informados pelo usuário
inicio = int(input("Digite o valor inicial do intervalo: "))
fim = int(input("Digite o valor final do intervalo: "))

# Inicializar a variável de soma
soma = 0

# Percorrer os números no intervalo e somar os números pares
for num in range(inicio, fim+1):
    if num % 2 == 0:
        soma += num

# Imprimir a soma dos números pares no intervalo
print("A soma dos números pares no intervalo é:", soma)
