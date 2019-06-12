#F.U.P. que calcule o tempo de utilização de um patinete elétrico. Você deve saber que existe uma taxa de utilização que permite ao usuário utilizar o patinete por 10 minutos que é de R$5,00.
#Passando disso o preço é acrescido de 20% por minuto. Ao final da utilização deve ser mostrado ao usuário o quanto deve pagar pela utlização.

tempo = int (input ("Tempo utilizado:"))

vporcentagem = (20 * 5) / 100

tempoexc = tempo - 10

if tempo <= 10:
    print ("Valor a ser pago: R$ 5,00")
else:
  print("Valor a ser pago: R$", (tempoexc * vporcentagem) + 5)