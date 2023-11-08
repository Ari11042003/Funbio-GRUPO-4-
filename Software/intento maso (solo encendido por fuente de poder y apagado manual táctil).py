import RPi.GPIO as GPIO
import picamera
import time
import tkinter as tk

# Configurar el pin de detección de energía
PIN_DETECCION_ENERGIA = 17 # el 17 es solo de ejemplo por mientras

def inicializar():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_DETECCION_ENERGIA, GPIO.IN)

def encender_camara():
    with picamera.PiCamera() as camera:
        camera.start_preview()
        while not GPIO.input(PIN_DETECCION_ENERGIA):
            time.sleep(1)
        camera.stop_preview()

def modo_traduccion():
    # Código específico del modo de traducción
    print("Modo Traducción Activado")
    continuar = input("¿Deseas continuar en el modo de traducción? (s/n): ")
    if continuar.lower() == 'n':
        opciones_pantalla_tactil()

def modo_interactivo():
    # Código específico del modo interactivo
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
    
    GPIO.cleanup()  

if __name__ == "__main__":
    try:
        inicializar()
        encender_camara()
        opciones_pantalla_tactil()

    except KeyboardInterrupt:
        pass

    finally:
        GPIO.cleanup()
        
