def fibonacci(n):
    """
    Função que calcula a série de Fibonacci até o n-ésimo termo.

    Args:
        n (int): O número de termos da série de Fibonacci a ser calculada.

    Returns:
        list: Uma lista contendo os n primeiros termos da série de Fibonacci.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    else:
        fib_list = [1, 1]
        for i in range(2, n):
            fib_list.append(fib_list[i - 1] + fib_list[i - 2])
        return fib_list