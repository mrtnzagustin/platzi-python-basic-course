def run():
    persona = {
        "nombre": "Juan Agustin",
        "apellido": "Martinez",
        "edad": 30
    }
    # Impresion por cada clave - valor
    print(persona["nombre"] + ", " + persona["apellido"])
    print("Edad: " + str(persona["edad"]))

    casos_covid_por_pais = {
        "Argentina": 400000,
        "Chile": 20000,
        "Brasil": 1100000
    }

    # Recorrida de cada key
    for llave_pais in casos_covid_por_pais.keys():
        print(llave_pais + ": " + str(casos_covid_por_pais[llave_pais]))
    
    # Recorrida de cada value
    for casos_pais_actual in casos_covid_por_pais.values():
        print("Casos: " + str(casos_pais_actual) )

    # Itera y a su vez permite acceso a clave y valor
    for pais, casos in casos_covid_por_pais.items():
        print(pais + ": " + str(casos))
if __name__ == '__main__':
    run()