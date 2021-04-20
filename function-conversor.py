PESOS_ARGENTINOS = '1'
PESOS_COLOMBIANOS = '2'
PESOS_MEXICANOS = '3'

menu = """
    Bienvenido al conversor de monedas :)
1 - Pesos Argentinos
2 - Pesos Colombianos
3 - Pesos Mexicanos

Ingresa opcion: """

def obtener_cotizacion(opcion):
    if opcion == PESOS_ARGENTINOS:
        return 97.5
    elif opcion == PESOS_MEXICANOS:
        return 30
    elif opcion == PESOS_COLOMBIANOS:
        return 3800

opcion = input(menu)

while opcion != PESOS_ARGENTINOS and opcion != PESOS_COLOMBIANOS and opcion != PESOS_MEXICANOS:
    print("Opcion incorrecta: ["+opcion+"]")
    opcion = input(menu)

pesos = int(input("Ingresa cuantos pesos tenes: "))

print("Tienes en total " + str(round(pesos / obtener_cotizacion(opcion), 2)) + " dolares")