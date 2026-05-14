#Exe.2
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
num3 = int(input("Digite um numero: "))
numerosLista = [num1, num2, num3] #colocamos os 3 número digitados em uma lista
#As funções embutidas max e min, pegam os maiores e os menores valores dentro uma lista ou coleção(no caso aqui lista)
maiorValor = max(numerosLista)
menorValor = min(numerosLista)
print("O maior valor é {}".format(maiorValor))
print("O menor valor é {}".format(menorValor))
