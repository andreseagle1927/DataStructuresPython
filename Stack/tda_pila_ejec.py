
from tda_pila import Pila, apilar, desapilar, pila_vacia, tamano, en_cima, barrido

pdatos = Pila()
ppar = Pila()
pimpar = Pila()
dato = int(input("ingrese un numero - 0 para salir: "))

while(dato != 0):
    apilar(pdatos, dato)
    dato = int(input("ingrese un numero - 0 para salir: "))

tamanopila = tamano(pdatos)

print("tamaño de la pila: "+str(tamanopila))

cimapila = en_cima(pdatos)
print("valor en cima de la pila: "+str(cimapila))

barridopila = barrido(pdatos)

while(not pila_vacia(pdatos)):
    dato = desapilar(pdatos)
    if(dato % 2 == 0):
        apilar(ppar , dato)
    else:
        apilar(pimpar, dato)
    
print("pila impar: ")

while(not pila_vacia(ppar)):
    dato = desapilar(ppar)
    print(dato)

print("pila impar: ")

while(not pila_vacia(pimpar)):
    dato = desapilar(pimpar)
    print(dato)
