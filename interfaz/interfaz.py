import cv2
import tkinter as tk
from tkinter import filedialog, scrolledtext
from PIL import Image, ImageTk
from detectar_objeto import detectar_objetos
from enviar_informacion import enviar_informacion
from calibrar_camara import calibrar_camara
from estado import ver_estado_motores
from aplicacion import aplicacion_yolo
from tomar_foto import tomar_foto
from generar_informacion import generar_informacion

class Aplicacion:
    informacion = None  # Variable de clase para almacenar la información

    def __init__(self, root):
        self.root = root
        self.root.title("Interfaz Automatizada")

       
        self.imagen_resultado = None
        self.objetos_detectados = None
        self.imagen_capturada = None

        # Botones
        self.btn_cargar_imagen = tk.Button(self.root, text="Cargar Imagen", command=self.cargar_imagen)
        self.btn_calibrar_aparato = tk.Button(self.root, text="Calibrar Aparato", command=self.calibrar_aparato)
        self.btn_ver_estado_motores = tk.Button(self.root, text="Ver Estado de Motores", command=self.ver_estado_motores)
        self.btn_iniciar_programa = tk.Button(self.root, text="Iniciar Programa", command=self.iniciar_programa)
        self.btn_tomar_foto = tk.Button(self.root, text="Tomar Foto", command=self.tomar_foto)

        # Lienzo para mostrar la imagen
        self.canvas = tk.Canvas(root, width=800, height=450)
        self.canvas.grid(row=1, column=0, columnspan=5)  # Span 5 columnas para abarcar todo el ancho

        # Widget de texto para mostrar DataFrame
        self.text_widget = scrolledtext.ScrolledText(root, width=100, height=10, wrap=tk.WORD)
        self.text_widget.grid(row=2, column=0, columnspan=5)  # Span 5 columnas

        # Posicionamiento de los botones en la parte superior izquierda
        self.btn_cargar_imagen.grid(row=0, column=0)
        self.btn_calibrar_aparato.grid(row=0, column=1)
        self.btn_ver_estado_motores.grid(row=0, column=2)
        self.btn_iniciar_programa.grid(row=0, column=3)
        self.btn_tomar_foto.grid(row=0, column=4)

        # Mostrar DataFrame durante la inicialización
        self.mostrar_informacion()

    def cargar_imagen(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.imagen_capturada = cv2.imread(file_path)
            self.mostrar_imagen(self.imagen_capturada)

    def mostrar_imagen(self, imagen):
        if imagen is not None:
            imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
            imagen_pil = Image.fromarray(imagen_rgb)
            imagen_tk = ImageTk.PhotoImage(imagen_pil)
            self.canvas.create_image(400, 300, anchor=tk.CENTER, image=imagen_tk)
            self.canvas.imagen_tk = imagen_tk

    def calibrar_aparato(self):
        calibrar_camara()

    def ver_estado_motores(self):
        ver_estado_motores()

    def iniciar_programa(self):
        self.tomar_foto()
        if self.imagen_capturada is not None:
            self.detectar_objetos(self.imagen_capturada)
            if self.objetos_detectados is not None:
                self.mostrar_imagen(self.imagen_capturada)
                self.enviar_informacion(self.objetos_detectados)
                self.mostrar_informacion()
                return self.informacion
        else:
            print("No se ha capturado ninguna imagen.")

    def tomar_foto(self):
        self.imagen_capturada = tomar_foto()

    def detectar_objetos(self, imagen):
        try:
            self.objetos_detectados, self.imagen_resultado = detectar_objetos(imagen)
        except Exception as e:
            print(f"Error en la detección de objetos: {e}")

    def mostrar_informacion(self):
        # Limpiar contenido previo en el widget de texto
        self.text_widget.delete(1.0, tk.END)

        if self.objetos_detectados is not None and not self.objetos_detectados.empty:
            # Convertir DataFrame a cadena de texto
            info_text = self.objetos_detectados.to_string(index=False)

            # Insertar el texto en el widget de texto
            self.text_widget.insert(tk.END, info_text)
        else:
            # Mostrar un mensaje si no hay objetos detectados
            self.text_widget.insert(tk.END, "No se detectaron objetos")


    def enviar_informacion(self, objetos_detectados):
        try:
            self.informacion = enviar_informacion(generar_informacion(objetos_detectados))
        except Exception as e:
            print(f"Error al enviar información: {e}")

