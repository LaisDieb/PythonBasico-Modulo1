notaA = float(input("Informe a primeira nota: "))
notaB = float(input("Informe a segunda nota: "))

#calcular media
mediafinal = (notaA + notaB)/2

if mediafinal>=7:
    print("Média: %.2f - Aprovado." % mediafinal)
else:
    print("Média: %.2f - Reprovado." % mediafinal)