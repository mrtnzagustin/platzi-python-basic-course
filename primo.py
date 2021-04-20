def es_primo(numero):
    if numero == 1:
        return False
    else: 
        # Comenzamos dividiendo el numero por si mismo
        numero_actual = numero 
        # Llevamos la cuenta de la cantidad de divisores
        cantidad_divisores = 0
        # Mientras no se llegue al numero 0
        while numero_actual > 0:
            # Se intenta dividir el numero por el numero actual
            if numero % numero_actual == 0:
                # Si la division es entera, entonces lo cuenta como divisor
                cantidad_divisores += 1
            # Si llego a la cantidad de divisores de al menos 3 numeros, estamos ante un numero no primo
            if cantidad_divisores > 2:
                return False
            else: # Si aun no se llego a la cantidad de divisores, se sigue intentando con el siguiente numero como divisor
                numero_actual -= 1
        # Si se llega a esta linea, es porque el numero es primo ya que no tuvo mas de 2 divisores
        return True

def run():
    if es_primo(int(input("Ingrese un numero para ver si es primo: "))):
        print("El numero es primo")
    else:
        print("El numero no es primo")


if __name__ == '__main__':
    run()


    