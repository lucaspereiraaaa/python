numero = int(input("Digite um número entre 0 e 99: "))

unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
dezenas = ["", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
dezenas_especiais = ["", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]

if numero == 0:
    print("zero")
elif numero < 10:
    print(unidades[numero])
elif numero < 20:
    print(dezenas_especiais[numero - 10])
elif numero < 100:
    dezena = numero // 10
    unidade = numero % 10
    if unidade == 0:
        print(dezenas[dezena])
    else:
        print(dezenas[dezena], "e", unidades[unidade])
else:
    print("Número inválido. Digite um número entre 0 e 99.")