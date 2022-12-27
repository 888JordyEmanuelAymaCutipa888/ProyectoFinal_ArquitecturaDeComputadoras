import cv2
import mediapipe as mp
import keyboardManage as k
import funciones as f
import math

class Gestos(): 

    def __init__(self):
        self.activate = True
        self.puntosInciales = None
        self.estados = [False, False];
        self.gestoEnProceso = None
        self.gestosRegistros = ['deslizarYdesplazar', 'zoom', 'cerrarPrograma'] #
        self.fotogramas = 0
        self.descanso = 0
        self.repeticiones = 0

    def pasarDatos(self, frame, hand_landmarks, mp_hands, height, width) :
        self.frame = frame
        self.hand_landmarks = hand_landmarks
        self.mp_hands = mp_hands
        if(mp_hands == None):
            print ("NO HAY MANOS")
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
                'deslizarYdesplazar' : lambda: self.deslizarYdesplazar(),
                'zoom' : lambda: self.zoom(),
                'cerrarPrograma' : lambda: self.cerrarPrograma(),
                }.get(gesto, lambda:None)

    #############################################################





    #######____  FUNCIONES PARA LOS GESTOS  ____######

    ############ REALIZAR ZOOM
    def zoom(self):

        #################
        #estado[0]: Juntar los dedos: indice y pulgar
        #estado[1]: Estirar o separar los dedos índice y pulgar
        #################

        #Se obtiene los datos de los dedos(puntos)
        indice = self.posicionPunto("INDEX_FINGER_TIP")
        pulgar = self.posicionPunto("THUMB_TIP")

        #Dibujamos los puntos
        if(self.estados[0] == True):
            cv2.circle(self.frame, (indice[0], indice[1]), 3, (255,0,0), 3)
            cv2.circle(self.frame, (pulgar[0], pulgar[1]), 3, (255,0,0), 3)

        #se obtiene la distancia
        distancia = f.distanciaPuntos(indice, pulgar)

        #Se verifica si se juntaron los dedos(indice, pulgar)
        if distancia> 0 and distancia < 30 and self.estados[0] == False:
            print("DEDO PULGAR E INDICE JUNTOS")
            self.estados[0] = True 
            self.gestoEnProceso = 'zoom'


        #Se verifica si los dedos se encuentran estirados
        if distancia >= 100 and self.estados[0] == True and self.repeticiones <1:
            print("estado2")
            #SE ACTIVA EL ZOOM
            self.estados[1] = True
            self.repeticiones = self.repeticiones + 1
            k.hacerZoom(3);

        #Deshace o termina el gesto bajo condiciones
        if self.estados[0] == True and self.estados[1] == True and distancia < 100:
            k.hacerMim(3);
            self.reiniciar()


    
    ######## DESLIZAR HACIA ARRIBA O HACIA ABAJO
    def deslizarYdesplazar(self):

        ##########################
        #estado1: Representa si el dedo indice y medio estan juntos
        #estado2: Representa la elevacion(subir) de los dedos
        ##########################

        Indice = self.posicionPunto("INDEX_FINGER_TIP")
        Midle = self.posicionPunto("MIDDLE_FINGER_TIP")

        #Dibujamos los puntos
        if(self.estados[0] == True):
            cv2.circle(self.frame, (Indice[0], Indice[1]), 3, (0,255,0), 3)
            cv2.circle(self.frame, (Midle[0], Midle[1]), 3, (0,255,0), 3)

        #verifica si los dedos estan juntos(indice y medio)
        distancia = f.distanciaPuntos(Indice, Midle)

        #distancia maxima para aceptar dedos juntos
        distanciaLimite = 35
        if(self.puntosInciales == None):
            #guarda la posición inicial de los dedos: indice y medio
            if(self.estados[0] == False and distancia < distanciaLimite):
                self.puntosInciales = [Indice, Midle]
                self.estados[0] = True
                self.gestoEnProceso = 'deslizarYdesplazar'

        else: 
            #diferencia en el eje y
            YdifIndice = self.puntosInciales[0][1] - Indice[1]
            YdifMidle = self.puntosInciales[1][1] - Midle[1]

            #diferencia en el eje y
            XdifIndice = self.puntosInciales[0][0] - Indice[0]
            XdifMidle = self.puntosInciales[1][0] - Midle[0]

            #Si se realiza el gesto de subir los dedos
            if(self.estados[0] == True and distancia < distanciaLimite and self.estados[1] == False
                and YdifIndice > 25 and YdifMidle > 25):
                self.estados[1] = True
                print("________________________________-abajo")
                k.bajarPagina(7)

            #Si se realiza el gesto de bajar los dedos
            elif(self.estados[0] == True and distancia < distanciaLimite and self.estados[1] == False
                and YdifIndice < -25 and YdifIndice < -25):
                self.estados[1] = True
                print("_________________________________-arriba")
                k.subirPagina(7)

            #verifica si se desplzaron los dedos hacia la izquierda
            elif(self.estados[0] == True and distancia < distanciaLimite and self.estados[1] == False
                and XdifIndice > 25 and XdifMidle > 25):
                self.estados[1] = True
                k.paginaSiguiente(1)
                print("_______________________________-DERECHA-SIGUIENTE")

            #verifica si se desplzaron los dedos hacia la derecha
            elif(self.estados[0] == True and distancia < distanciaLimite and self.estados[1] == False
               and XdifIndice < -25 and XdifIndice < -25):
                self.estados[1] = True
                k.paginaAnterior(1)
                print("_______________________________-IZQUIERDA-ATRAS")

        #Se establecen condiciones para que el gesto concluya
        if(self.estados[0] == True):
            self.fotogramas = self.fotogramas+1
        if(self.estados[1] == True):
            self.descanso = self.descanso +1
        
        if(self.fotogramas > 25 or self.descanso > 10 or distancia > distanciaLimite):
            self.reiniciar()


    ############  CERRAR EL PROGRAMA
    def cerrarPrograma(self):

        ################
        #estado[0]: representa si se junto el dedo pulgar y medio
        ################

        #posiciones
        pulgar = self.posicionPunto("THUMB_TIP")
        medio = self.posicionPunto("MIDDLE_FINGER_TIP")

        distancia = f.distanciaPuntos(pulgar, medio)

        #Dibujamos los puntos
        if(self.estados[0] == True):
            cv2.circle(self.frame, (pulgar[0], pulgar[1]), 3, (0,0,255), 3)
            cv2.circle(self.frame, (medio[0], medio[1]), 3, (0,0,255), 3)

        #Verificar si estan juntos
        if 0 < distancia and distancia < 30 and self.estados[0] == False:

            self.estados[0] = True
            self.gestoEnProceso = 'cerrarPrograma'
        
        #Si se juntaron y separraon con una dsitancia mayor a 100, cierra el programa
        if self.estados[0] == True and distancia > 100:
            self.reiniciar()
            self.activate = False;
            return;


    ################# FUNCIONES DE CLASE
    def reiniciar(self):
        self.__init__()


    def posicionPunto(self, nombrePunto):
        #UBICACIONES DE LA PUNTA DE LOS DEDOS:  PULGAR E INDICE
        posiciones = f.obtenerPosicion(self.height, self.width, self.hand_landmarks, self.mp_hands, nombrePunto)
        return posiciones;
