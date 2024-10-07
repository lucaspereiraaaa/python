numero = int(input("Digite um número inteiro entre 1 e 10: "))

if 1 <= numero <= 10:
    print("TABUADA de", numero, ":")
    for i in range(1, 11):
        print(numero, "X", i, "=", numero * i)
else:
    print("Número inválido. Digite um número entre 1 e 10.")