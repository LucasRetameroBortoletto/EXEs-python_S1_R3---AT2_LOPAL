#Exe.4 fibonacci
numeros = int(input("Digite um numero: "))
aux1 = 1
aux2 = 1
# já começa com os dois primeiros da sequência
listaFibonacci = [1,1,]

# tira 2 do range porque a lista já começou com 2 itens
for i in range(numeros - 2):
  fibonacci = aux1 + aux2
  aux2 = aux1
  aux1 = fibonacci
  # joga o novo número no final da lista
  listaFibonacci.append(fibonacci)

print(listaFibonacci)
