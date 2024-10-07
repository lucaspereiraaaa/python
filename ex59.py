# Inicializando as populações
pop_a = 80000
pop_b = 200000

# Taxas de crescimento
taxa_a = 0.03
taxa_b = 0.015

# Contador de anos
anos = 0

# Loop para calcular o número de anos
while pop_a < pop_b:
  pop_a += pop_a * taxa_a
  pop_b += pop_b * taxa_b
  anos += 1

# Imprimindo o resultado
print(f"A população do país A ultrapassará ou igualará a população do país B em {anos} anos.")