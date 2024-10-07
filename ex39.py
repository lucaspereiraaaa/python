numero = int(input("Digite um número inteiro menor que 1000: "))

centenas = numero // 100
dezenas = (numero % 100) // 10
unidades = numero % 10

if centenas > 0:
    print(f"{centenas} {'centena' if centenas == 1 else 'centenas'},", end=" ")
if dezenas > 0:
    print(f"{dezenas} {'dezena' if dezenas == 1 else 'dezenas'}", end=" ")
    if unidades > 0:
        print("e", end=" ")
if unidades > 0:
    print(f"{unidades} {'unidade' if unidades == 1 else 'unidades'}")