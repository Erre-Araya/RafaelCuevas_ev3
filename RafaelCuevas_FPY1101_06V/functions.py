import os, time
import random as rd
from datetime import datetime

ciudadanos = []

def limpiar_pantalla():
    os.system("cls")

def menu_principal():
    limpiar_pantalla()
    print("***MENÚ PRINCIPAL***")
    print("1. Registrar ciudadano")
    print("2. Buscar ciudadano")
    print("3. Imprimir certificado")
    print("4. Salir")

def obtener_nombre():
    nombre = input("Ingrese nombre (8 caracteres mínimo): ")
    while len(nombre) < 8 or nombre == "        ":
        nombre = input("ERROR: campo necesita mínimo 8 caracteres.\nIngrese nombre (8 caracteres mínimo): ")
    return nombre

def obtener_nacionalidad():
    nacionalidad = input("Ingrese nacionalidad: ")
    while len(nacionalidad) < 1:
        nacionalidad = input("ERROR: campo no puede venir vacío.\nIngrese nacionalidad: ")
    return nacionalidad

def obtener_edad():
    while True:
        edadS = input("Ingrese edad (mínimo 15 años): ")
        while len(edadS) < 2:
            edadS = input("ERROR: campo no puede venir vacío.\nIngrese edad (mínimo 15 años): ")
        try:
            edad = int(edadS)
            while edad < 15 or edad > 120:
                edad = int(input("ERROR: edad fuera de rango (15 a 120).\nIngrese edad: "))
            return edad
        except:
            print("ERROR: campo no acepta caracteres.")

def obtener_nif(contador_nifs):
    while True:
        print("¿Cuál es su ciudad de residencia?\n1. Barcelona\n2. Madrid\n3. Sevilla")
        try:
            ciudad = int(input("Señale una opción válida (1-3): "))
            if ciudad == 1:
                codigo_ciudad = "BAR"
            elif ciudad == 2:
                codigo_ciudad = "MAD"
            elif ciudad == 3:
                codigo_ciudad = "SEV"
            else:
                print("ERROR: opción fuera de rango.")
                time.sleep(1)
                continue
            nif_final = "0000000" + str(contador_nifs) + "-" + codigo_ciudad
            return nif_final
        except:
            print("ERROR: no se aceptan caracteres.")
            time.sleep(1)
            continue

def grabar_datos():
    contador_nifs = 1
    while True:
        limpiar_pantalla()
        print("Registrar ciudadano")
        nombre = obtener_nombre()
        nacionalidad = obtener_nacionalidad()
        edad = obtener_edad()
        nif = obtener_nif(contador_nifs)
        contador_nifs += 1
        ciudadano = [nombre, nacionalidad, edad, nif]
        ciudadanos.append(ciudadano)
        agregar = int(input("¿Desea agregar otro/a ciudadano?\n1. Sí\n2. No\nIngrese una opción válida (1-2): "))
        if agregar == 1:
            continue
        elif agregar == 2:
            break
        else:
            print("ERROR: opción fuera de rango. Detención automática.")
            break
    for c in ciudadanos:
        print(c)
    input("Presione alguna tecla para continuar.")
    crear_datos_certificado()

def buscar_persona():
    if len(ciudadanos) < 1:
        limpiar_pantalla()
        print("No se encuentran registros en la base de datos.")
        time.sleep(2)
    else:
        limpiar_pantalla()
        print("Buscar ciudadano")
        nif_buscar = input("Ingrese NIF correspondiente: ").upper()
        encontrado = False
        for ciudadano in ciudadanos:
            if ciudadano[3] == nif_buscar:
                encontrado = True
                print(f"NOMBRE: {ciudadano[0]}")
                print(f"NACIONALIDAD: {ciudadano[1]}")
                print(f"EDAD: {ciudadano[2]}")
                print(f"NIF: {ciudadano[3]}")
                input("Presione alguna tecla para continuar.")
        if not encontrado:
            print("ERROR: NIF no se encuentra en la base de datos.")
            time.sleep(2)

def crear_datos_certificado():
    for ciudadano in ciudadanos:
        registro = {}
        nacimiento = fecha_aleatoria()
        registro["Nacimiento"] = nacimiento
        estados = ["Soltero/a", "Casado/a", "Viudo/a", "Separado/a", "Divorciado/a"]
        estado_conyugal = rd.choice(estados)
        registro["Estado"] = estado_conyugal
        salario_mensual = rd.randint(1000, 3000)
        registro["Salario"] = salario_mensual
        ciudadano.append(registro)


def fecha_aleatoria():
    dia = rd.randint(1, 31)
    mes = rd.randint(1, 12)
    if mes == 2:
        if dia > 28:
            dia = 28
        if mes == 4 or mes == 6 or mes == 8 or mes == 11:
            if dia == 31:
                dia = 30
    fecha_nac = str(dia) + "/" + str(mes) + "/"
    return fecha_nac

def certificado_nacimiento():
    limpiar_pantalla()
    print("CERTIFICADO DE NACIMIENTO")
    nif_buscar = input("Ingrese NIF correspondiente: ").upper()
    encontrado = False
    for ciudadano in ciudadanos:
        if ciudadano[3] == nif_buscar:
            encontrado = True
            limpiar_pantalla()
            print("-----------------CERTIFICADO DE NACIMIENTO-----------------")
            print("El siguiente certificado viene a indicar que el ciudadano respectivo\ntiene la siguiente fecha de nacimiento: ", (ciudadano[4]["Nacimiento"]),(2024 - ciudadano[2]))
            print("\tDatos del solicitante: ")
            print(f"\tNOMBRE: {ciudadano[0]}")
            print(f"\tNACIONALIDAD: {ciudadano[1]}")
            print(f"\tEDAD: {ciudadano[2]}")
            print(f"\tNIF: {ciudadano[3]}")
            print(f"El siguiente certificado se otorga para los fines que estime conveniente.")
            print("---------------------------------------------------------------------")
            input("Presione alguna tecla para continuar.")
    if not encontrado:
        print("ERROR: NIF no se encuentra en la base de datos.")
        time.sleep(2)

def certificado_conyugal():
    limpiar_pantalla()
    print("CERTIFICADO DE ESTADO CONYUGAL")
    nif_buscar = input("Ingrese NIF correspondiente: ").upper()
    encontrado = False
    for ciudadano in ciudadanos:
        if ciudadano[3] == nif_buscar:
            encontrado = True
            limpiar_pantalla()
            print("-----------------CERTIFICADO DE ESTADO CONYUGAL-----------------")
            print(f"El siguiente certificado viene a indicar que el ciudadano respectivo\nmantiene un estado conyugal {ciudadano[4]["Estado"]}.")
            print("\tDatos del solicitante: ")
            print(f"\tNOMBRE: {ciudadano[0]}")
            print(f"\tNACIONALIDAD: {ciudadano[1]}")
            print(f"\tEDAD: {ciudadano[2]}")
            print(f"\tNIF: {ciudadano[3]}")
            print(f"El siguiente certificado se otorga para los fines que estime conveniente.")
            print("---------------------------------------------------------------------")
            input("Presione alguna tecla para continuar.")
    if not encontrado:
        print("ERROR: NIF no se encuentra en la base de datos.")
        time.sleep(2)

def certificado_salario():
    limpiar_pantalla()
    print("CERTIFICADO DE SALARIO MENSUAL")
    nif_buscar = input("Ingrese NIF correspondiente: ").upper()
    encontrado = False
    for ciudadano in ciudadanos:
        if ciudadano[3] == nif_buscar:
            encontrado = True
            limpiar_pantalla()
            print("---------------CERTIFICADO DE SALARIO MENSUAL---------------")
            print(f"El siguiente certificado viene a indicar que el ciudadano respectivo\npercibe un salario mensual de {ciudadano[4]["Salario"]} euros.")
            print("\tDatos del solicitante: ")
            print(f"\tNOMBRE: {ciudadano[0]}")
            print(f"\tNACIONALIDAD: {ciudadano[1]}")
            print(f"\tEDAD: {ciudadano[2]}")
            print(f"\tNIF: {ciudadano[3]}")
            print(f"El siguiente certificado se otorga para los fines que estime conveniente.")
            print("---------------------------------------------------------------------")
            input("Presione alguna tecla para continuar.")
    if not encontrado:
        print("ERROR: NIF no se encuentra en la base de datos.")
        time.sleep(2)

def imprimir_certificado():
    if len(ciudadanos) < 1:
        limpiar_pantalla()
        print("No se encuentran registros en la base de datos.")
        time.sleep(2)
    else:
        while True:
            limpiar_pantalla()
            print("Imprimir certificado")
            print("1. Certificado de nacimiento")
            print("2. Certificado de estado conyugal")
            print("3. Certificado de salario mensual")
            print("4. Volver al menú principal")
            try:
                opc2 = int(input("Ingrese una opción válida (1-4): "))
                if opc2 == 1:
                    certificado_nacimiento()
                elif opc2 == 2:
                    certificado_conyugal()
                elif opc2 == 3:
                    certificado_salario()
                elif opc2 == 4:
                    print("Volviendo...")
                    time.sleep(1)
                    break
                else:
                    print("ERROR: opción fuera de rango.")
                    time.sleep(2)
            except:
                print("ERROR: opción inválida. Sólo se aceptan números.")
                time.sleep(2)

def salir():
    limpiar_pantalla()
    print("Saliendo del programa...\nRafael Cuevas Araya - versión 1.0")
    input("Presione cualquier tecla.")