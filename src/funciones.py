import math

def distanciaPuntos(p1, p2):
    distancia = math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
    return distancia;

def obtenerPosicion(height, width, hand_landmarks, mp_hands, nombrePunto):
    #UBICACIONES DE LA PUNTA DE LOS DEDOS:  PULGAR E INDICE
    posX = int(hand_landmarks.landmark[mp_hands.HandLandmark[nombrePunto]].x*width)
    posY = int(hand_landmarks.landmark[mp_hands.HandLandmark[nombrePunto]].y*height)
    posiciones = [posX, posY]
    return posiciones;

