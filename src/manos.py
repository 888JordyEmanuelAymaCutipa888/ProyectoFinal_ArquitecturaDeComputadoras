
import cv2
import mediapipe as mp
import keyboardManage as k
import sys
from Gestos import Gestos
from time import sleep


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
        max_num_hands=1,
        min_detection_confidence=0.5) as hands:
        
        gesto = Gestos();
        while gesto.activate:
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

            if results.multi_handedness == None:
                print("No ha manosossssssssss")
                print("No ha manosossssssssss")
                print("No ha manosossssssssss")
                print("No ha manosossssssssss")
                print("No ha manosossssssssss")
                print("No ha manosossssssssss")
                gesto.preparandoSalir = False;
                gesto.ubicacionInicio = None

            if results.multi_hand_landmarks is not None:
                for hand_landmarks in results.multi_hand_landmarks:
                    #Pasamos datos que sirven para el reconocimiento
                    gesto.pasarDatos(frame, hand_landmarks, mp_hands, height, width)
                    gesto.controladorGestos()
                    #gesto.hacerZoom()
                    #gesto.cerrarPrograma()
                    gesto.moverUpDown();
            
            cv2.imshow('Frame',frame)

            if cv2.waitKey(1) & 0xFF == 27:
                break
    cap.release()
    cv2.destroyAllWindows()


iniciarReconocimiento()
