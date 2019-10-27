# juego para adivinar un numero entre 0 a 9

import random
numero = random.randint(0,9) # usamos el modulo random para crear un numero aleatorio

print('''
        Adivina el numero
    +++++++++++++++++++++++++++++++
    intenta adivinar el numero
    1. ingresa el numero de intentos que deseas hacer
    2. ingresa solo numero enteras que van del 0 al 9
    3. prueba tu Suerte ''')


intento = int(input('Cuantos intentos quieres hacer:'))
start = input('Precione Enter para empezar')
i=1
while i <= intento :
    valor = int(input('ingrese un numero: '))
    if valor == numero:
        print(f'has acertado el numero es {numero} y has realizado {i} intentos')
        break
    else:
        i+=1
        print('! intentalo denuevo !')
