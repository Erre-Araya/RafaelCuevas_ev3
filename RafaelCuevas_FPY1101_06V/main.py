from functions import *

banderaMenu = True

while banderaMenu:
    menu_principal()
    try:
        opc = int(input("Ingrese una opción válida (1-4): "))
        if opc == 1:
            grabar_datos()
        elif opc == 2:
            buscar_persona()
        elif opc == 3:
            imprimir_certificado()
        elif opc == 4:
            salir()
            banderaMenu = False
        else:
            print("ERROR: opción fuera de rango.")
            time.sleep(2)
    except:
        print("ERROR: opción inválida. Sólo se aceptan números.")
        time.sleep(2)
        