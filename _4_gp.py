import json
import time

class Pago:
    def __init__(self, cliente, monto, moneda, tipo_pago, fecha):
        self.cliente = cliente
        self.monto = monto
        self.moneda = moneda
        self.tipo_pago = tipo_pago
        self.fecha = fecha

# lee la información del archivo JSON 
with open('pagos.json', 'r') as f:
    pagos_json = json.load(f)

# Crear objeto
pagos = []
for pago_json in pagos_json:
    pago = Pago(pago_json["cliente"], pago_json["monto"], pago_json["moneda"], pago_json["tipo_pago"], pago_json["fecha"])
    pagos.append(pago)

#Buscador
def buscador():
    # Pedir al usuario que ingrese el término de búsqueda y el campo de búsqueda
    search_term = input("¿Qué objeto estás buscando? \n(ingresa cualquier dato del pago, luego se te preguntara que tipo de dato es)\n>>> ")

    # Mostrar opciones de campo de búsqueda y pedir al usuario que ingrese una opción numérica
    search_field_option = int(input(" ¿En qué campo deseas realizar la búsqueda? \n1. Cliente \n2. Monto \n3. Moneda \n4. Tipo de pago \n5. Fecha \n>>> "))

    # Convertir la opción numérica en un campo de búsqueda válido
    if search_field_option == 1:
        search_field = "cliente"
    elif search_field_option == 2:
        search_field = "monto"
    elif search_field_option == 3:
        search_field = "moneda"
    elif search_field_option == 4:
        search_field = "tipo_pago"
    elif search_field_option == 5:
        search_field = "fecha"
    else:
        print(f"\n Opción {search_field_option} no válida.")
        return

    # Buscar los objetos de pago que coinciden con el término de búsqueda y el campo de búsqueda
    pagos_encontrados = []
    for pago in pagos:
        if search_field == "cliente" and search_term.lower() in pago.cliente.lower():
            pagos_encontrados.append(pago)
        elif search_field == "monto" and str(search_term) in str(pago.monto):
            pagos_encontrados.append(pago)
        elif search_field == "moneda" and search_term.lower() in pago.moneda.lower():
            pagos_encontrados.append(pago)
        elif search_field == "tipo_pago" and search_term.lower() in pago.tipo_pago.lower():
            pagos_encontrados.append(pago)
        elif search_field == "fecha" and search_term.lower() in pago.fecha.lower():
            pagos_encontrados.append(pago)

    # Imprimir los resultados de la búsqueda
    if len(pagos_encontrados) == 0:
        print(f"\n No se encontraron resultados para '{search_term}' en el campo '{search_field}'.")
    else:
        print(f"\n Se encontraron {len(pagos_encontrados)} resultados para '{search_term}' en el campo '{search_field}': \n")
        for pago in pagos_encontrados:
            print(f"Cliente: {pago.cliente}")
            print(f"Monto: {pago.monto}")
            print(f"Moneda: {pago.moneda}")
            print(f"Tipo de pago: {pago.tipo_pago}")
            print(f"Fecha: {pago.fecha}")
            print()

def aggp(pagos):
    # Crear una nueva instancia de pago a partir de los datos ingresados por el usuario
    cliente = input("Cliente: ")
    monto = float(input("Monto: "))
    moneda = input("Moneda: ")
    tipo_pago = input("Tipo de pago: ")
    fecha = input("Fecha: ")
    nuevo_pago = Pago(cliente, monto, moneda, tipo_pago, fecha)

    # Agregar el nuevo pago a la lista de pagos existente
    pagos.append(nuevo_pago)

    # Imprimir un mensaje de confirmación
    print("Pago agregado con éxito a la lista de pagos.")

def cierre_mgp():
    
        cmgp = int(input('1 - volver a menu inicial \n2 - volver al menu de gestion de pagos \n3 - cerrar \n>>>'))
        if cmgp == 1:
           #lo se, poco profesional, pero sirve y es la manera que encontre para que no me de errores
           print
        elif cmgp == 2:
            MGP()
        elif cmgp == 3:
            print("Cerrando programa")
            for i in range(5):
                time.sleep(0.5)
                print(".", end="", flush=True)

            texto = "Adios"
            for i in range(10):
                time.sleep(0.1)
                print("\r" + " " * i + texto, end="", flush=True)
            print("\n")
            exit()
        else:
            print ('opcion del menu no seleccionado') 
            cierre_mgp()

def MGP():
    
    while True:
        menu_1mgp = int(input ('1 - Registrar pago \n2 - Busqueda de pagos \n3 - menu de cierre \n >>>'))
        if menu_1mgp == 1:
            # print el registro 
            aggp(pagos)        
            cierre_mgp()
            break
        elif menu_1mgp == 2:
            #buscador de ventas
            buscador()
            cierre_mgp()
            break
        elif menu_1mgp == 3:
            cierre_mgp()
            break
                    
        else:
                print ('opcion del menu no seleccionado')

        break
    