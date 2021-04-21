import random

LONGITUD_CONTRASENA = 15

def generar_contrasena():
    # Listas con diversos caracteres
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G'] # Agregar hasta Z idealmente
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g'] # Agregar hasta z idealmente
    simbolos = [ '!', '"', '$', '%', '&', '/' ]
    numeros = ['1', '2' , '3', '4', '5', '6', '7', '8', '9', '0']
    
    # Unificacion de listas
    caracteres = mayusculas + minusculas + simbolos + numeros

    # Contraseña final, aqui se iran guardando caracteres aleatorios
    contrasena = []

    for i in range(1, LONGITUD_CONTRASENA):
        posicion_caracter = random.randint(0, len(caracteres)-1) # Se puede usar random.choice(caracteres)
        contrasena.append(caracteres[posicion_caracter])

    # Join de la lista de caracteres de la contraseña en un unico string
    return ''.join(contrasena) 


def run():
    contrasena = generar_contrasena()
    print("Tu nueva contraseña es: " + contrasena)


if __name__ == '__main__':
    run()