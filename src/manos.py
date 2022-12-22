import gestos
import math 
import cv2
import mediapipe as mp
import keyboardManage as k

def zoomInteligente():

        mp_drawing = mp.solutions.drawing_utils
        mp_hands = mp.solutions.hands


        cap = cv2.VideoCapture(0)

        with mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.5) as hands:


            ##################################
            #VARIABLES PARA EL ZOOM

            estado1 = False
            estado2 = False
            distancia = -1
            contador = 0
            boton = True

            ##################################
            #GESTOS USANDO OBJETOS
            deslizar = gestos.gesto()
            ##################################

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
                print("hello")

                #reconocimietno de la mano
                if results.multi_hand_landmarks is not None:
                    for hand_landmarks in results.multi_hand_landmarks:


                        #se obtienen las ubicaciones con HandLandmarks
                        #UBICACIONES DE LA PUNTA DE LOS DEDOS:  PULGAR E INDICE
                        Xpulgar = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x*width)
                        Ypulgar = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y*height)
                        
                        Xindice = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x*width)
                        Yindice = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y*height)

                        distancia = math.sqrt((Xpulgar-Xindice)**2+(Ypulgar-Yindice)**2)

                        #####GESTOS
                        deslizar.actualizarEstado(hand_landmarks, mp_hands, height,width)
                        #####

                        cv2.circle(frame, (Xpulgar, Ypulgar), 3, (255,0,0), 3)
                        cv2.circle(frame, (Xindice, Yindice), 3, (255,0,0), 3)



                
                
                if distancia> 0 and distancia < 30 :
                    print("estado1")
                    estado1 = True 

                if distancia >= 100 and estado1 == True and contador < 1:
                    print("estado1")
                    #SE ACTIVA EL ZOOM
                    estado2 = True
                    contador = contador+1
                    k.hacerZoom();
                    k.hacerZoom();
                    k.hacerZoom();


                if estado1 == True and estado2 == True and distancia < 100:
                    estado1 = False 
                    estado2 = False 
                    k.hacerMim();
                    k.hacerMim();
                    k.hacerMim();
                    contador = 0;
                    print("REINICIO.................")
                    print("REINICIO.................")
                    print("REINICIO.................")
                    print("REINICIO.................")
                    print("REINICIO.................")
                    print("REINICIO.................")
                    print("REINICIO.................")
                    print("REINICIO.................")


                if estado1 == True and estado2 == True:
                    print("SE MANTIENE EL GESTO")
                else:
                    print("SIN NINGUN GESTO")

                ####Se visualiza la imagen
                cv2.imshow('Frame',frame)
                if cv2.waitKey(1) & 0xFF == 27:
                    break
        cap.release()
        cv2.destroyAllWindows()
