import random

RANDOM_MIN = 1
RANDOM_MAX = 100

def run():
    numero_aleatorio = random.randint(RANDOM_MIN, RANDOM_MAX)    
    valor_ingresado = int(input("Ingrese un numero entre " + str(RANDOM_MIN) + " y " + str(RANDOM_MAX) + ": "))

    while numero_aleatorio != valor_ingresado:
        mensaje = ''
        if valor_ingresado > numero_aleatorio:
            mensaje = 'Ingresá un numero más chico: '
        else: 
            mensaje = 'Ingresa un numero más grande: '
        valor_ingresado = int(input(mensaje))
    
    print("Ganaste")

if __name__ == '__main__':
    run()
