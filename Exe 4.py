#F.U.P. que peça um número inteiro e determine se ele é ou não um número primo.
#Um número primo é aquele que é divisível somente por ele mesmo e por 1.
num = int(input("\nInforme um número inteiro: "))
cont = 0
div = []

for i in range(num):

    if num % (i + 1) == 0:

        cont += 1
        div.append(i + 1)

    else:

        cont

if cont == 2:

    print("O numero é primo divisivel por ", div)

else:

    print("O numero não é primo pois é divisivel por ", div)