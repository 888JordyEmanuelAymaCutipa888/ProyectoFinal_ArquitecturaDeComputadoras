# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import cv2
import mediapipe as mp
import math

#Codigo inteligente que analizara los moviminetos de las manos de las personas
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

mpDibujo = mp.solutions.drawing_utils
confiDibu = mpDibujo.DrawingSpec(thickness=1,circle_radius=1)

