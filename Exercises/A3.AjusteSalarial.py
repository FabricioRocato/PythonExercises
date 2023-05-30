def calcular_novo_salario(salario, reajuste):
    novo_salario = salario + (salario * reajuste / 100)
    return novo_salario

def main():
    salario = float(input("Digite o salário atual: R$ "))
    reajuste = float(input("Digite o percentual de reajuste (%): "))

    novo_salario = calcular_novo_salario(salario, reajuste)

    print("Novo salário: R$", novo_salario)

if __name__ == "__main__":
    main()
