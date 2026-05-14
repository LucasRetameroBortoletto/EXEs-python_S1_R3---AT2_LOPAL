#Exe.11
numero = int(input("Digite um numero para descobrir sua tabuada: "))
print("\n")
print("Tabuada {}\n".format(numero))

# roda do 1 até o 10
for i in range(1, 11):
  resultado = numero * i
  print("{} x {} = {}".format(numero, i, resultado))
  