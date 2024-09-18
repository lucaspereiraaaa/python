num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada (Soma ou Subtração): ")

if operacao == "Soma":
  resultado = num1 + num2
  print("O resultado da soma é:", resultado)
elif operacao == "Subtração":
  resultado = num1 - num2
  print("O resultado da subtração é:", resultado)
else:
  print("Operação inválida!")
