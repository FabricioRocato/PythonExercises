def quebrar_linhas(frase, colunas):
    palavras = frase.split()
    linhas = []
    linha_atual = ""

    for palavra in palavras:
        if len(linha_atual) + len(palavra) <= colunas:
            linha_atual += palavra + " "
        else:
            linhas.append(linha_atual.strip())
            linha_atual = palavra + " "

    linhas.append(linha_atual.strip())

    return linhas


frase = input("Digite uma frase: ")
colunas = int(input("Digite a quantidade de colunas: "))

linhas_quebradas = quebrar_linhas(frase, colunas)

for linha in linhas_quebradas:
    print(linha)
