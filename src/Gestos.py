import funciones as f
import cv2
import keyboardManage as k
from time import sleep

class Gestos:

    def __init__(self):
        self.activate = True
        self.preparandoSalir = False

    def pasarDatos(self, frame, hand_landmarks, mp_hands, height, width) :
        self.frame = frame
        self.hand_landmarks = hand_landmarks
        self.mp_hands = mp_hands
        self.height = height
        self.width = width

    def hacerZoom(self):
        if not self.preparandoSalir : 
            #UBICACIONES DE LA PUNTA DE LOS DEDOS:  PULGAR E INDICE
            Xpulgar, Ypulgar = f.obtenerPosicion(self.height, self.width, self.hand_landmarks, self.mp_hands, "THUMB_TIP");
            Xindice, Yindice = f.obtenerPosicion(self.height, self.width, self.hand_landmarks, self.mp_hands, "INDEX_FINGER_TIP");

            distancia = f.hallarDistancia(Xpulgar, Ypulgar, Xindice, Yindice)

            #Dibujamos los puntos
            cv2.circle(self.frame, (Xpulgar, Ypulgar), 3, (255,0,0), 3)
            cv2.circle(self.frame, (Xindice, Yindice), 3, (255,0,0), 3)


            
            print("DISTACNOA " , distancia)
            print("DISTACNOA " , distancia)
            print("DISTACNOA " , distancia)
            print("DISTACNOA " , distancia)
            print("DISTACNOA " , distancia)
            print("DISTACNOA " , distancia)
            print("DISTACNOA " , distancia)
            print("DISTACNOA " , distancia)

            
            #Si distancia es amyor qu 110 -> haz zoom
            if distancia >= 110:
                print("activarZOOOOM")
                print("activarZOOOOM")
                print("activarZOOOOM")
                print("activarZOOOOM")
                print("activarZOOOOM")
                print("activarZOOOOM")
                
                #SE ACTIVA EL ZOOM
                #informacionZoom["estanEstirados"] = True
                #informacionZoom["estanJuntos"] == False
                sleep(.4)
                k.hacerZoom();

            if 40 <  distancia and distancia < 110:
                #Si distncai esta entre el intervalo de 20 y 110 -> minimiza
                sleep(.4)
                k.hacerMim();
                print("Hacer MIIIIIIM")
                print("Hacer MIIIIIIM")
                print("Hacer MIIIIIIM")
                print("Hacer MIIIIIIM")
                print("Hacer MIIIIIIM")
                print("Hacer MIIIIIIM")

            if  distancia < 40 :#sI ES menor QUE 20 no hagas nada
                #informacionZoom["estanJuntos"] = True
                #informacionZoom["estanEstirados"] = False
                print("demasiadoJutnos para hacer Zoom")
                print("demasiadoJutnos para hacer Zoom")
                print("demasiadoJutnos para hacer Zoom")
                print("demasiadoJutnos para hacer Zoom")
                print("demasiadoJutnos para hacer Zoom")
                print("demasiadoJutnos para hacer Zoom")


    def cerrarPrograma(self):

        Xpulgar, Ypulgar = f.obtenerPosicion(self.height, self.width,self.hand_landmarks, self.mp_hands, "THUMB_TIP");
        Xmedio, Ymedio = f.obtenerPosicion(self.height, self.width,self.hand_landmarks, self.mp_hands, "MIDDLE_FINGER_TIP");

        distancia = f.hallarDistancia(Xpulgar, Ypulgar, Xmedio, Ymedio)

        #Dibujamos los puntos
        cv2.circle(self.frame, (Xpulgar, Ypulgar), 3, (255,0,0), 3)
        cv2.circle(self.frame, (Xmedio, Ymedio), 3, (255,0,0), 3)

        #Verificar si estan juntos
        if 0 < distancia and distancia < 15:
            self.preparandoSalir =True
            print("Preprando para cerrarr")
            print("Preprando para cerrarr")
            print("Preprando para cerrarr")
            print("Preprando para cerrarr")
            print("Preprando para cerrarr")
            print("Preprando para cerrarr")
            print("Preprando para cerrarr")

        
        #Si se juntaron y separraon con una dsitancia mayor a 100, cierra el programa
        if self.preparandoSalir == True and distancia > 130:
            print("Cierra el programa")
            print("Cierra el programa")
            print("Cierra el programa")
            print("Cierra el programa")
            print("Cierra el programa")
            self.activate = False;
            return;
        
        