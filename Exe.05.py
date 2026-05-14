#Exe.5 -- validação de informações
#faz a validação do nome
while True:
  nome = str(input("Digite seu nome[minimo de 4 caracteres]: "))
  tamanhoNome = len(nome)
  if tamanhoNome > 3:
    break
  else:
    print("Seu nome deve conter no minimo 4 caracteres")

#faz a validação de idade
while True:
  idade = int(input("Digite sua idade: "))
  if idade < 150 and idade > 0:
    break
  else:
    print("--> {} <-- não é uma informação válida.".format(idade))

# faz a validação do salario:
while True:
  salario = float(input("Digite seu salario: "))

  if salario > 0 :
    break
  elif salario == 0:
    print("Pare de mentir 🤨🤨, --> {} <-- não é um valor valido!!".format(salario))
  elif salario < 0:
    print("Ta devendo é amigo? --> {} <-- não é um valor valido!!".format(salario))

#faz a validação para o sexo do usuario
while True:
  sexo = str(input("Digite seu sexo[F/M]: "))
  sexo = sexo.upper()
  if sexo == 'F' or sexo == 'M':
    break
  else:
    print("Digite F para feminino ou M para masculino, --> {} <-- não é uma opção válida.".format(sexo))

#Faz a verificação do estado civil do usuario
while True:
  estadoCivil = str(input("Digite seu estado civil[S/C/V/D]: "))
  estadoCivil = estadoCivil.upper()
  if estadoCivil == "S" or estadoCivil == "C" or estadoCivil == "V" or estadoCivil == "D":
    break
  else:
    print("\n-->{}<-- não é uma informação válida".format(estadoCivil))
    print("S --> Solteiro(a) \nC --> Casado(a) \nV --> Viúvo(a) \nD --> Divorciado(a)")

print("\n\nInformações registradas:\n")
print(f"{'Nome':.<25}{nome}")
print(f"{'Idade':.<25}{idade}")
print(f"{'Salário':.<25}{salario}")
print(f"{'Sexo':.<25}{sexo}")
print(f"{'Estado civil':.<25}{estadoCivil}")
