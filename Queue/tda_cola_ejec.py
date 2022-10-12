from operator import le
from traceback import print_tb
from tda_cola import Cola, arribo, atencion, cola_vacia, tamano, en_frente

cdatos = Cola()
cvocales = Cola()

letra = input("ingrese un caracter: ")

while(letra !=""):
    arribo(cdatos, letra)
    letra = input("ingrese un caracter: ")
    

tamanocola = tamano(cdatos)

print("el tamaño de la cola de caratetes: "+str(tamanocola))


frentecola = en_frente(cdatos)
print("valor en frente: "+str(frentecola))

while(not cola_vacia(cdatos)):
    letra = atencion(cdatos)
    if letra.upper() in ["A","E","I","O","U"]:
        arribo(cvocales, letra)

tamanocola = tamano(cvocales)
print("tamaño de la cola de vocales: "+str(tamanocola))
print("vocales")
while(not cola_vacia(cvocales)):
    dato = atencion(cvocales)
    print(dato)