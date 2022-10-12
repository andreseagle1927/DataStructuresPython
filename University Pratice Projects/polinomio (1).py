import colorama


class bcolors:
    Yellow = '\033[103m'
    Cyan = '\033[46m'
    Magenta = '\033[45m'
    White = '\033[30;47m'
    Black = '\033[40m'
    Green = '\033[32m'
    Red = '\033[41m'
    Reset = '\033[0m'  # RESET


class Nodo(object):
    info, sig = None, None


aux = Nodo()
naux = aux

Arreglo = []
Número = 0

# Asignar Nodos
for i in range(1, 31):
    nodo = Nodo()
    nodo.info = i
    naux.sig = nodo
    naux = nodo

# Crear Array
for i in range(0, 6):
    Arreglo.append([0] * 7)

aux = aux.sig

# Asignar valores array
while (aux is not None):
    for x in range(1, 6):
        for y in range(0, 7):
            if aux != None:
                if x == 1:
                    if (y < 5):
                        Arreglo[x][y] = 0
                    else:
                        Arreglo[x][y] = (aux.info)
                        aux = aux.sig
                else:
                    Arreglo[x][y] = (aux.info)
                    aux = aux.sig

Arreglo[0][0] = "Do"
Arreglo[0][1] = "Lu"
Arreglo[0][2] = "Ma"
Arreglo[0][3] = "Mi"
Arreglo[0][4] = "Ju"
Arreglo[0][5] = "Vi"
Arreglo[0][6] = "Sa"

print("         MES ABRIL")
print
for x in range(0, 6):
    print("")

    for y in range(0, 7):
        if (x > 0):
            if (Arreglo[x][y] < 10):
                if (Arreglo[x][y] == 8):
                    print(bcolors.Yellow + "  " + str(Arreglo[x][y]) + bcolors.Reset, end=" ")
                elif (Arreglo[x][y] == 1):
                    print(bcolors.Black + "  " + str(Arreglo[x][y]) + bcolors.Reset, end=" ")
                elif (Arreglo[x][y] == 9):
                    print(bcolors.Magenta + "  " + str(Arreglo[x][y]) + bcolors.Reset, end=" ")
                else:
                    print("  " + str(Arreglo[x][y]), end=" ")
            else:
                if (Arreglo[x][y] == 14 or Arreglo[x][y] == 15 or Arreglo[x][y] == 18):
                    print(bcolors.Red + " " + str(Arreglo[x][y]) + bcolors.Reset, end=" ")
                elif (Arreglo[x][y] == 16):
                    print(bcolors.White + " " + str(Arreglo[x][y]) + bcolors.Reset, end=" ")
                elif (Arreglo[x][y] == 30):
                    print(bcolors.Black + " " + str(Arreglo[x][y]) + bcolors.Reset, end=" ")
                elif (Arreglo[x][y] == 23):
                    print(bcolors.Cyan + " " + str(Arreglo[x][y]) + bcolors.Reset, end=" ")
                else:
                    print(" " + str(Arreglo[x][y]), end=" ")

        else:
            print(" " + str(Arreglo[x][y]), end=" ")

print("\n\nNOTACIÓN DÍAS")
print(bcolors.Yellow + "Día Actual" + bcolors.Reset)
print(bcolors.Red + "Día Festivos" + bcolors.Reset)

print("\nNOTACIÓN LUNAS")
print(bcolors.Black + "Luna Nueva" + bcolors.Reset)
print(bcolors.White + "Luna Llena" + bcolors.Reset)
print(bcolors.Cyan + "Luna Creciente" + bcolors.Reset)
print(bcolors.Magenta + "Luna Menguante" + bcolors.Reset)

