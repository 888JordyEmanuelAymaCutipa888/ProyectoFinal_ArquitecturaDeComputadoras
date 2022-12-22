import math

def obtenerPosicion( height, width, hand_landmarks, mp_hands, nombrePunto):
    #UBICACIONES DE LA PUNTA DE LOS DEDOS:  PULGAR E INDICE
    posX = int(hand_landmarks.landmark[mp_hands.HandLandmark[nombrePunto]].x*width)
    posY = int(hand_landmarks.landmark[mp_hands.HandLandmark[nombrePunto]].y*height)
    posiciones = [posX, posY]
    return posiciones;

def hallarDistancia(x1, y1, x2, y2):
    distancia = math.sqrt((x1-x2)**2+(y1-y2)**2)
    return distancia;