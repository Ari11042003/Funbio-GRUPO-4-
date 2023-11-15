import tkinter as tk
import cv #se realizó el cambio de cv2 a openCV (cv)

# Inicializar la cámara USB (raspberry cam)
camera = cv.VideoCapture(0)

def encender_camara():
    global camera
    while True:
        ret, frame = camera.read()
        cv.imshow("Cámara", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

def modo_traduccion():
    print("Modo Traducción Activado")
    # Código del modo de traducción (aquí debería insertarse lo del dataset para que solo la cámara reconozca y te arroje los valores(letras) tal como funciona en una laptop)
    continuar = input("¿Deseas continuar en el modo de traducción? (s/n): ")
    if continuar.lower() == 'n':
        opciones_pantalla_tactil()

def modo_interactivo():
    print("Modo Interactivo Activado")
    # Código del modo interactivo (la idea es establecer un número de letras a ser procesadas, con la cámara registrará las señas que se hacen y como tiene un máximo de letras definida, al final deberá devolver la palabra formada
    continuar = input("¿Deseas continuar en el modo interactivo? (s/n): ")
    if continuar.lower() == 'n':
        opciones_pantalla_tactil()

def opciones_pantalla_tactil():
    ventana = tk.Tk()
    ventana.title("Opciones") #las opciones se encuentran en lo de botones (unas líneas abajo de esto

    # Función para apagar la cámara y finalizar el programa
    def apagar():
        ventana.destroy()
        apagar_camara()

    etiqueta = tk.Label(ventana, text="¿Qué modo deseas activar?")
    etiqueta.pack(pady=10)

    boton_traduccion = tk.Button(ventana, text="Modo Traducción", command=modo_traduccion)
    boton_traduccion.pack(pady=5)

    boton_interactivo = tk.Button(ventana, text="Modo Interactivo", command=modo_interactivo)
    boton_interactivo.pack(pady=5)

    boton_apagar = tk.Button(ventana, text="Apagar y Salir", command=apagar)
    boton_apagar.pack(pady=5)

    ventana.mainloop()

def apagar_camara():
    global camera
    camera.release()
    cv.destroyAllWindows()

if __name__ == "__main__": #interfaz principal, de aquí primero se enciende la cámara y luego sigue con el programa (respuesta táctil), cada función se encuentra identada en la parte de arriba
    try:
        encender_camara()
        opciones_pantalla_tactil()

    except KeyboardInterrupt:
        pass

    finally:
        apagar_camara()
