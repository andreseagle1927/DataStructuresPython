from cgi import print_arguments
from tda_tabla_hash import crear_tabla, cantidad_elementos, cantidad_elementos_totales, buscar_tabla
from tda_lista import Lista, insertar
from randoms import randomtemperatura

#CREAMOS LA TABLA DE TAMAÑO 9
tabla=crear_tabla(5)

#Para cada indice de la tabla creamos una lista 
for i in range(0,5):
    tabla[i] = Lista()

                    #   [0]
             # [0] -> [pais]

                    
             # [1] -> [latitud, longitud, altitud]

                    #     [2][0]     [2][1]   [2][2]      [2][3]
             # [2] -> [temperatura, presion, humedad, estado del clima]

insertar(tabla[0], ["Argentina",["coorx", "coory", "coorz"],[25, 23, 15, "soleado"]] )
insertar(tabla[1], ["colombia",["coorx", "coory", "coorz"],[38, 15, 24, "soleado"]] )
insertar(tabla[2], ["Francia",["coorx", "coory", "coorz"],[4, 32, 15, "nevado"]] )
insertar(tabla[3], ["UK",["coorx", "coory", "coorz"],[10, 20, 45, "lluvioso"]] )
insertar(tabla[4], ["USA",["coorx", "coory", "coorz"],[18, 18, 30, "nublado"]] )

def imprimirPais(dato):
    
    print("La estacion M "+str(dato + 1)+" esta ubicado en el pais de: "+str(tabla[dato].inicio.info[0])+"")

def imprimirCoordenas(dato):
    print("La estacion M "+str(dato + 1 )+" las coordenas son: "+str(tabla[dato].inicio.info[1])+"")

def imprimirTemperatura(dato):
    print("La estacion M "+str(dato + 1)+" la temperatura es: "+str(tabla[dato].inicio.info[2][0])+"°")

def imprimirPresion(dato):
    print("de estacion M "+str(dato + 1)+" la presion es: "+str(tabla[dato].inicio.info[2][1])+" Pascales")

def imprimirHumedad(dato):
    print("de estacion M "+str(dato + 1)+" la humedad es: "+str(tabla[dato].inicio.info[2][2])+"%")

def imprimirEstClima(dato):
    print("de estacion M "+str(dato + 1)+" el estado del clima es : "+str(tabla[dato].inicio.info[2][3]))


def nueva_hora():
    
    for i in range(0,5):
        numero, presion, humedad, clima = randomtemperatura()
        for j in range(0,4):
            if j == 0:
                tabla[i].inicio.info[2][j] = numero
            if j == 1: 
                tabla[i].inicio.info[2][j] = presion
            if j == 2:
                tabla[i].inicio.info[2][j] = humedad
            if j == 3:
                tabla[i].inicio.info[2][j] = clima

def promedioTemperaturas():
    
    suma_datos = tabla[0].inicio.info[2][0] + tabla[1].inicio.info[2][0] + tabla[2].inicio.info[2][0] + tabla[3].inicio.info[2][0] + tabla[4].inicio.info[2][0]
    num_datos = 5
    promedio = suma_datos / num_datos

    print("El promedio de las temperaturas: "+str(promedio) + " c°")

def promedioHumedad():
    
    suma_datos = tabla[0].inicio.info[2][2] + tabla[1].inicio.info[2][2] + tabla[2].inicio.info[2][2] + tabla[3].inicio.info[2][2] + tabla[4].inicio.info[2][2]
    num_datos = 5
    promedio = suma_datos / num_datos

    print("El promedio de la Humedad: "+str(promedio) + " c°")
        


def menu():
    opcion = None
    opcion  = input(bcolors.Green+"-----SELECCIONE UNA OPCION------- \n 1) Imprimir datos de una estacion \n 2) Mostrar Promedio Temperaturas y humedad \n 3) Imprimir todos los datos de todas las estaciones \n 4) Actualizar Hora \n RESPUESTA = "+bcolors.Green)
    nueva_hora()

    if opcion == "1":
        opcion2 = input("Hay 5 estaciones, digite el numero de la estacion a imprimir ej: (1 o 2 etc...): ")
        if opcion2 >= "1" and opcion2 <= "5":
            imprimirPais(int(opcion2)-1)
            imprimirCoordenas(int(opcion2)-1)
            imprimirTemperatura(int(opcion2)-1)
            imprimirPresion(int(opcion2)-1)
            imprimirHumedad(int(opcion2)-1)
            imprimirEstClima(int(opcion2)-1)

    elif opcion == "2":
        promedioTemperaturas()
        promedioHumedad()

    elif opcion == "3":
        print(bcolors.Yellow+"------- TODOS LOS DATOS--------"+bcolors.Yellow)
        for i in range(0,5):
            print("LOS DATOS DE LA ESTACION "+str(i+1)+" SON:")
            imprimirPais(i)
            imprimirCoordenas(i)
            imprimirTemperatura(i)
            imprimirPresion(i)
            imprimirHumedad(i)
            imprimirEstClima(i)

            print(bcolors.Yellow+"-------------------"+bcolors.Reset)

    elif opcion == "4":
        nueva_hora()
        print("hora y datos actualizada exitosamente")

    else: 
        print("NO SELECCION UNA OPCION VALIDA")

class bcolors:
    Yellow = '\033[93m'
    Cyan = '\033[46m'
    Magenta = '\033[45m'
    White = '\033[30;47m'
    Black = '\033[40m'
    Green = '\033[32m'
    Red = '\033[41m'
    Reset = '\033[0m'  # RESET

while(True):
    menu()