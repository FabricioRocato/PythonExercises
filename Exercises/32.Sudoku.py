def validar_sudoku(tabuleiro):
    for linha in tabuleiro:
        if len(set(linha)) != len(linha):
            return False

    for coluna in range(9):
        valores = set()
        for linha in tabuleiro:
            valor = linha[coluna]
            if valor in valores:
                return False
            valores.add(valor)

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            valores = set()
            for m in range(i, i + 3):
                for n in range(j, j + 3):
                    valor = tabuleiro[m][n]
                    if valor in valores:
                        return False
                    valores.add(valor)

    return True


def encontrar_celulas_incorretas(tabuleiro):
    celulas_incorretas = []

    for linha in range(9):
        for coluna in range(9):
            valor = tabuleiro[linha][coluna]
            if valor != 0:
                tabuleiro[linha][coluna] = 0
                if not validar_sudoku(tabuleiro):
                    celulas_incorretas.append((linha, coluna))
                tabuleiro[linha][coluna] = valor

    return celulas_incorretas


tabuleiro = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

celulas_incorretas = encontrar_celulas_incorretas(tabuleiro)

if celulas_incorretas:
    print("Células incorretas encontradas:")
    for celula in celulas_incorretas:
        linha, coluna = celula
        print(f"Célula ({linha}, {coluna})")
else:
    print("Tabuleiro válido.")
