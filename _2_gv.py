import json

# Cargar los datos del archivo JSON
with open('ventas.json', 'r') as f:
    data = json.load(f)

class Venta:
    def __init__(self, cliente, fecha, monto):
        self.cliente = cliente
        self.fecha = fecha
        self.monto = monto

# Convertir los objetos del archivo JSON en objetos Venta
ventas = []
for obj in data:
    venta = Venta(obj['cliente'], 
                  obj['fecha'], 
                  obj['monto'])
    ventas.append(venta)


def generar_factura():
   # Inicializar variables para el total de ventas y el total con impuestos
    total_ventas = 0
    total_con_impuestos = 0

    # Iterar sobre los objetos del archivo JSON y sumar los montos de las ventas
    for obj in data:
        total_ventas += obj['monto']

    # Calcular el total con impuestos
    total_con_impuestos = total_ventas * 1.1

    # Definir la cantidad de decimales a mostrar
    decimales = 2

    # Generar la factura
    print("FACTURA DE VENTAS")
    print("=================")
    for obj in data:
        print(f"{obj['cliente']} - Fecha: {obj['fecha']} - Monto: ${obj['monto']:.{decimales}f}")
    print(f"Total sin impuestos: ${total_ventas:.{decimales}f}")
    print(f"Total con impuestos: ${total_con_impuestos:.{decimales}f}")    

#buscadores

#por cliente
def BGVC():
    search_term = input("¿Qué cliente estás buscando? \n>>> ")
    results = [venta for venta in ventas if search_term.lower() in venta.cliente.lower()]
    if len(results) == 0:
        print(f"\n No se encontraron resultados para '{search_term}'.")
    else:
        print(f"\n Se encontraron {len(results)} resultados para '{search_term}': \n")
        for result in results:
            print(f"Cliente: {result.cliente}")
            print(f"Fecha de venta: {result.fecha}")
            print(f"Monto de venta: {result.monto}")
            print()

#por monto error
def BGVM(monto_minimo, monto_maximo):
    monto_minimo = int(input("Ingrese el monto mínimo: "))
    monto_maximo = int(input("Ingrese el monto máximo: "))
    # Filtrar las ventas por monto
    results = filter(lambda venta: monto_minimo <= venta.monto <= monto_maximo, ventas)
    results = list(results)
    if len(results) == 0:
        print(f"\n No se encontraron resultados para montos entre {monto_minimo} y {monto_maximo}.")
    else:
        print(f"\n Se encontraron {len(results)} resultados para montos entre {monto_minimo} y {monto_maximo}: \n")
        for result in results:
            print(f"Cliente: {result.cliente}")
            print(f"Fecha de venta: {result.fecha}")
            print(f"Monto de venta: {result.monto}")
            print()
#por fecha
def BGVF(fecha_inicio, fecha_fin):
    # Filtrar las ventas por fecha
    results = [venta for venta in ventas if fecha_inicio <= venta.fecha <= fecha_fin]
    if len(results) == 0:
        print(f"\n No se encontraron resultados para ventas entre {fecha_inicio} y {fecha_fin}.")
    else:
        print(f"\n Se encontraron {len(results)} resultados para ventas entre {fecha_inicio} y {fecha_fin}: \n")
        for result in results:
            print(f"Cliente: {result.cliente}")
            print(f"Fecha de venta: {result.fecha}")
            print(f"Monto de venta: {result.monto}")
            print()

def cierre_mgv():
    
        cmgv = int(input('1 - volver a menu inicial \n2 - volver al menu de gestion de ventas \n3 - cerrar \n>>>'))
        if cmgv == 1:
           #lo se, poco profesional, pero sirve y es la manera que encontre para que no me de errores
           print
        elif cmgv == 2:
            MGV()
        elif cmgv == 3:
            print('adios')
        else:
            print ('opcion del menu no seleccionado') 
            cierre_mgv()


def MGV():
    
    while True:
        menu_1mgv = int(input ('1 - Registro de venta \n2 - Busqueda de venta \n3 - menu de cierre \n >>>'))
        if menu_1mgv == 1:
            generar_factura()
            # print el registro  
            cierre_mgv()
            break
        elif menu_1mgv == 2:
            #buscador de ventas
            m_2mgv = int(input ('1 - Buscar por cliente \n 2 - Buscar por monto \n 3 - Buscar por fecha \n4 - menu de cierre'))
            if m_2mgv == 1:
                BGVC()
                cierre_mgv()
                break

            elif m_2mgv == 2:
                BGVM()
                cierre_mgv()
                break

            elif m_2mgv == 3:
                BGVF()
                cierre_mgv()
                break

            elif m_2mgv == 4:
                cierre_mgv()
                break
            else:
                print ('opcion del menu no seleccionado')
            
            cierre_mgv()
            break
        elif menu_1mgv == 3:
            cierre_mgv()
            break
                    
        else:
            print ('opcion del menu no seleccionado')

        break
    