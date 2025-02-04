# Inteligencia artificial
# Israel Espinosa López
# 2025-01-30

import tkinter as tk
from tkinter import messagebox
import random
#Librerias


Celda_Tam = 50
limpio = "white"
sucio = "black"
aspiradora = "green"
# varibles
def matriz(filas, columnas):
    return [[random.choice([0,1]) for _ in range (columnas)] for _ in range(filas)]

def dibujar_matriz():
    canvas.delete("all")  # Limpiar el canvas
    for i in range(filas):
        for j in range(columnas):
            x1, y1 = j * Celda_Tam, i * Celda_Tam
            x2, y2 = x1 + Celda_Tam, y1 + Celda_Tam
            color = sucio if matriz[i][j] == 1 else limpio
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")
    dibujar_aspiradora()

# Función para dibujar la aspiradora
def dibujar_aspiradora():
    x1, y1 = aspiradora_col * Celda_Tam, aspiradora_fila * Celda_Tam
    x2, y2 = x1 + Celda_Tam, y1 + Celda_Tam
    canvas.create_oval(x1, y1, x2, y2, fill=aspiradora, outline="gray")

# Función para mover la aspiradora
def mover_aspiradora():
    global aspiradora_fila, aspiradora_col

    # Limpiar la celda actual si está sucia
    if matriz[aspiradora_fila][aspiradora_col] == 1:
        matriz[aspiradora_fila][aspiradora_col] = 0
        dibujar_matriz()

    # Moverse a una celda vecina aleatoria
    movimientos = [
        (aspiradora_fila - 1, aspiradora_col),  # Arriba
        (aspiradora_fila + 1, aspiradora_col),  # Abajo
        (aspiradora_fila, aspiradora_col - 1),  # Izquierda
        (aspiradora_fila, aspiradora_col + 1),
        (aspiradora_fila + 1, aspiradora_col + 1),
        (aspiradora_fila - 1,aspiradora_col - 1),
        (aspiradora_fila + 1, aspiradora_col - 1),
        (aspiradora_fila - 1,aspiradora_col + 1)
    ]
    movimientos_validos = [
        (f, c) for f, c in movimientos
        if 0 <= f < filas and 0 <= c < columnas
    ]

    if movimientos_validos:##Tinen un mal fincionamiento en el movimeiento
        aspiradora_fila, aspiradora_col = random.choice(movimientos_validos)
        dibujar_matriz()

    # Verificar si todas las celdas están limpias
    if all(all(celda == 0 for celda in fila) for fila in matriz):
        messagebox.showinfo("Fin", "¡Todas las celdas están limpias!")
        return

    # Programar el siguiente movimiento
    root.after(500, mover_aspiradora)

# Función para iniciar la simulación
def iniciar_simulacion():
    global filas, columnas, matriz, aspiradora_fila, aspiradora_col

    try:
        # Obtener el número de filas y columnas
        filas = int(entry_filas.get())
        columnas = int(entry_columnas.get())

        # Validar que los valores sean positivos
        if filas <= 0 or columnas <= 0:
            messagebox.showerror("Error", "El número de filas y columnas debe ser mayor que 0.")
            return

        # Generar la matriz de suciedad
        matriz = matriz(filas, columnas)

        # Obtener la posición inicial de la aspiradora
        aspiradora_fila = int(entry_aspiradora_fila.get())
        aspiradora_col = int(entry_aspiradora_col.get())

        # Validar la posición de la aspiradora
        if not (0 <= aspiradora_fila < filas and 0 <= aspiradora_col < columnas):
            messagebox.showerror("Error", "La posición de la aspiradora está fuera de la matriz.")
            return

        # Dibujar la matriz y la aspiradora
        dibujar_matriz()

        # Iniciar la simulación
        root.after(1000, mover_aspiradora)

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")


# Crear la ventana principal
root = tk.Tk()
root.title("Simulación de Aspiradora Autónoma")

# Campos de entrada para filas y columnas
tk.Label(root, text="Filas:").grid(row=0, column=0, padx=10, pady=10)
entry_filas = tk.Entry(root)
entry_filas.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Columnas:").grid(row=1, column=0, padx=10, pady=10)
entry_columnas = tk.Entry(root)
entry_columnas.grid(row=1, column=1, padx=10, pady=10)

# Campos de entrada para la posición de la aspiradora
tk.Label(root, text="Fila de la aspiradora:").grid(row=2, column=0, padx=10, pady=10)
entry_aspiradora_fila = tk.Entry(root)
entry_aspiradora_fila.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Columna de la aspiradora:").grid(row=3, column=0, padx=10, pady=10)
entry_aspiradora_col = tk.Entry(root)
entry_aspiradora_col.grid(row=3, column=1, padx=10, pady=10)

# Botón para iniciar la simulación
tk.Button(root, text="Iniciar Simulación", command=iniciar_simulacion).grid(row=4, column=0, columnspan=2, pady=10)

# Canvas para dibujar la matriz
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()