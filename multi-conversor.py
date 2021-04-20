menu = """
    Bienvenido al conversor de monedas :)
1 - Pesos Argentinos
2 - Pesos Colombianos
3 - Pesos Mexicanos

Ingresa opcion: """

cotizacion_dolar_argentina = 97.5
cotizacion_dolar_mexico = 30
cotizacion_dolar_colombia = 3800

opcion = input(menu)

while opcion != '1' and opcion != '2' and opcion != '3':
    print("Opcion incorrecta: ["+opcion+"]")
    opcion = input(menu)

pesos = int(input("Ingresa cuantos pesos tenes: "))

if opcion == '1':
    print("Tienes en total " + str(round(pesos / cotizacion_dolar_argentina, 2)) + " dolares")
elif opcion == '2':
    print("Tienes en total " + str(round(pesos / cotizacion_dolar_mexico, 2)) + " dolares")
elif opcion == '3':
    print("Tienes en total " + str(round(pesos / cotizacion_dolar_colombia, 2)) + " dolares")
    