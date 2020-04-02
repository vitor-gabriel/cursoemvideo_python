a = input('Digite um caractere: ')

print(type(a))
print('Tem somente letras?: ', a.isalpha())
print('Tem somente numeros?: ', a.isnumeric())
print('Tem somente espaços?:', a.isspace())
print('É alfanumerico?:', a.isalnum())
print('É somente numeros?:', a.isnumeric())
print('É capitalizada:', a.istitle())
