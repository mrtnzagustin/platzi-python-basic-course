# Indica si la letra indicada es una vocal
def es_vocal(letra):
    return letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'

def run():
    # Imprime valores desde el 5 (inclusive) hasta el 101(no inclusive)
    for interador in range(5, 101):
        print("Estas en la iteración ["+str(interador)+"]")

    # Solicita una frase y muestra cada posicion
    frase_input = input("Ingresa una frase: ")

    # Itera con for desde 0 hasta el final del input
    print("Imprime recorriendo posicion a posicion por index")
    for posicion in range(0, len(frase_input)):
        print("Caracter en posicion [" + str(posicion) +"]: " + frase_input[posicion])
    
    # Itera letra por letra de una cadena
    print("Imprime recorriendo letra a letra")
    for letra in frase_input:
        print("Caracter : " + letra)

    # Solo muestra las vocales de la frase
    print("Imprime solo vocales")
    for letra in frase_input:
        if es_vocal(letra):
            print("Caracter : " + letra)
        else:
            continue

    # Solo muestra las vocales de la frase
    print("Imprime solo hasta la primera vocal")
    for letra in frase_input:
        print("Caracter : " + letra)
        if es_vocal(letra):
            break

if __name__ == '__main__':
    run()