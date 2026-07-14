lista = []
contador = 0

recorrido = {
"R001": ["Santiago", "Valparaíso", 120, "normal", "día", True],
"R002": ["Santiago", "Concepción", 500, "cama", "noche", True],
"R003": ["La Serena", "Coquimbo", 15, "normal", "día", False],
"R004": ["Temuco", "Valdivia", 165, "semi-cama", "día", True],
"R005": ["Iquique", "Arica", 310, "cama", "noche", False],
"R006": ["Santiago", "Rancagua", 90, "normal", "día", True],
}

venta = {
"R001": [7990, 20],
"R002": [25990, 0],
"R003": [1990, 35],
"R004": [12990, 8],
"R005": [18990, 3],
"R006": [4990, 12]
}

def validar_int_entero(mensaje:str):
    while(True):
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                print ("el valor debe ser mayor a 0")
            else:
                return valor
        except:
            print("ingtese un valor numerico entero")

def asientos_origen(mensaje:str):
    for i in recorrido:
        valor = input(mensaje).capitalize
        if valor == i:
            print(i["R001"])

            


def menu():
    while(True):
        print("1. Asientos por ciudad de origen")
        print("2. Búsqueda de recorridos por rango de precio")
        print("3. Actualizar precio de recorrido")
        print("4. Agregar recorrido")
        print("5. Eliminar recorrido")
        print("6. Salir")

        opc = validar_int_entero("ingresa una opcion: ")
        if opc != 1 and opc != 2 and opc != 3 and opc != 4 and opc != 5 and opc != 6:
            print("ingrese una opcion valida")
        elif opc == 1:
            asientos_origen("ingrese su ciudad  de origen: ")
        elif opc == 6:
            print("saliendo...")
            break

        
menu()