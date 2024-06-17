from os import system

dic_trabajadores = {}

def menu_principal():
    opciones = {
        '1': ('Registrar Trabajador', registrar),
        '2': ('Listar Todos los Trabajadores', listar),
        '3': ('Imprimir Planilla de Sueldos', sueldos),
        '4': ('Salir del Programa', salir)
    }

    generar_menu(opciones, '4')

def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        system("cls")
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print() # se imprime una línea en blanco para clarificar la salida por pantalla

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def registrar():
    print("Bienvenid@")
    print("Por favor Escriba su Nombre y Apellido:")
    nom = input()
    print("Por favor Escriba su Cargo:")
    cargo = input()
    print("Por favor Escriba su Sueldo Bruto:")
    valido = True
    while valido == True:
        sueldo = input()
        try:
            sueldo = int(sueldo)
            valido = False
        except ValueError:
            print("Ingrese sueldo válido")
    des_salud = (sueldo/100)*7
    des_afp = (sueldo/100)*12
    liquido = (sueldo - des_salud) - des_afp
    dic_trabajadores[len(dic_trabajadores)+1] = {'Nombre': nom,'Cargo': cargo,'Sueldo Bruto': str(sueldo), 'Desc. Salud': str(des_salud), 'Desc. AFP':str(des_afp),'Líquido a pagar': str(liquido)}
    

def listar():
    print("Bienvenid@")
    print("Se muestra a continuación todos los trabajadores:")
    print("  Nombre |   Cargo  | Sueldo Bruto |  Des. Salud | Desc. AFP | Líquido a Pagar")
    for clave,valor in dic_trabajadores.items():
        linea = ""
        for clave2, valor2 in valor.items():
            linea += valor2 + ' | '
        print(linea)
    input("Presione Enter para Volver al Menú")

def sueldos():
    print('Has elegido la opción 3')


def salir():
    print('Saliendo')


menu_principal()