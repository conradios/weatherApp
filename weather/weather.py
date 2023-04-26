import tkinter as tk
import requests
import io
import urllib.request
from PIL import ImageTk, Image

api_key = "cdfbd6525456a0f4fa53cfd2cb782e3a"

def obtener_clima(ciudad):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        temperatura = datos["main"]["temp"] - 273.15
        humedad = datos["main"]["humidity"]
        viento = datos["wind"]["speed"]
        return f"Temperatura: {temperatura:.2f} °C\nHumedad: {humedad}%\nViento: {viento} m/s"
    else:
        return "Error al obtener los datos."

def obtener_mapa(ciudad):
    ciudad = ciudad.replace(' ', '_')
    url = f"https://maps.googleapis.com/maps/api/staticmap?center={ciudad}&zoom=11&size=500x500&key=AIzaSyAqtxb3njkcDQ_0GXtHS5IS2xIOmr51Mzk"
    imagen_bytes = urllib.request.urlopen(url).read()
    imagen = Image.open(io.BytesIO(imagen_bytes))
    return imagen

def mostrar_clima():
    global mapa_imagen_tk
    ciudad = entrada_ciudad.get()
    clima = obtener_clima(ciudad)
    etiqueta_clima.config(text=clima)
    mapa_imagen = obtener_mapa(ciudad)
    mapa_imagen_tk = ImageTk.PhotoImage(mapa_imagen)
    etiqueta_mapa.config(image=mapa_imagen_tk)
    etiqueta_mapa.image = mapa_imagen_tk

ventana = tk.Tk()
ventana.title("Clima")
ventana.iconphoto(True, tk.PhotoImage(file=r"C:\Users\conra\Documents\workspace\py\weather\Weather.png"))

# Configuración de la fuente
font_title = ("Helvetica", 20, "bold")
font_label = ("Helvetica", 14)
font_button = ("Helvetica", 14, "bold")

# Configuración de los colores
color_fondo = "#02BADA"
color_etiqueta = "#454F9E"
color_boton = "#1e90ff"

# Configuración de la ventana
ventana.geometry("600x600")
ventana.configure(bg=color_fondo)
ventana.resizable(False, False)

# etiqueta "Ciudad"
etiqueta_ciudad = tk.Label(ventana, text="Ciudad:", font=font_title, fg=color_etiqueta, bg=color_fondo)
etiqueta_ciudad.pack(pady=10)

# Configuración de la entrada de texto para la ciudad
entrada_ciudad = tk.Entry(ventana, font=font_label)
entrada_ciudad.pack(pady=10)

# botón "Consultar"
boton_consultar = tk.Button(ventana, text="Consultar", font=font_button, bg=color_boton, fg="white", command=mostrar_clima)
boton_consultar.pack(pady=10)

# etiqueta que muestra el clima
etiqueta_clima = tk.Label(ventana, text="", font=font_label, bg=color_fondo)
etiqueta_clima.pack(pady=10)

# etiqueta que muestra el mapa
etiqueta_mapa = tk.Label(ventana)
etiqueta_mapa.pack(fill=tk.BOTH, expand=True, padx=50, pady=50)

ventana.mainloop()
