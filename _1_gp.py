import json
import requests
import time
from Clase_itm import Producto

#conectar a github, respaldo si json no tiene nada
try:
    with open('products.json', 'r') as f:
        data = json.load(f)
        
        if len(data) == 0:
            print("El archivo JSON está vacío.")
            response = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/e20c412e7e1dcc3b089b0594b5a42f30ac15e49b/products.json')
            data = response.json()
            with open('products.json', 'w') as f:
                json.dump(data, f)
            print("Los datos se han descargado del servidor y almacenado en el archivo JSON.")
        else:
            print("El archivo JSON contiene información.")
except FileNotFoundError:
    # Si el archivo no existe, descargar los datos del servidor
    print("El archivo JSON no existe. Descargando datos...")
    response = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/e20c412e7e1dcc3b089b0594b5a42f30ac15e49b/products.json')
    data = response.json()
    with open('products.json', 'w') as f:
        json.dump(data, f)
    print("Los datos se han descargado del servidor y almacenado en el archivo JSON.")

Almacen = []


#print objetos
for obj in data:
    name = obj['name']
    description = obj['description']
    price = obj['price']
    category = obj['category']
    description = obj['description']
    item = Producto(name, description, price, category)
    Almacen.append(item)

def goj():
    with open('products.json', 'w') as f:
        json.dump([item.__dict__ for item in Almacen], f)

    

#Buscador por nombre
def BMGPN(): 
 
    search_term = input("¿Qué objeto estás buscando? \n>>> ")
    results = [obj for obj in Almacen if search_term.lower() in obj.name.lower()]
    if len(results) == 0:
        print(f"\n No se encontraron resultados para '{search_term}'.")
    else:
        print(f"\n Se encontraron {len(results)} resultados para '{search_term}': \n")
        for result in results:
            print(f"Nombre: {result.name}")
            print(f"Descripción: {result.description}")
            print(f"Precio: {result.price}")
            print(f"Categoría: {result.category}")
            print()

#Buscador por categoria error
def BMGPC():
    with open("products.json", "r") as f:
        data = json.load(f)
    
    categoria = input("Ingrese la categoria que desea buscar \n>>>")

    resultados = [producto for producto in data if producto["category"].lower() == categoria.lower()]

    if len(resultados) == 0:
        print(f"\n No se encontraron resultados para la categoría '{categoria}'.")
    else:
        print(f"\n Se encontraron {len(resultados)} resultados para la categoría '{categoria}': \n")
        for resultado in resultados:
            print(f"Nombre: {resultado['name']}")
            print(f"Descripción: {resultado['description']}")
            print(f"Precio: {resultado['price']}")
            print(f"Categoría: {resultado['category']}")
            print()

#Buscador por descripcion
def BMGPD(): 

    search_term = input("¿Qué objeto estás buscando? \n>>> ")
    results = [obj for obj in Almacen if search_term.lower() in obj.description.lower()]

    if len(results) == 0:
        print(f"\n No se encontraron resultados para '{search_term}'.")
    else:
        print(f"\n Se encontraron {len(results)} resultados para '{search_term}': \n")
        for result in results:
            print(f"Nombre: {result.name}")
            print(f"Descripción: {result.description}")
            print(f"Precio: {result.price}")
            print(f"Categoría: {result.category}")
            print()

#Buscador por precio error

#eliminar objeto
def EMGPN():
    nombre_producto = input("Introduce el nombre del producto que desea eliminar para confirmar: ").lower()
    for producto in Almacen:
        if producto.name.lower() == nombre_producto:
            Almacen.remove(producto)
            print(f"El producto '{producto.name}' ha sido eliminado.")
            return
    print(f"No se encontró el producto '{nombre_producto.capitalize()}'.")

def EMGPC():
    nombre_producto = input("Introduce el nombre de la categoria que desea eliminar para confirmar: ").lower()
    for producto in Almacen:
        if producto.category.lower() == nombre_producto:
            Almacen.remove(producto)
            print(f"El producto '{producto.category}' ha sido eliminado.")
            return
    print(f"No se encontró el producto '{nombre_producto.capitalize()}'.")

def EMGPD():
    nombre_producto = input("Introduce el nombre de la categoria que desea eliminar para confirmar: ").lower()
    for producto in Almacen:
        if producto.description.lower() == nombre_producto:
            Almacen.remove(producto)
            print(f"El producto '{producto.description}' ha sido eliminado.")
            return
    print(f"No se encontró el producto '{nombre_producto.capitalize()}'.")

#agg objeto
def NCAP():
    name = input("Introduce el nombre del producto: ")
    price = float(input("Introduce el precio del producto: "))
    category = input("Introduce la categoría del producto: ")
    description = input("Introduce la descripción del producto: ")

    for producto in Almacen:
        if producto.name == name:
            print(f"El producto '{name}' ya existe en la lista 'Almacen'.")
            return

    item = Producto(name, price, category, description)
    Almacen.append(item)
    print(f"El producto '{name}' ha sido agregado a la lista 'Almacen'.")

def BMGPP():
# Solicitamos el precio que el usuario desea buscar
    precio = float(input("Ingrese el precio que desea buscar: "))
    
    # Buscamos los productos que tengan el precio especificado
    resultados = []
    for producto in Almacen:
        if producto.price == precio:
            resultados.append(producto)
    
    # Si no se encontraron resultados, mostramos un mensaje
    if len(resultados) == 0:
        print(f"No se encontraron resultados para el precio '{precio}'.")
    
    # Si se encontraron resultados, los imprimimos
    else:
        print(f"Se encontraron {len(resultados)} resultados para el precio '{precio}':")
        for resultado in resultados:
            print(f"Nombre: {resultado.nombre}")
            print(f"Categoría: {resultado.categoria}")
            print(f"Descripción: {resultado.descripcion}")
            print(f"Precio: {resultado.precio}")
            print()
                    
#edit productos
def EDTMGP():
    name = input("Introduce el nombre del producto que deseas editar para confirmar: ")
    for producto in Almacen:
        if producto.name == name:
            print(f"Producto encontrado: {producto}")
            print("Introduce los nuevos detalles del producto: ")
            producto.name = input(f"Nuevo nombre ({producto.name}): ") or producto.name
            producto.price = float(input(f"Nuevo precio ({producto.price}): ")) or producto.price
            producto.category = input(f"Nueva categoría ({producto.category}): ") or producto.category
            producto.description = input(f"Nueva descripción ({producto.description}): ") or producto.description
            print(f"El producto '{name}' ha sido actualizado.")
            return
        else:
            print(f"No se ha encontrado un producto con el nombre '{name}'.")

#Menu cierre de menus
def cierre_mgp():
    while True:
        cmgp = int(input('1 - volver a menu inicial \n2 - volver al menu de gestion de productos \n3 - cerrar \n>>>'))
        if cmgp == 1:
          pass
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

#Menu de este modulo
def MGP():
    
    while True:
        menu_1mgp = int(input ('1 - Nueva Carga \n2 - Almacen/Lista de productos \n3 - Mostrar productos \n4 - menu de cierre \n >>>'))
        if menu_1mgp == 1:
                # bucle nueva carga         
                        NCAP()
                        goj()
                        cierre_mgp()
                        pass
        
        elif menu_1mgp == 2:
             
            bus_2mgp = int(input('1 - Buscar por nombre \n 2 - Buscar por precio \n 3 - Busacar por categoria \n 4 - Buscar por descripcion \n 5 - cerrar \n>>>'))

            if bus_2mgp == 1:
                 
                BMGPN()
                bus_3mgp = []
                while True:
                    bus_3mgp = int(input('1 - eliminar producto \n2 - editar producto \n3 - menu de cierre'))
                    if bus_3mgp == 1:
                        EMGPN()
                        goj()
                        cierre_mgp()
                        break
                    elif bus_3mgp == 2:
                        EDTMGP()
                        goj()
                        cierre_mgp()
                        break
                    elif bus_3mgp == 3:
                        cierre_mgp
                        break
                    else:
                        print ('opcion del menu no seleccionado')

            elif bus_2mgp == 2:
                #busqueda por precio
                BMGPP()
                bus_3mgp = []
                while True:
                    bus_3mgp = int(input('1 - eliminar producto \n2 - editar producto \n3 - menu de cierre'))
                    if bus_3mgp == 1:
                        EMGPD()
                        goj()
                        cierre_mgp()
                        break
                    elif bus_3mgp == 2:
                        EDTMGP()
                        goj()
                        cierre_mgp()
                        break
                    elif bus_3mgp == 3:
                        cierre_mgp
                        break
                    else:
                        print ('opcion del menu no seleccionado')

                cierre_mgp()
                pass

            elif bus_2mgp == 3:
                 
                BMGPC()
                bus_3mgp = []
                while True:
                    bus_3mgp = int(input('1 - eliminar producto \n2 - editar producto \n3 - menu de cierre'))
                    if bus_3mgp == 1:
                        EMGPC()
                        goj()
                        cierre_mgp()
                        break
                    elif bus_3mgp == 2:
                        EDTMGP()
                        goj()
                        cierre_mgp()
                        break
                    elif bus_3mgp == 3:
                        cierre_mgp
                        break
                    else:
                        print ('opcion del menu no seleccionado')

            elif bus_2mgp == 4:
                 
                BMGPD()
                bus_3mgp = []
                while True:
                    bus_3mgp = int(input('1 - eliminar producto \n2 - editar producto \n3 - menu de cierre'))
                    if bus_3mgp == 1:
                        EMGPD()
                        goj()
                        cierre_mgp()
                        break
                    elif bus_3mgp == 2:
                        EDTMGP()
                        goj()
                        cierre_mgp()
                        break
                    elif bus_3mgp == 3:
                        cierre_mgp
                        break
                    else:
                        print ('opcion del menu no seleccionado')


            elif bus_2mgp == 5:
                cierre_mgp()
                pass

        elif menu_1mgp == 4:
            cierre_mgp()
            break
                    
        else:
                print ('opcion del menu no seleccionado')

    

