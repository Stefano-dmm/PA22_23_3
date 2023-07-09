import json
import requests
import time
import _1_gp as _1_gp
import _2_gv as _2_gv
import _3_gc as _3_gc
import _4_gp as _4_gp
import _5_ge as _5_ge
import _6_e as _6_e


while True:
    inp_menu_inicial = int(input("BIENVENIDO AL SISTEMA DE GESTION DE TIENDA DE PRODUCTOS NATURALES \n POR FAVOR INSERTE EL VALOR DEL MENU AL QUE DESEE ACCEDER \n  1 - Gestion de Productos \n  2 - Gestion de Ventas \n  3 - Gestion de Clientes \n  4 - Gestion de Pagos \n  5 - Gestion de Envios  \n  6 - Estadisticas \n  7 - Cerrar \n   >>>"))
    if inp_menu_inicial == 1:
        _1_gp.MGP()
        break

    elif inp_menu_inicial == 2:
        _2_gv.MGV()
        pass

    elif inp_menu_inicial == 3:
        _3_gc.MGC()
        pass

    elif inp_menu_inicial == 4:
        _4_gp.MGP()
        pass

    elif inp_menu_inicial == 5:
        _5_ge.MGE()
        pass

    elif inp_menu_inicial == 6:
       _6_e.menu6()

    elif inp_menu_inicial == 7:
        print("Cerrando programa")
        for i in range(5):
            time.sleep(0.5)
            print(".", end="", flush=True)

        texto = "Adios"
        for i in range(10):
            time.sleep(0.1)
            print("\r" + " " * i + texto, end="", flush=True)
        exit()
    
    else:
        print ('opcion del menu no seleccionado') 

    






