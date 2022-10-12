from tda_lista import Lista, insertar, tamano, buscar

def crear_tabla(tamano):
    tabla = [None]*tamano
    return tabla

#Esta funcion le resta a la longitud de la tabla los elementos con valor None
def cantidad_elementos(tabla):
    return len(tabla)-tabla.count(None)

#SUMA DE 1 EN 1 TODOS LOS ELEMENTOS DE LA TABLA QUE SEAN DIFERENTES DE NONE
def cantidad_elementos_totales(tabla):
    return sum(tamano(lista) for lista in tabla if lista is not None)

#LONGITUD DE EL DATO SIN ESPACIOS DIVIENDIENDO POR EL TAMAÑO DE LA TABLA Y TOMANDO SU RESIDUO



#FUNCION PARA AGREGAR UN DATO, EN BASE A SU INDICE



# LA FUUNCION UNA TABLA Y UNA DATO TARGET PARA BUSCARLA EN LA TABLA ENTREGADA COMO PARAMETRO

def buscar_tabla(tabla, buscado):
    pos = None
    posicion = funcion_hash(buscado, len(tabla))
    print(tabla[posicion])
    if(tabla[posicion] is not None):
        pos = buscar(tabla[posicion], buscado)
    return pos
