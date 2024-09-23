deposito = float(input("Digite o valor do depósito: "))
taxa_juros = float(input("Digite a taxa de juros (em decimal): "))

rendimento = deposito * taxa_juros
total = deposito + rendimento

print("Valor do rendimento:", rendimento)
print("Valor total:", total)