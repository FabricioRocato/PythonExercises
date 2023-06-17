def encontrar_primeira_letra_nao_repetida(texto):
    frequencia = {}

    # Contar a frequência de cada letra no texto
    for letra in texto:
        if letra in frequencia:
            frequencia[letra] += 1
        else:
            frequencia[letra] = 1

    # Encontrar a primeira letra não repetida
    for letra in texto:
        if frequencia[letra] == 1:
            return letra

    # Se não houver letras não repetidas, retornar None
    return None


texto = input("Digite um texto: ")
primeira_letra = encontrar_primeira_letra_nao_repetida(texto)

if primeira_letra:
    print(f"A primeira letra não repetida é: {primeira_letra}")
else:
    print("Não existem letras que não se repetem no texto informado.")
