import random

n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input('Digite o nome do querto aluno: ')

lista = [n1, n2, n3, n4]

random.shuffle(lista)

print ('A ordem da lista será: ')
print (lista)