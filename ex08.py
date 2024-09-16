letra = input("Digite uma letra: ")

if letra.lower() in 'aeiou':
    print(f"A letra '{letra}' é uma vogal.")
else:
    print(f"A letra '{letra}' é uma consoante.")