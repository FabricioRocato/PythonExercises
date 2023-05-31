# Leitura das quatro notas bimestrais
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

# Cálculo da média
media = (nota1 + nota2 + nota3 + nota4) / 4

# Verificação da situação do aluno
if media >= 5:
    print("Aprovado")
else:
    print("Reprovado")

# Apresentação do valor da média
print("Média:", media)
