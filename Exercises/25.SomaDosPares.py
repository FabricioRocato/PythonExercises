numeros = []
continuar = True

while continuar:
    numero = float(input("Digite um número: "))
    numeros.append(numero)

    resposta = input("Deseja inserir mais números? (s/n): ")
    if resposta.lower() == "n":
        continuar = False

media = sum(numeros) / len(numeros)
print(f"A média dos números é: {media}")
