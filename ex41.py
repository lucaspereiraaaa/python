maior = 0
for i in range(5):
  numero = int(input(f"Digite o {i+1}º número: "))
  if numero > maior:
    maior = numero
print(f"O maior número digitado foi {maior}")