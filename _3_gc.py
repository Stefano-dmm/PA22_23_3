import json

class Cliente:
    def __init__(self, nombre, cedula_rif, correo):
        self.nombre = nombre
        self.cedula_rif = cedula_rif
        self.correo = correo


    # Leer la información del archivo JSON y crear objetos de cliente
with open('clientes.json', 'r') as f:
    clientes_json = json.load(f)

clientes = []
for cliente_json in clientes_json:
    cliente = Cliente(cliente_json["nombre"], cliente_json["cedula o rif"], cliente_json["correo"])
    clientes.append(cliente)

def aggc(clientes):
    # Pedir al usuario que ingrese los datos del nuevo cliente
    nombre = input("Ingrese el nombre del nuevo cliente: ")
    cedula_rif = input("Ingrese la cedula o rif del nuevo cliente: ")
    correo = input("Ingrese el correo del nuevo cliente: ")

    # Crear un nuevo objeto de cliente con los datos ingresados
    nuevo_cliente = Cliente(nombre, cedula_rif, correo)

    # Agregar el nuevo objeto a la lista existente
    clientes.append(nuevo_cliente)

    # Escribir la lista actualizada de objetos en el archivo JSON
    with open('clientes.json', 'w') as f:
        json.dump([cliente.__dict__ for cliente in clientes], f)

    print(f"El cliente '{nombre}' ha sido agregado al archivo 'clientes.json'.")

def cierre_mgc():
    
        cmgc = int(input('1 - volver a menu inicial \n2 - volver al menu de gestion de clientes \n3 - cerrar \n>>>'))
        if cmgc == 1:
           #lo se, poco profesional, pero sirve y es la manera que encontre para que no me de errores
           print
        elif cmgc == 2:
            MGC()
        elif cmgc == 3:
            print('adios')
        else:
            print ('opcion del menu no seleccionado') 
            cierre_mgc()

def mc(clientes):
    # Pedir al usuario que ingrese el nombre del cliente a modificar
    nombre = input("Ingrese el nombre del cliente a modificar para confirmar: ")

    # Buscar el objeto de cliente correspondiente y modificar sus datos
    for cliente in clientes:
        if cliente.nombre == nombre:
            cliente.nombre = input("Ingrese el nuevo nombre del cliente: ")
            cliente.cedula_rif = input("Ingrese el nuevo cedula o rif del cliente: ")
            cliente.correo = input("Ingrese el nuevo correo del cliente: ")
            break

    # Escribir la lista actualizada de objetos en el archivo JSON
    with open('clientes.json', 'w') as f:
        json.dump([cliente.__dict__ for cliente in clientes], f)

    print(f"El cliente '{nombre}' ha sido modificado en el archivo 'clientes.json'.")

def ec(clientes):
    # Pedir al usuario que ingrese el nombre del cliente a eliminar
    nombre = input("Ingrese el nombre del cliente a eliminar para confirmar: ")

    # Buscar el objeto de cliente correspondiente y eliminarlo de la lista
    for cliente in clientes:
        if cliente.nombre == nombre:
            clientes.remove(cliente)
            break

    # Escribir la lista actualizada de objetos en el archivo JSON
    with open('clientes.json', 'w') as f:
        json.dump([cliente.__dict__ for cliente in clientes], f)

    print(f"El cliente '{nombre}' ha sido eliminado del archivo 'clientes.json'.")


#buscadores
def buscador():
    # Pedir al usuario que ingrese el término de búsqueda y el campo de búsqueda
    search_term = input("¿Qué objeto estás buscando? \n>>> ")

    # Mostrar opciones de campo de búsqueda y pedir al usuario que ingrese una opción numérica
    search_field_option = int(input(" ¿En qué campo deseas realizar la búsqueda? \n1. Nombre \n2. Cedula o rif \n3. Correo \n>>> "))

    # Convertir la opción numérica en un campo de búsqueda válido
    if search_field_option == 1:
        search_field = "nombre"
    elif search_field_option == 2:
        search_field = "cedula o rif"
    elif search_field_option == 3:
        search_field = "correo"
    else:
        print(f"\n Opción {search_field_option} no válida.")
        return

    # Buscar los objetos de cliente que coinciden con el término de búsqueda y el campo de búsqueda
    clientes_encontrados = []
    for cliente in clientes:
        if search_field == "nombre" and search_term.lower() in cliente.nombre.lower():
            clientes_encontrados.append(cliente)
        elif search_field == "cedula o rif" and search_term.lower() in cliente.cedula_rif.lower():
            clientes_encontrados.append(cliente)
        elif search_field == "correo" and search_term.lower() in cliente.correo.lower():
            clientes_encontrados.append(cliente)

    # Imprimir los resultados de la búsqueda
    if len(clientes_encontrados) == 0:
        print(f"\n No se encontraron resultados para '{search_term}' en el campo '{search_field}'.")
    else:
        print(f"\n Se encontraron {len(clientes_encontrados)} resultados para '{search_term}' en el campo '{search_field}': \n")
        for cliente in clientes_encontrados:
            print(f"Nombre: {cliente.nombre}")
            print(f"Cedula o rif: {cliente.cedula_rif}")
            print(f"Correo: {cliente.correo}")
            print()

def MGC():
    
    while True:
        menu_1mgc = int(input ('1 - Registro de nuevo cliente \n2 - Modificacion de cliente existente \n3 - menu de cierre \n >>>'))
        if menu_1mgc == 1:
            aggc(clientes)
            cierre_mgc()
            break
        elif menu_1mgc == 2:
            while True:
                #buscador de objeto cliente, luego de encontrar cliente
                buscador()
                menu_2mgc = int(input('1 - Eliminar Cliente \n2 - Modificar Cliente \n 3 - menu de cierre \n>>>'))
                if menu_2mgc == 1:
                    #eliminar el cliente buscado anteriormente
                    ec(clientes)
                    cierre_mgc()
                    break
                elif menu_2mgc == 2:
                    #editar el producto cliente anteriormente
                    mc(clientes)
                    cierre_mgc()
                    break

                elif menu_2mgc == 3:
                    cierre_mgc()
                    break
            
                else:
                    print ('opcion del menu no seleccionado')

            cierre_mgc()
            break

        elif menu_1mgc == 3:
            cierre_mgc()
            break
                    
        else:
                print ('opcion del menu no seleccionado')

        break
    