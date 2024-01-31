import pandas as pd
import torch
from ultralytics import YOLO

def detectar_objetos(imagen, confianza_minima=0.2, tamano_entrada=(416, 416)):
    print("Iniciando detección de objetos")
    try:
        # Cargar el modelo preentrenado YOLO
        model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
        resultados = model(imagen)
        imagenresutado=resultados.show()
        print (type(imagenresutado))

        # Obtener las cajas, nombres de clases (names) y probabilidades (probs)
        df = resultados.pandas().xyxy[0]

        # Filtrar detecciones con confianza mínima
        df_filtrado = df[df['confidence'] >= confianza_minima]
        
        # Calcular puntos centrales y agregar al DataFrame original
        df_filtrado['x_center'] = (df_filtrado['xmin'] + df_filtrado['xmax']) / 2
        df_filtrado['y_center'] = (df_filtrado['ymin'] + df_filtrado['ymax']) / 2

        # Convertir DataFrame filtrado a JSON
        

        # Lógica para obtener las posiciones de los objetos detectados
        return df_filtrado,imagenresutado

    except Exception as e:
        print(f"Error al detectar objetos: {e}")
        return []

