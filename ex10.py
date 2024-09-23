def tipo_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b and a == c:
            return "Triângulo Equilátero"
        elif a == b or a == c or b == c:
            return "Triângulo Isósceles"
        else:
            return "Triângulo Escaleno"
    else:
        return "Não forma um triângulo"

# Entrada dos lados do triângulo
lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

# Chamada da função e exibição do resultado
resultado = tipo_triangulo(lado1, lado2, lado3)
print(resultado)