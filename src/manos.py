import math 
import cv2
import mediapipe as mp
import keyboardManage as k
import sys
from time import sleep



#################FUNCIONES
def hacerZoom(frame, hand_landmarks, mp_hands, height, width, informacionZoom):
        #UBICACIONES DE LA PUNTA DE LOS DEDOS:  PULGAR E INDICE
        Xpulgar, Ypulgar = obtenerPosicion(height, width, hand_landmarks, mp_hands, "THUMB_TIP");
        Xindice, Yindice = obtenerPosicion(height, width, hand_landmarks, mp_hands, "INDEX_FINGER_TIP");

        distancia = hallarDistancia(Xpulgar, Ypulgar, Xindice, Yindice)

        #Dibujamos los puntos
        cv2.circle(frame, (Xpulgar, Ypulgar), 3, (255,0,0), 3)
        cv2.circle(frame, (Xindice, Yindice), 3, (255,0,0), 3)


        
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
            print("activarZOOOOM")
            print("activarZOOOOM")
            
            #SE ACTIVA EL ZOOM
            informacionZoom["estanEstirados"] = True
            informacionZoom["estanJuntos"] == False
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
            informacionZoom["estanJuntos"] = True
            informacionZoom["estanEstirados"] = False
            print("demasiadoJutnos para hacer Zoom")
            print("demasiadoJutnos para hacer Zoom")
            print("demasiadoJutnos para hacer Zoom")
            print("demasiadoJutnos para hacer Zoom")
            print("demasiadoJutnos para hacer Zoom")
            print("demasiadoJutnos para hacer Zoom")
        


def cerrarPrograma(frame, hand_landmarks, mp_hands,height, width, informacionCerrar):
    Xpulgar, Ypulgar = obtenerPosicion(height, width,hand_landmarks, mp_hands, "THUMB_TIP");
    Xmedio, Ymedio = obtenerPosicion(height, width,hand_landmarks, mp_hands, "MIDDLE_FINGER_TIP");

    distancia = hallarDistancia(Xpulgar, Ypulgar, Xmedio, Ymedio)

    #Dibujamos los puntos
    cv2.circle(frame, (Xpulgar, Ypulgar), 3, (255,0,0), 3)
    cv2.circle(frame, (Xmedio, Ymedio), 3, (255,0,0), 3)

    #Verificar si estan juntos
    if 0 < distancia and distancia < 10:
        informacionCerrar["seJuntaron"] =True
        print("Preprando para cerrarr")
        return True;

    
    #Si se juntaron y separraon con una dsitancia mayor a 100, cierra el programa
    if informacionCerrar["seJuntaron"] == True and distancia >70:
        print("Cierra el programa")
        print("Cierra el programa")
        print("Cierra el programa")
        print("Cierra el programa")
        print("Cierra el programa")
        return False;


    return True;
    # if distancia >:
    #     informacionCerrar["seJuntaron"] =False
    #     print("Dedeos demasiado juntos ")

def obtenerPosicion( height, width, hand_landmarks, mp_hands, nombrePunto):
    #UBICACIONES DE LA PUNTA DE LOS DEDOS:  PULGAR E INDICE
    posX = int(hand_landmarks.landmark[mp_hands.HandLandmark[nombrePunto]].x*width)
    posY = int(hand_landmarks.landmark[mp_hands.HandLandmark[nombrePunto]].y*height)
    posiciones = [posX, posY]
    return posiciones;

def hallarDistancia(x1, y1, x2, y2):
    distancia = math.sqrt((x1-x2)**2+(y1-y2)**2)
    return distancia;

def iniciarReconocimiento():
    
    #Nos ayudara a ddibujar los 21 PUNTOS y su Conexiones
    mp_drawing = mp.solutions.drawing_utils
    #Emplearemos la solutions hands
    mp_hands = mp.solutions.hands

    cap = cv2.VideoCapture(0)

    #Capturar Camara
    height = 1;
    width = 1;

    #Configuramos para modo Video
    with mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=2,
        min_detection_confidence=0.5) as hands:
        ##################################
        #VARIABLES
        informacionZoom = {
            "estanJuntos" : False,
            "estanSeparados" : False,
        }
        informacionCerrar = {
            "seJuntaron": False,
        }
        ##################################
        bandera = True
        while bandera:
            ret, frame = cap.read()
            if ret == False:
                print("Saliendo.....")
                break

            #Capturamos el ancho y altura del video
            height, width, _ = frame.shape
            #Volteamos en modo espejo
            frame = cv2.flip(frame, 1)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            results = hands.process(frame_rgb)
            if results.multi_hand_landmarks is not None:
                for hand_landmarks in results.multi_hand_landmarks:
                    
                    hacerZoom(frame, hand_landmarks, mp_hands, height, width, informacionZoom)
                    bandera = cerrarPrograma(frame, hand_landmarks, mp_hands, height, width, informacionCerrar)
            
            cv2.imshow('Frame',frame)

            
            
            



            if cv2.waitKey(1) & 0xFF == 27:
                break
    cap.release()
    cv2.destroyAllWindows()




