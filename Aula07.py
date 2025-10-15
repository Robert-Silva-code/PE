""" Q01
print('Números pares de 1 até 50: ')
for c in range(1, 50+1):
    if c % 2 == 0:
        print(c)
"""

""" Q02
x = int(input('Digite um número: '))
c = 0
for c in range(10):
    print('{} x {} = {}'.format(x,c+1,x*(c+1)))
"""

""" Q03
palavra = input('Digite uma palavra: ')

for letra in palavra:
    print(letra)
"""



""" Q04
impares = []
for c in range(1, 100+1):
    if c % 2 == 1:
        impares.append(c)
sp = sum(impares)
print(f'A soma de todos os números ímpares de 1 até 100 é: {sp}')
"""

""" Q05
frase = input('Escreva uma frase: ')
vogais = 'aeiou'
contadorVogal = 0

for letra in frase:
    if letra in vogais:
        contadorVogal += 1

print(f'A sua frase tem {contadorVogal} vogais!')
"""


palavra = input('Digite uma palavra: ')
palavraInvertida = ''

for letra in palavra:
    palavraInvertida = letra + palavraInvertida

print("A palavra ao contrário é:", palavraInvertida)