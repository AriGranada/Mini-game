# Importo los módulos que voy a utilizar
import tkinter as tk
from PIL import Image, ImageTk
import sqlite3

# Conexión a la base de datos
conexion = sqlite3.connect("jugadores.db")
cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS jugadores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        puntuacion INTEGER DEFAULT 0
    )
''')
conexion.commit()


def mostrar_pregunta1(nombre_jugador):
    ventana = tk.Tk()
    ventana.title("Pregunta 1")
    ventana.geometry("500x300")

    fondo_img = Image.open("guerra.png")
    fondo_img = fondo_img.resize((500, 300))
    fondo = ImageTk.PhotoImage(fondo_img)
    label_fondo = tk.Label(ventana, image=fondo)
    label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
    ventana.fondo = fondo  # guardar referencia

    pregunta = "¿Cuando empezo la Segunda Guerra Mundial? (deberias saberlo)"
    opciones = {
        "A": "1945",
        "B": "1935",
        "C": "1939",
        "D": "1914"
    }
    respuesta_correcta = "C"

    def responder(eleccion):
        if eleccion == respuesta_correcta:
            cursor.execute("UPDATE jugadores SET puntuacion = puntuacion + 10 WHERE nombre = ?", (nombre_jugador,))
            conexion.commit()
        ventana.destroy()
        mostrar_pregunta2(nombre_jugador)

    tk.Label(ventana, text=pregunta, font=("FangSong", 14), bg="lightblue").pack(pady=10)

    for clave, valor in opciones.items():
        texto = f"{clave} {valor}"
        tk.Button(ventana, text=texto, font=("FangSong", 12), bg="white",
                  command=lambda c=clave: responder(c)).pack(pady=5)

    ventana.mainloop()


def mostrar_pregunta2(nombre_jugador):
    ventana = tk.Tk()
    ventana.title("Pregunta 2")
    ventana.geometry("500x300")

    fondo_img = Image.open("banderas.png")
    fondo_img = fondo_img.resize((500, 300))
    fondo = ImageTk.PhotoImage(fondo_img)
    label_fondo = tk.Label(ventana, image=fondo)
    label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
    ventana.fondo = fondo

    pregunta = "¿Que colores tiene la bandera de Mexico?"
    opciones = {
        "A": "azul, blanco, rojo",
        "B": "verde, blanco, rojo",
        "C": "negro, amarillo, rojo",
        "D": "azul, blanco, rojo"
    }
    respuesta_correcta = "B"

    def responder(eleccion):
        if eleccion == respuesta_correcta:
            cursor.execute("UPDATE jugadores SET puntuacion = puntuacion + 10 WHERE nombre = ?", (nombre_jugador,))
            conexion.commit()
        ventana.destroy()
        mostrar_pregunta3(nombre_jugador)

    tk.Label(ventana, text=pregunta, font=("FangSong", 14), bg="lightblue").pack(pady=10)

    for clave, valor in opciones.items():
        texto = f"{clave} {valor}"
        tk.Button(ventana, text=texto, font=("FangSong", 12), bg="white",
                  command=lambda c=clave: responder(c)).pack(pady=5)

    ventana.mainloop()


def mostrar_pregunta3(nombre_jugador):
    ventana = tk.Tk()
    ventana.title("Pregunta 3")
    ventana.geometry("500x300")

    fondo_img = Image.open("libros.png")
    fondo_img = fondo_img.resize((500, 300))
    fondo = ImageTk.PhotoImage(fondo_img)
    label_fondo = tk.Label(ventana, image=fondo)
    label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
    ventana.fondo = fondo

    pregunta = "¿Quién escribió la Odisea?"
    opciones = {
        "A": "Unamuno",
        "B": "Cervantes",
        "C": "Shakespeare",
        "D": "Homero"
    }
    respuesta_correcta = "D"

    def responder(eleccion):
        if eleccion == respuesta_correcta:
            cursor.execute("UPDATE jugadores SET puntuacion = puntuacion + 10 WHERE nombre = ?", (nombre_jugador,))
            conexion.commit()
        ventana.destroy()
        mostrar_puntaje_final(nombre_jugador)

    tk.Label(ventana, text=pregunta, font=("FangSong", 14), bg="lightblue").pack(pady=10)

    for clave, valor in opciones.items():
        texto = f"{clave} {valor}"
        tk.Button(ventana, text=texto, font=("FangSong", 12), bg="white",
                  command=lambda c=clave: responder(c)).pack(pady=5)

    ventana.mainloop()


def mostrar_puntaje_final(nombre_jugador):
    ventana = tk.Tk()
    ventana.title("Resultado")
    ventana.geometry("300x200")

    fondo_img = Image.open("fiesta.png")
    fondo_img = fondo_img.resize((300, 200))
    fondo = ImageTk.PhotoImage(fondo_img)
    label_fondo = tk.Label(ventana, image=fondo)
    label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
    ventana.fondo = fondo

    cursor.execute("SELECT puntuacion FROM jugadores WHERE nombre = ?", (nombre_jugador,))
    puntuacion = cursor.fetchone()[0]

    tk.Label(ventana, text=f"¡Gracias por jugar, {nombre_jugador}!", font=("FangSong", 14), bg="lightgreen").pack(pady=10)
    tk.Label(ventana, text=f"Tu puntuacion final es: {puntuacion}", font=("FangSong", 14), bg="lightgreen").pack(pady=10)

    tk.Button(ventana, text="Salir", command=ventana.destroy, font=("FangSong", 12), bg="white").pack(pady=20)

    ventana.mainloop()


# Login principal
def comenzar_juego():
    nombre = entrada_nombre.get().strip().capitalize()
    if nombre:
        cursor.execute("INSERT INTO jugadores (nombre, puntuacion) VALUES (?, ?)", (nombre, 0))
        conexion.commit()
        root.destroy()
        mostrar_pregunta1(nombre)
    else:
        label_mensaje.config(text="Por favor, introduce un nombre")


# Ventana principal
root = tk.Tk()
root.title("Ventana Principal")
root.geometry("350x300")

# Fondo
fondo_img = Image.open("preguntas.png")
fondo_img = fondo_img.resize((350, 300))
fondo = ImageTk.PhotoImage(fondo_img)
label_fondo = tk.Label(root, image=fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
root.fondo = fondo

label_titulo = tk.Label(root, text="Introduce tu nombre", font=("FangSong", 14), bg="teal", fg="white")
label_titulo.pack(pady=10)

entrada_nombre = tk.Entry(root, font=("FangSong", 14))
entrada_nombre.pack(pady=10)

boton_comenzar = tk.Button(root, text="COMENZAR", font=("FangSong", 14), command=comenzar_juego, bg="white")
boton_comenzar.pack(pady=10)

label_mensaje = tk.Label(root, text="", fg="red", font=("FangSong", 14), bg="teal")
label_mensaje.pack(pady=10)

root.mainloop()
