def trocar_valores(a, b):
    temp = a
    a = b
    b = temp
    return a, b

def main():
    a = input("Digite o valor de A: ")
    b = input("Digite o valor de B: ")

    # Convertendo os valores para o tipo adequado (ex: int, float)
    a = int(a)
    b = int(b)

    print("Valores antes da troca:")
    print("A:", a)
    print("B:", b)

    a, b = trocar_valores(a, b)

    print("Valores após a troca:")
    print("A:", a)
    print("B:", b)

if __name__ == "__main__":
    main()
