import serial
import time

def enviar_informacion(informacion, puerto_serial='COM5', velocidad_serial=115200):
    try:
        # Configura el objeto Serial
        ser = serial.Serial(puerto_serial, velocidad_serial, timeout=1)
        time.sleep(2)  # Espera 2 segundos para que el puerto serial se abra correctamente

        # Envía la información al ESP32
        ser.write(informacion.encode())
        print(f"Información enviada al ESP32: {informacion}")

    except Exception as e:
        print(f"Error al enviar información: {e}")

    finally:
        # Cierra el puerto serial al finalizar
        ser.close()
        print("Puerto serial cerrado.")


