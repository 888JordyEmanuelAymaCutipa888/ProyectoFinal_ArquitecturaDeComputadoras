import funcionesMatematicas as fm
import math
class gesto(): 

    def __init__(self):
        self.activate = True
        self.preparandoSalir = False #Condicional para cerrar el programa
        self.ubicacionInicio = None #Para bajar y subir
        self.estado1 = False 
        self.estado2 = False 
        self.posM = -1 
        self.posI = -1
        self.enProceso = None
        self.gestosRegistros = ['deslizarAbajo'] #
        self.fotogramas = 0
        self.descanso = 0

    def pasarDatos(self, frame, hand_landmarks, mp_hands, height, width) :
        self.frame = frame
        self.hand_landmarks = hand_landmarks
        self.mp_hands = mp_hands
        self.height = height
        self.width = width


    ##########Prohibe la sincronización de gestos###############

    def controladorGestos(self):
        if(self.gestoEnProceso == None):
            print("a")
            for gesto in enumerate(self.gestosRegistros):
                self.gestoEnProceso = self.realizarGesto(gesto[1])()
                if(self.gestoEnProceso != None):
                    break
        else:
            print(self.gestoEnProceso)
            self.realizarGesto(self.gestoEnProceso)()
            

    def realizarGesto(self,gesto): 
        return {
                'deslizarAbajo' : lambda: self.deslizarAbajo(),
                }.get(gesto, lambda:None)

    #############################################################



    def deslizarAbajo(self):
        pIndice = obtenerPosicion(self.height, self.width, self.hand_landmarks, self.mp_hands, "INDEX_FINGER_TIP")
        pMidle = obtenerPosicion(self.height, self.width, self.hand_landmarks, self.mp_hands, "MIDDLE_FINGER_TIP")
        dMidle = self.posM - pMidle[1]
        dIndice = self.posI - pIndice[1]

        print ("===============")
        print("DATOOOS")
        print("FOTOGRAMAS" and self.fotogramas)
        print("DIFERENCIA DE MEDIOS" and dMidle)
        print("DIFERENCIA DE INDICE" and dIndice)
        print ("===============")
        #verifica si los dedos estan juntos
        distancia = hallarDistancia(pIndice[0], pIndice[1], pMidle[0], pMidle[1])
        print("DISTANCIAAAA CLASE")
        print(distancia)
        print ("===============")
        if(self.estado1 == False and distancia < 35):
            print("DESLIZAR1111")
            print("DESLIZAR1111")
            self.posI = pIndice[1]
            self.posM = pMidle[1]
            self.estado1 = True
            self.enProceso = True

        if(self.estado1 == True and distancia < 35 and self.estado2 == False
                and dIndice > 10 and dMidle > 10):
            self.estado2 = True
            #ejecutar
            print("deslizar hacia abajo____________________________________________________________--")
            print("deslizar hacia abajo")
            print("deslizar hacia abajo")
            print("deslizar hacia abajo")

        if(self.estado1 == True):
            self.fotogramas = self.fotogramas+1
        if(self.estado2 == True):
            self.descanso = self.descanso +1
        
        if(self.fotogramas > 25 or (self.estado2 == True and self.descanso > 5)):
            self.reiniciar()
            self.enProceso = None

    def zoom(self):
        Indice = obtenerPosicion(self.height, self.width, self.hand_landmarks, self.mp_hands, "INDEX_FINGER_TIP")
        Midle = obtenerPosicion(self.height, self.width, self.hand_landmarks, self.mp_hands, "MIDDLE_FINGER_TIP")
        distanciaPulgarIndice = hallarDistancia()
        pass



    def reiniciar(self):
        self.enProceso = False
        self.ejecutar = False

        self.posP = -1 
        self.posI = -1 

        self.estado1 = False 
        self.estado2 = False; 

        self.fotogramas = 0
        self.descanso = 0



#################FUNCIONES
def obtenerPosicion(height, width, hand_landmarks, mp_hands, nombrePunto):
    #UBICACIONES DE LA PUNTA DE LOS DEDOS:  PULGAR E INDICE
    posX = int(hand_landmarks.landmark[mp_hands.HandLandmark[nombrePunto]].x*width)
    posY = int(hand_landmarks.landmark[mp_hands.HandLandmark[nombrePunto]].y*height)
    posiciones = [posX, posY]
    return posiciones;

def hallarDistancia(x1, y1, x2, y2):
    distancia = math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))
    return distancia;
