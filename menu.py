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
    cargo = ''
    while cargo != 'CEO' and cargo != 'ANALISTA DE DATOS' and cargo != "DESARROLLADOR":
        cargo = input().upper()
        if cargo != 'CEO' and cargo != 'ANALISTA DE DATOS' and cargo != "DESARROLLADOR":
            print("Ingrese cargo válido")
    print("Por favor Escriba su Sueldo Bruto:")
    valido = True
    while valido == True:
        sueldo = input()
        try:
            sueldo = int(sueldo)
            valido = False
        except ValueError:
            print("Ingrese sueldo válido")
    des_salud = round((sueldo/100)*7)
    des_afp = round((sueldo/100)*12)
    liquido = (sueldo - des_salud) - des_afp
    dic_trabajadores[len(dic_trabajadores)+1] = {'Nombre': nom,'Cargo': cargo,'Sueldo Bruto': str(sueldo), 'Desc. Salud': str(des_salud), 'Desc. AFP':str(des_afp),'Líquido a pagar': str(liquido)}
    

def listar():
    print("Bienvenid@")
    print("Se muestra a continuación todos los trabajadores:")
    print("     Nombre     |   Cargo  | Sueldo Bruto |  Des. Salud | Desc. AFP | Líquido a Pagar")
    for clave,valor in dic_trabajadores.items():
        linea = ""
        for clave2, valor2 in valor.items():
            linea += valor2 + ' | '
        print(linea)
    input("Presione Enter para Volver al Menú")

def sueldos():
    with open(r'C:\Users\cetecom\Downloads\salida.txt','w',newline="") as f:
        f.write(f'Nombre\t       Cargo\t   Sueldo_Bruto\t   Desc. Salud\t  Desc.AFP\t  Liquido a pagar\t\n')
        for clave,valor in dic_trabajadores.items():
            for clave2,valor2 in valor.items():
                f.write(valor2 + '  |  ')
            f.write('\n')

def salir():
    print('Saliendo')


menu_principal()