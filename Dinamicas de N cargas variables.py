import numpy as np
import matplotlib.pyplot as plt
from CargasElectricas import *
import matplotlib.animation as animation

listaDeCargas = []

circulo_de_cargas(listaDeCargas, 2, np.array([0,0]), 10, valor_Q= -5)
linea_de_cargas(listaDeCargas, 2, np.array([-100, 50]), np.array([100, 50]), valor_Q= 0,valor_masa= 10 )
circulo_de_cargas(listaDeCargas, 2, np.array([-50,0]), 50, valor_Q= 3)

posEnX = []
posEnY = []
colorCarga = []
for carga in listaDeCargas:
    posEnX.append(carga.pos[0])
    posEnY.append(carga.pos[1])
    if carga.q > 0:
        colorCarga.append("blue")
    elif carga.q < 0:
        colorCarga.append("red")
    else:
        colorCarga.append("brown")

fig, ax = plt.subplots()
limx = 1000
limy = 1000

ax.set_xlim(-limx, limx)
ax.set_ylim(-limy, limy)

scat = ax.scatter([], [], c=[], animated=True)

def animate(i):
   
    for i in range(len(listaDeCargas)):
        for j in range(i + 1, len(listaDeCargas)):
            listaDeCargas[i] @ listaDeCargas[j]
    
    nuevas_posiciones = []
    nuevos_colores = []
    for carga in listaDeCargas:
        carga.actualizarPos()
        nuevas_posiciones.append([carga.pos[0], carga.pos[1]])

        if carga.q > 0:
            nuevos_colores.append("blue")
        elif carga.q < 0:
            nuevos_colores.append("red")
        else: 
            nuevos_colores.append("brown")

    scat.set_offsets(np.array(nuevas_posiciones))
    scat.set_color(nuevos_colores)
    return (scat,)

# Animación
ani = animation.FuncAnimation(fig, animate, frames= 100, blit=True)

plt.show()