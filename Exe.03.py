#Exe.3
palavra=input("Digite uma palavra: ")

# contador pra ajudar a fatiar a palavra
quantidade = 1

for letras in palavra:
    # vai printando pedaços cada vez maiores da string
    print(palavra[0:quantidade])
    quantidade += 1
    