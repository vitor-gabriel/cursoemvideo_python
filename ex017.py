import math

cat_a = float (input('Digite o cateto adjacente: '))
cat_o = float (input('Digite o cateto oposto: '))

hipo = math.sqrt ((cat_a ** 2) + (cat_o ** 2))

print('A hipotenusa é: {}'.format(hipo))