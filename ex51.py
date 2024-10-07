numero = int(input("Digite um número inteiro: "))
e_primo = True
for i in range(2, numero):
  if numero % i == 0:
    e_primo = False
    break
if e_primo:
  print(f"{numero} é um número primo.")
else:
  print(f"{numero} não é um número primo.")