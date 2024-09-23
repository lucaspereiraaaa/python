import math

def equacao_2_grau(a, b, c):
    """
    Calcula as raízes da equação do 2º grau "ax²+bx+c=0".

    Args:
        a: Coeficiente do termo quadrático.
        b: Coeficiente do termo linear.
        c: Termo constante.

    Returns:
        Uma tupla com as raízes da equação, ou None se a equação não possui raízes reais.
    """
    delta = b**2 - 4 * a * c
    if delta >= 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return (x1, x2)
    else:
        return None
