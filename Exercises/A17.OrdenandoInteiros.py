# Leitura dos elementos
elementos = []
for i in range(12):
    elemento = int(input("Digite um elemento: "))
    elementos.append(elemento)

# Ordenação em ordem decrescente
elementos.sort(reverse=True)

# Apresentação dos elementos ordenados
print("Elementos ordenados em ordem decrescente:")
for elemento in elementos:
    print(elemento)
