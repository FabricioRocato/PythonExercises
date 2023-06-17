def fibonacci(numero):
    fibonacci_seq = [0, 1]

    while fibonacci_seq[-1] <= numero:
        novo_numero = fibonacci_seq[-1] + fibonacci_seq[-2]
        fibonacci_seq.append(novo_numero)

    return fibonacci_seq[:-1]


numero = int(input("Digite um número: "))
sequencia_fibonacci = fibonacci(numero)

print("Sequência de Fibonacci:")
for num in sequencia_fibonacci:
    print(num, end=" ")
