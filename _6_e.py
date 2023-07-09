import json
import time

class Venta:
    def __init__(self, cliente, fecha, monto, productos=None):
        self.cliente = cliente
        self.fecha = fecha
        self.monto = monto
        self.productos = productos or []

# Leer
with open('ventas.json', 'r') as f:
    ventas_json = json.load(f)
    
#pagos

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
    
#envios
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
    
    
    # Obtener la fecha actual
fecha_actual = time.localtime()

    
def menu6():
    while True:

        opcion = input("1. Generar informes de ventas \n2. Generar informes de pagos \n3. Generar informes de envíos \n4. Salir \n>>>")

        if opcion == "1":
            menu2 =[]
            menu2 = int(input('1 - Venta de productos \n2 - productos mas vendidos \n3 - Clientes mas frecuentes \n4 - cerrar'))
            if menu2 == 1:
                
                # Generar informes de ventas
                # Inicializar variables para ventas totales
                ventas_totales_dia = 0
                ventas_totales_semana = 0
                ventas_totales_mes = 0
                ventas_totales_anio = 0

                # Calcular ventas totales por día, semana, mes y año
                for venta in ventas_json:
                    fecha_venta = time.strptime(venta['fecha'], '%Y-%m-%d')
                    monto_venta = venta['monto']

                    # Sumar venta al total del día
                    if fecha_actual.tm_year == fecha_venta.tm_year and fecha_actual.tm_yday == fecha_venta.tm_yday:
                        ventas_totales_dia += monto_venta

                    # Sumar venta al total de la semana
                    semana_actual = time.strftime('%U', fecha_actual)
                    semana_venta = time.strftime('%U', fecha_venta)
                    if fecha_actual.tm_year == fecha_venta.tm_year and semana_actual == semana_venta:
                        ventas_totales_semana += monto_venta

                    # Sumar venta al total del mes
                    if fecha_actual.tm_year == fecha_venta.tm_year and fecha_actual.tm_mon == fecha_venta.tm_mon:
                        ventas_totales_mes += monto_venta

                    # Sumar venta al total del año
                    if fecha_actual.tm_year == fecha_venta.tm_year:
                        ventas_totales_anio += monto_venta

                # Imprimir ventas totales
                print(f"Ventas totales del día: {ventas_totales_dia}")
                print(f"Ventas totales de la semana: {ventas_totales_semana}")
                print(f"Ventas totales del mes: {ventas_totales_mes}")
                print(f"Ventas totales del año: {ventas_totales_anio}")
                
            elif menu2 == 2:
                # Crear un diccionario para contar las ventas de cada producto
                    ventas_por_producto = {}

                    for venta in ventas:
                            for producto in venta['productos']:
                                if producto in ventas_por_producto:
                                    ventas_por_producto[producto] += venta['monto']
                                else:
                                    ventas_por_producto[producto] = venta['monto']

                        # Ordenar los productos por ventas de mayor a menor
                    productos_mas_vendidos = sorted(ventas_por_producto.items(), key=lambda x: x[1], reverse=True)

                        # Imprimir los 3 productos más vendidos
                    print("Los productos más vendidos son:")
                    for producto, ventas in productos_mas_vendidos[:3]:
                            print(f"- {producto}: {ventas}")
                            
            elif menu2 == 3:

                ventas_por_cliente = {}

                for venta in ventas:
                    cliente = venta['cliente']
                    if cliente in ventas_por_cliente:
                        ventas_por_cliente[cliente] += 1
                    else:
                        ventas_por_cliente[cliente] = 1

                # Ordenar los clientes por frecuencia de mayor a menor
                clientes_mas_frecuentes = sorted(ventas_por_cliente.items(), key=lambda x: x[1], reverse=True)

                # Imprimir los 3 clientes más frecuentes
                print("Los clientes más frecuentes son:")
                for cliente, frecuencia in clientes_mas_frecuentes[:3]:
                    print(f"- {cliente}: {frecuencia} compras")
                
            elif menu2 == 4:
                # Salir del programa
                print("Saliendo del programa...")
                break
            
            else:
                print("Opción inválida, intente de nuevo")
        
        elif opcion == "2":
           
           menu2 =[]
           menu2 = int(input('1 - Pagos totales \n2 - Cliente con pagos pendientes \n3 - cerrar'))
           if menu2 == 1:
               
               pago_total = sum(venta['monto'] for venta in ventas)
               print(f"El pago total de todas las ventas es: {pago_total}")
               
           elif menu2 == 2:
               
               clientes_con_pagos_pendientes = set()
               for venta in ventas:
                    if not venta['pago_recibido']:
                        clientes_con_pagos_pendientes.add(venta['cliente'])
                        print("Los clientes con pagos pendientes son:")
                    for cliente in clientes_con_pagos_pendientes:
                        print(f"- {cliente}")
               
           elif menu2 == 3:
               print("Saliendo del programa...")
               break
           else:
               print("Opción inválida, intente de nuevo")
        
        elif opcion == "3":
            menu2 =[]
            menu2 = int(input('1 - Envios totales \n2 - Productos mas enviados \n3 - \n4 - cerrar'))
            if menu2 == 1:
                envios_por_dia = {}
                envios_por_semana = {}
                envios_por_mes = {}
                envios_por_ano = {}

                for envio in envios:
                    fecha_envio = time.strptime(envio['fecha'], "%Y-%m-%d %H:%M:%S")

                    # Envíos por día
                    fecha_dia = time.strftime("%Y-%m-%d", fecha_envio)
                    if fecha_dia not in envios_por_dia:
                        envios_por_dia[fecha_dia] = 0
                    envios_por_dia[fecha_dia] += 1

                    # Envíos por semana
                    num_semana = time.strftime("%U", fecha_envio)
                    fecha_semana = f"{fecha_envio.tm_year}-Semana{num_semana}"
                    if fecha_semana not in envios_por_semana:
                        envios_por_semana[fecha_semana] = 0
                    envios_por_semana[fecha_semana] += 1

                    # Envíos por mes
                    fecha_mes = time.strftime("%Y-%m", fecha_envio)
                    if fecha_mes not in envios_por_mes:
                        envios_por_mes[fecha_mes] = 0
                    envios_por_mes[fecha_mes] += 1

                    # Envíos por año
                    fecha_ano = str(fecha_envio.tm_year)
                    if fecha_ano not in envios_por_ano:
                        envios_por_ano[fecha_ano] = 0
                    envios_por_ano[fecha_ano] += 1

                print("Envíos por día:")
                print(envios_por_dia)
                print("Envíos por semana:")
                print(envios_por_semana)
                print("Envíos por mes:")
                print(envios_por_mes)
                print("Envíos por año:")
                print(envios_por_ano)
                print("Informes de envíos generados")
                
            elif menu2 == 2:
                
                productos_mas_enviados = {}

                for envio in envios:
                    for producto in envio['productos']:
                        if producto not in productos_mas_enviados:
                            productos_mas_enviados[producto] = 0
                        productos_mas_enviados[producto] += 1

                productos_mas_enviados = dict(sorted(productos_mas_enviados.items(), key=lambda item: item[1], reverse=True))

                print("Productos más enviados:")
                for producto, cantidad in productos_mas_enviados.items():
                    print(f"{producto}: {cantidad}")
            
            elif menu2 == 3:
                
                
                envios_pendientes_por_cliente = {}

                for envio in envios:
                    if envio['estado'] == 'pendiente':
                        if envio['cliente'] not in envios_pendientes_por_cliente:
                            envios_pendientes_por_cliente[envio['cliente']] = 0
                        envios_pendientes_por_cliente[envio['cliente']] += 1

                if len(envios_pendientes_por_cliente) == 0:
                    print("No hay envíos pendientes.")
                else:
                    cliente_con_envios_pendientes = max(envios_pendientes_por_cliente, key=envios_pendientes_por_cliente.get)
                    print(f"El cliente con envíos pendientes es: {cliente_con_envios_pendientes}")
                
        elif opcion == "4":
            # Salir del programa
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente de nuevo")
            