import cv2

def tomar_foto():
    print("tomando fotografia")
    cam = cv2.VideoCapture(0)
    
    # Tomar una foto
    ret, foto = cam.read()

    
    # Liberar la cámara
    cam.release()

    return foto
