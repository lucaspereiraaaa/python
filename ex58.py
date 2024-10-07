# Ler o número de litros vendidos
litros = float(input("Digite o número de litros vendidos: "))

# Ler o tipo de combustível
tipo_combustivel = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").upper()

# Calcular o valor a ser pago
if tipo_combustivel == "A":
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
    valor_a_pagar = litros * 3.90 * (1 - desconto)
elif tipo_combustivel == "G":
    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
    valor_a_pagar = litros * 5.50 * (1 - desconto)
else:
    print("Tipo de combustível inválido.")
    valor_a_pagar = 0

# Imprimir o valor a ser pago
print("Valor a ser pago: R$ {:.2f}".format(valor_a_pagar))