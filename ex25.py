def calcular_fatorial(numero):
    """Calcula o fatorial de um número.

    Args:
        numero: Um número inteiro positivo.

    Returns:
        O fatorial do número.
    """
    if numero == 0:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)

def main():
    """
    Recebe um número positivo e maior que zero, calcula e mostra o fatorial, a soma dos dígitos e o número invertido.
    """
    while True:
        try:
            numero = int(input("Digite um número positivo e maior que zero: "))
            if numero > 0:
                break
            else:
                print("Número inválido. Digite um número positivo e maior que zero.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    fatorial = calcular_fatorial(numero)
    print(f"O fatorial de {numero} é {fatorial}")

if __name__ == "__main__":
    main()