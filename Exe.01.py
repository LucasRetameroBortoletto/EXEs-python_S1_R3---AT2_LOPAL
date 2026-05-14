#Exe.1
# vai do 0 ao 100
for i in range(0, 101):
  # checa se o resto da divisão é 0 pra saber se é par
  if i % 2 == 0:
    print("Esse número é par: {}".format(i))
  else:
    print("Esse número é impar: {}".format(i))
    