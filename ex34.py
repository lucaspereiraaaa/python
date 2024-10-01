def calcula_peso_ideal(h, sexo):
  """
  Calcula o peso ideal de uma pessoa com base na altura e sexo.

  Args:
    h: A altura da pessoa em metros.
    sexo: O sexo da pessoa, "H" para homem e "M" para mulher.

  Returns:
    O peso ideal da pessoa.
  """
  if sexo == "H":
    return (72.7 * h) - 58
  elif sexo == "M":
    return (62.1 * h) - 44.7
  else:
    return "Sexo inválido."

# Exemplo de uso: