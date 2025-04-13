import numpy as np
import matplotlib.pyplot as plt
from CargasElectricas import *
import matplotlib.animation as animation

electron1 = CargaElec(posicion= np.array([-1,0]))
electron2 = CargaElec(q=-10, masa= 10 ,posicion= np.array([1, 0]), velocidad=np.array([0,1]))
positron1 = CargaElec(q=3 , masa= 3, posicion=np.array([5, 1]))
neutron1 = CargaElec(q=0, masa= 100)



fig, ax = plt.subplots()
limx = 100
limy = 100

ax.set_xlim(-limx, limx)
ax.set_ylim(-limy, limy)

# Dos partículas: inicializamos con 2 puntos
scat = ax.scatter([electron1.pos[0], electron2.pos[0], positron1.pos[0]], [electron1.pos[1], electron2.pos[1], positron1.pos[1]], c=['red', 'red', 'blue'])

def animate(i):
   
    electron1 @ electron2
    electron1 @ positron1
    electron2 @ positron1
    
    electron1.actualizarPos()
    electron2.actualizarPos()
    positron1.actualizarPos()
    nuevas_posiciones = np.array([[electron1.pos[0], electron1.pos[1]], [electron2.pos[0], electron2.pos[1]], [positron1.pos[0], positron1.pos[1]]])


    scat.set_offsets(nuevas_posiciones)
    return (scat,)

# Animación
ani = animation.FuncAnimation(fig, animate, frames= 1000, interval=100, blit=True)

plt.show()