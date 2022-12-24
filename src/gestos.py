import keyboardManage as k
import funcionesMatematicas as fm
import math

class Gestos(): 

    def __init__(self):
        self.activate = True
        self.preparandoSalir = False #Condicional para cerrar el programa
        self.ubicacionInicio = None #Para bajar y subir
        self.estado1 = False 
        self.estado2 = False 
        self.posM = -1 
        self.posI = -1
        self.gestoEnProceso= None
        self.gestosRegistros = ['deslizarAbajo', 'zoom'] #
        self.fotogramas = 0
        self.descanso = 0
        self.repeticiones = 0

    def pasarDatos(self, frame, hand_landmarks, mp_hands, height, width) :
        self.frame = frame
        self.hand_landmarks = hand_landmarks
        self.mp_hands = mp_hands
        self.height = height
        self.width = width


    ##########Prohibe la sincronización de gestos###############

    def controladorGestos(self):
        print("GESTO EN PROCESO============>:    ", self.gestoEnProceso)
        if(self.gestoEnProceso == None):
            for gesto in enumerate(self.gestosRegistros):
                self.realizarGesto(gesto[1])()
                if(self.gestoEnProceso != None):
                    break
        else:
            print(self.gestoEnProceso)
            self.realizarGesto(self.gestoEnProceso)()
            

    def realizarGesto(self,gesto): 
        return {
                'deslizarAbajo' : lambda: self.deslizarAbajo(),
                'zoom' : lambda: self.zoom(),
                }.get(gesto, lambda:None)

    #############################################################



    def deslizarAbajo(self):
        pIndice = obtenerPosicion(self.height, self.width, self.hand_landmarks, self.mp_hands, "INDEX_FINGER_TIP")
        pMidle = obtenerPosicion(self.height, self.width, self.hand_landmarks, self.mp_hands, "MIDDLE_FINGER_TIP")
        dMidle = self.posM - pMidle[1]
        dIndice = self.posI - pIndice[1]

        print ("===============")
        print("DATOOOS: ")
        print("FOTOGRAMAS: ", self.fotogramas)
        print("DIFERENCIA DE MEDIOS: ", dMidle)
        print("DIFERENCIA DE INDICE: ", dIndice)
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
            self.gestoEnProceso = 'deslizarAbajo'

        if(self.estado1 == True and distancia < 35 and self.estado2 == False
                and dIndice > 10 and dMidle > 10):
            self.estado2 = True
            #ejecutar
            print("deslizar_______________________________________________________________________-")
            k.bajarPagina(7)

        if(self.estado1 == True):
            self.fotogramas = self.fotogramas+1
        if(self.estado2 == True):
            self.descanso = self.descanso +1
        
        if(self.fotogramas > 25 or (self.estado2 == True and self.descanso > 5) or distancia > 35):
            self.reiniciar()
            self.gestoEnProceso = None





    def zoom(self):
        indice = obtenerPosicion(self.height, self.width, self.hand_landmarks, self.mp_hands, "INDEX_FINGER_TIP")
        pulgar = obtenerPosicion(self.height, self.width, self.hand_landmarks, self.mp_hands, "THUMB_TIP")
        distancia = fm.distanciaPuntos(indice, pulgar)

        ##cv2.circle(frame, (Xpulgar, Ypulgar), 3, (0,0,255), 3)
        #cv2.circle(frame, (Xindice, Yindice), 3, (0,0,255), 3)
        print("DISTANCIA ZOOM: ", distancia)
        print("REPETICIONES ZOOM: ", self.repeticiones)
        if distancia> 0 and distancia < 30 and self.estado1 == False:
            print("DEDO PULGAR E INDICE JUNTOS")
            self.estado1 = True 
            self.gestoEnProceso = 'zoom'


        if distancia >= 100 and self.estado1 == True and self.repeticiones <1:
            print("estado2")
            #SE ACTIVA EL ZOOM
            self.estado2 = True
            self.repeticiones = self.repeticiones + 1
            k.hacerZoom();
            k.hacerZoom();
            k.hacerZoom();

        if self.estado1 == True and self.estado2 == True:
            print("SE MANTIENE EL GESTO********************************************************************")
        else:
            print("SIN NINGUN GESTO")
        if self.estado1 == True and self.estado2 == True and distancia < 100:
            self.estado1 = False 
            self.estado2 = False 
            k.hacerMim();
            k.hacerMim();
            k.hacerMim();
            self.repeticiones = 0;
            self.gestoEnProceso = None
            self.reiniciar()
            print("REINICIO.................")
            print("REINICIO.................")
            print("REINICIO.................")
            print("REINICIO.................")
            print("REINICIO.................")
            print("REINICIO.................")
            print("REINICIO.................")
            print("REINICIO.................")



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
