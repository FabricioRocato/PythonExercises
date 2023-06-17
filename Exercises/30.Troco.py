def calcular_troco(total, pago):
    troco = pago - total
    cedulas = [100, 50, 10, 5, 1]
    moedas = [0.50, 0.10, 0.05, 0.01]
    resultado = {}

    for cedula in cedulas:
        quantidade = int(troco // cedula)
        if quantidade > 0:
            resultado[cedula] = quantidade
            troco -= quantidade * cedula

    for moeda in moedas:
        quantidade = int(troco // moeda)
        if quantidade > 0:
            resultado[moeda] = quantidade
            troco -= quantidade * moeda

    return resultado

total_a_pagar = float(input("Valor total a ser pago: "))
valor_pago = float(input("Valor efetivamente pago: "))

troco = calcular_troco(total_a_pagar, valor_pago)

print("Troco:")
for valor, quantidade in troco.items():
    print(f"{quantidade} {'cédula' if valor.is_integer() else 'moeda'} de R${valor:.2f}")
