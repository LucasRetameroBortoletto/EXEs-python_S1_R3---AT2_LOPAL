#Exe.6
numero = int(input("Digite um número: "))
# números menores que 2 não entram na regra de primos
if numero < 2:
  print("O número {} não é primo".format(numero))
else:
  # tenta dividir por todos os números que vêm antes dele
  for i in range(2, numero):
      if numero % i == 0:
          print("O número {} não é primo".format(numero))
          break
  else:
      print("O número {} é primo".format(numero))