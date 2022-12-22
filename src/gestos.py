import math
class gesto(): 

    enProceso = False 
    ejecutar = False
    fotogramas = 0


    posM = -1 
    posI = -1 

    estado1 = False 
    estado2 = False 
    estado3 = False 


    def actualizarEstado(self, hand_landmarks, mp_hands, height, width):
        pIndice = obtenerPosicion(height, width, hand_landmarks, mp_hands, "INDEX_FINGER_TIP")
        pMidle = obtenerPosicion(height, width, hand_landmarks, mp_hands, "INDEX_FINGER_TIP")
        dIndice = self.posI - pIndice[1]
        dMidle = self.posM - pMidle[1]
        self.fotogramas = self.fotogramas + 1
        print ("===============")
        print(self.fotogramas)
        print(dMidle)
        print ("===============")
        print(dIndice)
        print ("===============")
        #verifica si los dedos estan juntos
        distancia = hallarDistancia(pIndice[0], pIndice[1], pMidle[0],pMidle[1]);
        if(self.estado1 == False and distancia < 30):
            self.posI = pIndice[1]
            self.posM = pMidle[1]
            self.estado1 = True
            self.enProceso = True
            print("DESLIZAR1111")
            print("DESLIZAR1111")
        if(self.estado1 == True and distancia < 25 and self.estado2 == False
                and dIndice > 5 and dMidle > 5):
            self.estado2 = True;
            #ejecutar
            print("deslizar hacia abajo____________________________________________________________--")
            print("deslizar hacia abajo")
            print("deslizar hacia abajo")
            print("deslizar hacia abajo")
            self.reiniciar();

        if(self.fotogramas > 10000):
            self.reiniciar();

    def reiniciar(self):
        self.enProceso = False
        self.ejecutar = False

        self.posP = -1 
        self.posI = -1 

        self.estado1 = False 
        self.estado2 = False; 


#################FUNCIONES
def obtenerPosicion( height, width, hand_landmarks, mp_hands, nombrePunto):
    #UBICACIONES DE LA PUNTA DE LOS DEDOS:  PULGAR E INDICE
    posX = int(hand_landmarks.landmark[mp_hands.HandLandmark[nombrePunto]].x*width)
    posY = int(hand_landmarks.landmark[mp_hands.HandLandmark[nombrePunto]].y*height)
    posiciones = [posX, posY]
    return posiciones;

def hallarDistancia(x1, y1, x2, y2):
    distancia = math.sqrt((x1-x2)*2+(y1-y2)*2)
    return distancia;
