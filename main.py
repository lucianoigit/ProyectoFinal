import tkinter as tk

import cv2
from interfaz.interfaz import Aplicacion
from calibrar_camara import calibrar_camara
from tomar_foto import tomar_foto
from corregir_distorsion import corregir_distorsion
from detectar_objeto import detectar_objetos
from enviar_informacion import enviar_informacion

def main():
    # Iniciar programa y tomar foto
    root = tk.Tk()
    app = Aplicacion(root)
    # No es necesario llamar a 'inicializar_interfaz', ya que los botones y su funcionalidad se han definido en el constructor __init__
    root.mainloop()

    """    # Luego de cerrar la interfaz, ejecutar el resto del código
    informacion_camera = {"matriz_camera": "", "coef_distorsion": ""}
    
    # Lista de rutas de imágenes de calibración
    imagenes_calibracion = ["./imagen1.jpg", "./imagen2.jpg"]

    # Calibrar la cámara
    matriz_camera, coef_distorsion = calibrar_camara(imagenes_calibracion)

    informacion_camera["matriz_camera"] = matriz_camera
    informacion_camera["coef_distorsion"] = coef_distorsion

    print("Matriz de la cámara:")
    print(informacion_camera["matriz_camera"])
    print("Coeficientes de distorsión:")
    print(informacion_camera["coef_distorsion"])

    imagen = app.tomar_y_mostrar_foto() """
    
   

    try:
        """ # Corregir distorsión
        foto_corregida = corregir_distorsion(imagen, informacion_camera["matriz_camera"], informacion_camera["coef_distorsion"])
 """
        # Detectar objetos
        """ objetos_detectados = app.detectar_objetos(imagen)
        enviar_informacion(objetos_detectados) """

    except Exception as e:
        print(f"Error en la ejecución principal: {e}")

if __name__ == "__main__":
    main()
