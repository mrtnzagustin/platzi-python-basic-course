import random

RANDOM_MIN = 1
RANDOM_MAX = 100
CANT_VIDAS = 9

def run():
    cant_vidas = CANT_VIDAS
    numero_aleatorio = random.randint(RANDOM_MIN, RANDOM_MAX)    
    valor_ingresado = int(input("Ingrese un numero entre " + str(RANDOM_MIN) + " y " + str(RANDOM_MAX) + ": "))

    while numero_aleatorio != valor_ingresado and cant_vidas > 0:
        cant_vidas -= 1
        print("Te quedan " + str(cant_vidas+1) + " vidas.")
        mensaje = ''
        if valor_ingresado > numero_aleatorio:
            mensaje = 'Ingresá un numero más chico: '
        else: 
            mensaje = 'Ingresa un numero más grande: '
        valor_ingresado = int(input(mensaje))
    
    if numero_aleatorio == valor_ingresado:
        print("Ganaste")
    else: 
        print("Perdiste")

if __name__ == '__main__':
    run()
