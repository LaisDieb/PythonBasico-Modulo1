qnt = 0
soma = 0
media = 0
valor = float(input("Digite um valor: "))

while (valor > 0.0):
    soma = soma+valor
    qnt = qnt+1
    #Entrada de valores
    valor = float(input("Digite um valor: "))

#Caso digite um valor negativo o laço encerra
media = soma/qnt
print("\n Total da soma: ", soma)
print("\n Quantidade de valores digitados: ", qnt)
print("\n Média dos valores: ", media)