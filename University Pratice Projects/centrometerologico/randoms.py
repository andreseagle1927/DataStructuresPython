import random
from unittest import case

def randomtemperatura():
    a = random.randint(-15,30)
    estado_clima = None
    humedad = None

    if a <= 0:
        estado_clima = "Nevado"
        humedad = random.randint(18,28)
        presion = random.randint(1050, 1150)

    elif a <= 10 and a > 0:
        estado_clima = "Lluvioso"
        humedad = random.randint(15,43)
        presion = random.randint(1150, 1250)

    elif a <= 25 and a > 10:
        estado_clima = "Nublado"
        humedad = random.randint(9,15)
        presion = random.randint(1250, 1350)

    elif a <= 40 and a > 20:
        estado_clima = "Soleado"
        humedad = random.randint(4,9)
        presion = random.randint(1350, 1450)
    
    
    
    
    return a ,presion , humedad, estado_clima
    
        
    
    

numero, presion , humedad, clima = randomtemperatura()

