# Funcion encargada de determinar si una frases es palindromo
def es_palindromo(frase):
    # Pasamos a minusculas y sacamos los espacios
    frase = frase.lower().replace(" ","")
    # Comparamos si la frase conincide con su inversa
    return frase == frase[::-1]

def run():
    # Leemos la frase
    frase = input("Ingrese una frase: ")
    # Analizamos si la frases es igual a su inversa
    if es_palindromo(frase):
        print("Es palíndromo")
    else:
        print("No es palíndromo")

if __name__ == "__main__":
    run()