def calcular_fatorial(numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

# Leitura do número
numero = int(input("Digite um número: "))

# Calculando o fatorial
resultado = calcular_fatorial(numero)

# Imprimindo o resultado
print("O fatorial de", numero, "é", resultado)
