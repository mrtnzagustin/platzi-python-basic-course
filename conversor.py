# Variable encargada de recibir input de pesos
pesos_argentinos = int(input("Ingresar tus pesos argentinos: "))

# Cotizacion del dolar abril 2021
cotizacion_dolar = 97.5

# Print de conversion con round
print("Tienes en total " + str(round(pesos_argentinos / cotizacion_dolar, 2)) + " dolares")