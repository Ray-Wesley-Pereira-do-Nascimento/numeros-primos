def primos(num):
  cont  = 0
  for i in range(1, num+1):
    if num % i == 0:
      cont += 1
  if cont == 2:
    return print(f'{num} é um número primo!')
  else:
    return print(f'{num} não é um número primo!')

n = int(input("Digite um número: "))
primos(n)

