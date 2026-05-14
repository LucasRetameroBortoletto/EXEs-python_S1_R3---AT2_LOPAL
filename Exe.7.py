#Exe.7
numero= int(input("Digite uma número para descobrir seu fatorial: "))
resultadoLista = []
originalNumero = numero
numero += 1
resultado = 1

for i in range(1,numero):
    resultado *= i
    # guarda os números como string pra montar a conta visual depois
    resultadoLista.append("{}".format(i))

# inverte a lista pra mostrar a conta decrescente (ex: 5x4x3x2x1)
resultadoLista.reverse()
conta = "x".join(resultadoLista)

print("\n\nO fatorial de {} é {}\n".format(originalNumero , resultado))
print("{}! = {} = {}".format(originalNumero, conta, resultado))