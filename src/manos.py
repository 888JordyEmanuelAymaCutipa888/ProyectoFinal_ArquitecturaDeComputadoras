from gestos import Gestos
import math 
import cv2
import mediapipe as mp
import keyboardManage as k

def zoomInteligente():

        mp_drawing = mp.solutions.drawing_utils
        mp_hands = mp.solutions.hands


        cap = cv2.VideoCapture(0)

        #Capturar Camara
        height = 1;
        width = 1;


        with mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.5) as hands:

            boton = True


            ##########ContraladorGEstos
            gestos  = Gestos()
            ##########ContraladorGEstos

            while boton:
                #bonton = interfaz
                ret, frame = cap.read()
                if ret == False:
                    print("Buclehello")
                    break
                height, width, _ = frame.shape

                ####se obtiene un fotograma utlizando openCV
                frame = cv2.flip(frame, 1)
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                ####Aquí se obtiene la informacion de la mano
                ###Si no encuentra ninguna results toma none
                results = hands.process(frame_rgb)

                #reconocimietno de la mano
                if results.multi_hand_landmarks is not None:
                    for hand_landmarks in results.multi_hand_landmarks:


                        #se obtienen las ubicaciones con HandLandmarks
                        #UBICACIONES DE LA PUNTA DE LOS DEDOS:  PULGAR E INDICE
                        Xpulgar = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x*width)
                        Ypulgar = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y*height)
                        
                        Xindice = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x*width)
                        Yindice = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y*height)

                        #####GESTOS
                        gestos.pasarDatos(frame, hand_landmarks, mp_hands, height, width)
                        gestos.controladorGestos()
                        #####

                        cv2.circle(frame, (Xpulgar, Ypulgar), 3, (255,0,0), 3)
                        cv2.circle(frame, (Xindice, Yindice), 3, (255,0,0), 3)

                ####Se visualiza la imagen
                cv2.imshow('Frame',frame)
                if cv2.waitKey(1) & 0xFF == 27:
                    break
        cap.release()
        cv2.destroyAllWindows()


zoomInteligente()
