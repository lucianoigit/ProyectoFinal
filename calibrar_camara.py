import numpy as np
import cv2
import os  # Importa el módulo 'os' para verificar la existencia de archivos

def calibrar_camara(imagenes_calibracion):
    try:
        # Definir el tamaño del tablero de ajedrez (número de esquinas internas)
        esquinas_interior = (8, 6)  # Por ejemplo, 8x6 esquinas internas

        # Preparar puntos de objeto, como (0,0,0), (1,0,0), (2,0,0), ..., (7,5,0)
        puntos_objeto = np.zeros((np.prod(esquinas_interior), 3), dtype=np.float32)
        puntos_objeto[:, :2] = np.mgrid[0:esquinas_interior[0], 0:esquinas_interior[1]].T.reshape(-1, 2)

        # Listas para almacenar puntos de objeto y puntos de imagen de todas las imágenes de calibración
        puntos_objeto_total = []
        puntos_imagen_total = []

        for imagen_calibracion in imagenes_calibracion:
            if not os.path.exists(imagen_calibracion):
                print(f"Error: La imagen {imagen_calibracion} no existe.")
                continue  # Salta a la siguiente iteración si la imagen no existe

            imagen = cv2.imread(imagen_calibracion)
            imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

            # Encontrar esquinas del tablero de ajedrez
            ret, esquinas = cv2.findChessboardCorners(imagen_gris, esquinas_interior, None)

            if ret:
                puntos_objeto_total.append(puntos_objeto)
                puntos_imagen_total.append(esquinas)

        # Verifica si hay al menos una imagen válida para la calibración
        if not puntos_objeto_total:
            raise ValueError("No se encontraron imágenes válidas para la calibración.")

        # Calibrar cámara
        ret, matriz_camera, coef_distorsion, _, _ = cv2.calibrateCamera(
            puntos_objeto_total, puntos_imagen_total, imagen_gris.shape[::-1], None, None
        )

        return matriz_camera, coef_distorsion

    except Exception as e:
        print(f"Error en la calibración de la cámara: {e}")
        return None, None
