PESOS_ARGENTINOS = '1'
PESOS_COLOMBIANOS = '2'
PESOS_MEXICANOS = '3'

# Menu principal con multi line string
menu = """
    Bienvenido al conversor de monedas :)
1 - Pesos Argentinos
2 - Pesos Colombianos
3 - Pesos Mexicanos

Ingresa opcion: """

# Funcion encargada de obtener  cotizacion para cierto tipo de opcion
def obtener_cotizacion(opcion):
    if opcion == PESOS_ARGENTINOS:
        return 97.5
    elif opcion == PESOS_MEXICANOS:
        return 30
    elif opcion == PESOS_COLOMBIANOS:
        return 3800

# Obtencion de opcion
opcion = input(menu)

# validacion de opcion y re-solicitud
while opcion != PESOS_ARGENTINOS and opcion != PESOS_COLOMBIANOS and opcion != PESOS_MEXICANOS:
    print("Opcion incorrecta: ["+opcion+"]")
    opcion = input(menu)

# Obtencion de pesos
pesos = int(input("Ingresa cuantos pesos tenes: "))

# Impresion de conversion
print("Tienes en total " + str(round(pesos / obtener_cotizacion(opcion), 2)) + " dolares")