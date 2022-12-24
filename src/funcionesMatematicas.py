import math

def distanciaPuntos(p1, p2):
    distancia = math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
    return distancia;
