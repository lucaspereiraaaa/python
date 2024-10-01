def potencia(base, expoente):
    """
    Calcula a potência de um número.

    Args:
        base: O número base.
        expoente: O expoente.

    Returns:
        A potência do número base.
    """
    if expoente <= 10:
        return base ** expoente
    else:
        return "Expoente inválido. O expoente deve ser no máximo 10."

while True:
    try:
        base = int(input("Digite a base: "))
        expoente = int(input("Digite o expoente: "))
        if base > 0 and expoente > 0:
            resultado = potencia(base, expoente)
            print(f"{base} elevado a {expoente} é igual a {resultado}")
            break
        else:
            print("Os números devem ser maiores que zero.")
    except ValueError:
        print("Entrada inválida. Digite números inteiros.")