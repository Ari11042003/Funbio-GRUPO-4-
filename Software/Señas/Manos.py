import cv2
import mediapipe as mp
import os

# ----------------------------- Creamos la carpeta donde almacenaremos el entrenamiento ---------------------------------
nombre = 'Mano_Izquierda'
direccion = 'C:/Users/derek/Desktop/Señas/Manos/Fotos/Validacion'
carpeta = os.path.join(direccion, nombre)
if not os.path.exists(carpeta):
    print('Carpeta creada: ', carpeta)
    os.makedirs(carpeta)

# Asignamos un contador para el nombre de la fotos
cont = 0

# Leemos la cámara
cap = cv2.VideoCapture(0)

# ----------------------------Creamos un objeto que va a almacenar la detección y el seguimiento de las manos------------
clase_manos = mp.solutions.hands
manos = clase_manos.Hands()

# ----------------------------------Metodo para dibujar las manos---------------------------
dibujo = mp.solutions.drawing_utils

while True:
    ret, frame = cap.read()
    color = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    copia = frame.copy()
    resultado = manos.process(color)
    posiciones = []  # En esta lista vamos a almacenar las coordenadas de los puntos

    if resultado.multi_hand_landmarks:  # Si hay algo en los resultados entramos al if
        for mano in resultado.multi_hand_landmarks:  # Buscamos la mano dentro de la lista de manos que nos da el descriptor
            for id, lm in enumerate(mano.landmark):  # Vamos a obtener la información de cada mano encontrada por el ID
                alto, ancho, c = frame.shape
                corx, cory = int(lm.x * ancho), int(lm.y * alto)
                posiciones.append([id, corx, cory])
                dibujo.draw_landmarks(frame, mano, clase_manos.HAND_CONNECTIONS)
            if len(posiciones) != 0:
                pto_i5 = posiciones[9]  # Punto central
                x1, y1 = pto_i5[1] - 80, pto_i5[2] - 80
                ancho, alto = x1 + 80, y1 + 80
                x2, y2 = x1 + ancho, y1 + alto
                dedos_reg = copia[y1:y2, x1:x2]
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
                dedos_reg = cv2.resize(dedos_reg, (200, 200), interpolation=cv2.INTER_CUBIC)
                cv2.imwrite(carpeta + "/Mano_{}.jpg".format(cont), dedos_reg)
                cont += 1

    cv2.imshow("Video", frame)
    k = cv2.waitKey(1)
    if k == 27 or cont >= 300:
        break

cap.release()
cv2.destroyAllWindows()
