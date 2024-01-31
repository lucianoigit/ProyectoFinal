import cv2
import corregir_distorsion
import enviar_informacion
import tomar_foto
from detectar_objeto import detectar_objetos  # Asegúrate de importar la función detectar_objetos

def aplicacion_yolo():
    entrada = input("¿Desea iniciar el programa? (Sí/No): ").lower()
    
    if entrada == "si" or entrada == "s":
        print("Programa iniciado")

        
    else:
        print("Programa no iniciado")
