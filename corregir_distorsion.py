import cv2
import numpy as np

def corregir_distorsion(imagen, matriz_camara, coef_distorsion):
    # Convertir la imagen a escala de grises
    print("iniciando correccion de distorsion ")
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Obtener la nueva matriz de la cámara y region de interés (ROI)
    nueva_matriz_camara, roi = cv2.getOptimalNewCameraMatrix(matriz_camara, coef_distorsion, (imagen.shape[1], imagen.shape[0]), 1, (imagen.shape[1], imagen.shape[0]))

    # Aplicar corrección de distorsión
    dst = cv2.undistort(gris, matriz_camara, coef_distorsion, None, nueva_matriz_camara)
    print("finalizando correccion de distorsion ")
    return dst
