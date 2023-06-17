import string

def verificar_pangrama(frase):
    alfabeto = set(string.ascii_lowercase)
    letras_frase = set(frase.lower())

    return alfabeto.issubset(letras_frase)

frase = input("Digite uma frase: ")

if verificar_pangrama(frase):
    print("A frase é um pangrama.")
else:
    print("A frase não é um pangrama.")
