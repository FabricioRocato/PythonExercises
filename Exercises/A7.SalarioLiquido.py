# Ler os dados do professor
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
valor_hora_aula = float(input("Digite o valor da hora-aula: "))
percentual_desconto = float(input("Digite o percentual de desconto do INSS: "))

# Calcular o salário bruto
salario_bruto = horas_trabalhadas * valor_hora_aula

# Calcular o valor do desconto do INSS
desconto_inss = salario_bruto * (percentual_desconto / 100)

# Calcular o salário líquido
salario_liquido = salario_bruto - desconto_inss

# Apresentar os valores dos salários bruto e líquido
print("Salário bruto: R$", salario_bruto)
print("Salário líquido: R$", salario_liquido)
