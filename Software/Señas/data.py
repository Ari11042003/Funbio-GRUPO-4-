import cv2
import mediapipe as mp

# Inicializar la detección de manos
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Inicializar la captura de video
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("No se puede acceder a la cámara.")
        break

    # Convertir la imagen de BGR a RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Procesar la imagen para detectar manos
    results = hands.process(image_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for point in hand_landmarks.landmark:
                x = int(point.x * image.shape[1])
                y = int(point.y * image.shape[0])
                cv2.circle(image, (x, y), 5, (0, 255, 0), -1)

    cv2.imshow('Detención de Mano', image)

    if cv2.waitKey(5) & 0xFF == 27:
        break

hands.close()
cap.release()
cv2.destroyAllWindows()
