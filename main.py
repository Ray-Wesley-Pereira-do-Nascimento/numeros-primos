#Verificar se o número é primo ou não

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

#Mostra os primos de 2 até 100

def primosAteCem():
  for i in range(2, 100):
    for j in range(2, i):
      if i % j == 0:
        break
    else:
      print(i, end = " ")

print("\nNúmeros primos de 2 a 100:")
primosAteCem()

