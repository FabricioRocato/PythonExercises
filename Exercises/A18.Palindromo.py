def eh_palindromo(palavra):
    # Removendo espaços em branco e convertendo para minúsculas
    palavra = palavra.replace(" ", "").lower()

    # Verificando se a palavra é igual à sua reversa
    return palavra == palavra[::-1]

# Leitura da palavra, frase ou número
entrada = input("Digite uma palavra, frase ou número: ")

# Verificando se é um palíndromo
resultado = eh_palindromo(entrada)

# Imprimindo o resultado
print("Palavra/Frase/Número:", entrada)
print("É palíndromo?", resultado)
