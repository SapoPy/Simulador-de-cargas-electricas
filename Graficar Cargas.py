import numpy as np
import matplotlib.pyplot as plt
from CargasElectricas import *


# Crear una malla de puntos
x = np.linspace(-10, 10, 200)
y = np.linspace(-10, 10, 200)
X, Y = np.meshgrid(x, y)

# Definir las cargas
cargas = [ ]
Num_Q = 50



circulo_de_cargas(cargas, Num_Q, [0, 1], 1, 0.5)

linea_de_cargas(cargas, Num_Q, [-5,-5], [0,0], 10)

circulo_de_cargas(cargas, Num_Q, [5, -3], 3, 0.5,np.pi,-3)

# Inicializar el campo total
Ex_total = np.zeros_like(X)
Ey_total = np.zeros_like(Y)

# Sumar los campos de cada carga
for carga in cargas:
    Ex, Ey = carga.campo(X, Y)
    Ex_total += Ex
    Ey_total += Ey

# Graficar líneas de campo eléctrico
fig, ax = plt.subplots(figsize=(6, 6))
color = np.log(np.hypot(Ex_total, Ey_total))  # para visualizar mejor la intensidad
ax.streamplot(X, Y, Ex_total, Ey_total, color=color, cmap='inferno', density=1.5)

# Dibujar las cargas
for carga in cargas:
    if carga.q > 0:
        ax.plot(carga.x, carga.y, 'ro')  # roja para positiva
    else:
        ax.plot(carga.x, carga.y, 'bo')  # azul para negativa

ax.set_title('Líneas de campo eléctrico')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_aspect('equal')
plt.grid(True)
plt.show()