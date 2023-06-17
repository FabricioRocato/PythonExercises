def verificar_ganhador(jogador1, jogador2):
    if jogador1 == jogador2:
        return "Empate"
    elif (
            (jogador1 == "Tesoura" and jogador2 == "Papel")
            or (jogador1 == "Papel" and jogador2 == "Pedra")
            or (jogador1 == "Pedra" and jogador2 == "Lagarto")
            or (jogador1 == "Lagarto" and jogador2 == "Spock")
            or (jogador1 == "Spock" and jogador2 == "Tesoura")
            or (jogador1 == "Tesoura" and jogador2 == "Lagarto")
            or (jogador1 == "Lagarto" and jogador2 == "Papel")
            or (jogador1 == "Papel" and jogador2 == "Spock")
            or (jogador1 == "Spock" and jogador2 == "Pedra")
            or (jogador1 == "Pedra" and jogador2 == "Tesoura")
    ):
        return "Jogador 1"
    else:
        return "Jogador 2"


jogador1 = input("Jogador 1, escolha entre Pedra, Papel, Tesoura, Lagarto ou Spock: ")
jogador2 = input("Jogador 2, escolha entre Pedra, Papel, Tesoura, Lagarto ou Spock: ")

resultado = verificar_ganhador(jogador1, jogador2)
print(f"Resultado: {resultado}")
