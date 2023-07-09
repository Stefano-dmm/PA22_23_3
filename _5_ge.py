import json
import time

class Envio:
    def __init__(self, cliente, fecha):
        self.cliente = cliente
        self.fecha = fecha

# Leer
with open('envios.json', 'r') as f:
    envios_json = json.load(f)

# Crea un objeto
envios = []
for envio_json in envios_json:
    envio = Envio(envio_json["cliente"], envio_json["fecha"])
    envios.append(envio)

def agge(envios):
    cliente = input("Cliente: ")
    fecha = input("Fecha: ")
    nuevo_envio = Envio(cliente, fecha)
    # Agg
    envios.append(nuevo_envio)
    print("Envío agregado con éxito a la lista de envíos.")


def buscador(envios):

    search_term = input("¿Qué envío estás buscando? (Ingresa cualquier dato del envío)\n>>> ")
    # Buscar
    envios_encontrados = []
    for envio in envios:
        if search_term.lower() in envio.cliente.lower():
            envios_encontrados.append(envio)
        elif search_term.lower() in envio.fecha.lower():
            envios_encontrados.append(envio)

    # Imprimir
    if len(envios_encontrados) == 0:
        print(f"No se encontraron resultados para '{search_term}'.")
    else:
        print(f"Se encontraron {len(envios_encontrados)} resultados para '{search_term}':\n")
        for envio in envios_encontrados:
            print(f"Cliente: {envio.cliente}")
            print(f"Fecha: {envio.fecha}")
            print()

def cierre_mge():
    
        cmge = int(input('1 - volver a menu inicial \n2 - volver al menu de gestion de envios \n3 - cerrar \n>>>'))
        if cmge == 1:
           #lo se, poco profesional, pero sirve y es la manera que encontre para que no me de errores
           pass
        elif cmge == 2:
            MGE()
        elif cmge == 3:
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
            cierre_mge()


def MGE():
    
    while True:
        menu_1mge = int(input ('1 - Registrar envio \n2 - Busqueda de envio \n3 - menu de cierre \n >>>'))
        if menu_1mge == 1:
            # print el registro  
            agge(envios)       
            cierre_mge()
            break
        elif menu_1mge == 2:
            #buscador de ventas
            buscador(envios)
            cierre_mge()
            break
        elif menu_1mge == 3:
            cierre_mge()
            break
                    
        else:
                print ('opcion del menu no seleccionado')

        break
    