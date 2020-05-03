dias = int(input('Quantos dias voce ficou com o carro? '))
km = int(input('Quantos kilomentros voce rodou? '))

kmdias = (dias * 60) + (km * 0.15)
print('Voce tem que pagar R${}.'.format(kmdias))