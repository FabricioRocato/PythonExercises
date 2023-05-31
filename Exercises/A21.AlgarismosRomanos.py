def converter_romano_para_inteiro(s):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    i = 0

    while i < len(s):
        if i + 1 < len(s) and valores[s[i]] < valores[s[i + 1]]:
            total += valores[s[i + 1]] - valores[s[i]]
            i += 2
        else:
            total += valores[s[i]]
            i += 1

    return total

# Leitura do numeral romano
s = input("Digite um numeral romano: ")

# Convertendo para inteiro
resultado = converter_romano_para_inteiro(s)

# Imprimindo o resultado
print("O numeral romano", s, "corresponde ao número inteiro", resultado)
