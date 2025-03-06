import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image

def seleccionar_imagen():
    """Abrir un cuadro de diálogo para seleccionar una imagen"""
    ruta = filedialog.askopenfilename(
        title="Seleccionar imagen",
        filetypes=[("Archivos de imagen", "*.jpg;*.jpeg;*.png;*.gif;*.bmp;*.tiff;*.webp")]
    )
    entrada_ruta.delete(0, tk.END)
    entrada_ruta.insert(0, ruta)

def seleccionar_carpeta():
    """Abrir un cuadro de diálogo para seleccionar una carpeta de destino"""
    carpeta = filedialog.askdirectory(title="Seleccionar carpeta de destino")
    entrada_carpeta.delete(0, tk.END)
    entrada_carpeta.insert(0, carpeta)

def convertir_imagen():
    """Convertir la imagen seleccionada al formato elegido"""
    ruta_imagen = entrada_ruta.get()
    formato_salida = formato_seleccionado.get().lower()
    carpeta_destino = entrada_carpeta.get()

    if not os.path.exists(ruta_imagen):
        messagebox.showerror("Error", "La imagen seleccionada no existe.")
        return

    try:
        # Abrir la imagen
        imagen = Image.open(ruta_imagen)
        nombre_base = os.path.splitext(os.path.basename(ruta_imagen))[0]

        # Si no hay carpeta destino, usar la misma carpeta de la imagen original
        if not carpeta_destino:
            carpeta_destino = os.path.dirname(ruta_imagen)

        # Asegurar que la carpeta destino existe
        os.makedirs(carpeta_destino, exist_ok=True)

        # Ruta de salida
        ruta_salida = os.path.join(carpeta_destino, f"{nombre_base}.{formato_salida}")
        
        # Guardar imagen en el nuevo formato
        imagen.save(ruta_salida)
        
        messagebox.showinfo("Éxito", f"Imagen convertida y guardada en:\n{ruta_salida}")

    except Exception as e:
        messagebox.showerror("Error", f"Error al convertir la imagen: {e}")

# Crear la ventana principal
root = tk.Tk()
root.title("Convertidor de Imágenes")
root.geometry("400x300")

# Widgets
tk.Label(root, text="Ruta de la imagen:").pack(pady=5)
entrada_ruta = tk.Entry(root, width=40)
entrada_ruta.pack()
tk.Button(root, text="Seleccionar imagen", command=seleccionar_imagen).pack(pady=5)

tk.Label(root, text="Selecciona el formato de salida:").pack(pady=5)
opciones_formato = ["JPG", "PNG", "GIF", "BMP", "TIFF", "WEBP"]
formato_seleccionado = tk.StringVar(value=opciones_formato[0])
menu_formato = ttk.Combobox(root, textvariable=formato_seleccionado, values=opciones_formato)
menu_formato.pack(pady=5)

tk.Label(root, text="Carpeta de destino (opcional):").pack(pady=5)
entrada_carpeta = tk.Entry(root, width=40)
entrada_carpeta.pack()
tk.Button(root, text="Seleccionar carpeta", command=seleccionar_carpeta).pack(pady=5)

tk.Button(root, text="Convertir imagen", command=convertir_imagen).pack(pady=10)

# Ejecutar la ventana
root.mainloop()
