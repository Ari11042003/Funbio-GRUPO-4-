import tkinter as tk
import cv2

# Inicializar la cámara USB
camera = cv2.VideoCapture(0)

def encender_camara():
    global camera
    while True:
        ret, frame = camera.read()
        cv2.imshow("Cámara", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def modo_traduccion():
    # Código del modo de traducción
    print("Modo Traducción Activado")
    continuar = input("¿Deseas continuar en el modo de traducción? (s/n): ")
    if continuar.lower() == 'n':
        opciones_pantalla_tactil()

def modo_interactivo():
    # Código del modo interactivo
    print("Modo Interactivo Activado")
    continuar = input("¿Deseas continuar en el modo interactivo? (s/n): ")
    if continuar.lower() == 'n':
        opciones_pantalla_tactil()

def opciones_pantalla_tactil():
    ventana = tk.Tk()
    ventana.title("Opciones")

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
    cv2.destroyAllWindows()

if __name__ == "__main__":
    try:
        encender_camara()
        opciones_pantalla_tactil()

    except KeyboardInterrupt:
        pass

    finally:
        apagar_camara()

