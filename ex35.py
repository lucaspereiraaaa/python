area = float(input("Digite a área a ser pintada (em m²): "))
litros_necessarios = area / 3
latas_necessarias = int(litros_necessarios / 18) + 1  # Arredonda para cima para garantir tinta suficiente
preco_total = latas_necessarias * 80
print(f"Você precisará de {latas_necessarias} latas de tinta.")
print(f"O preço total será de R$ {preco_total:.2f}.")