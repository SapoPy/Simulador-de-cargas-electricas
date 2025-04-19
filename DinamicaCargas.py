import numpy as np
import matplotlib.pyplot as plt
from CargasElectricas import *
import matplotlib.animation as animation

electron1 = CargaElec(posicion=np.array([10000, -100]), velocidad=np.array([0, 200]))
positron1 = CargaElec(q=10,masa = 10000 ,posicion=np.array([100, 0]))
neutron1 = CargaElec(q=0, masa = 20040, posicion= np.array([-1000, 0]), velocidad=np.array([100,-100]))


fig, ax = plt.subplots()
limx = 30000
limy = 30000

ax.set_xlim(-limx, limx)
ax.set_ylim(-limy, limy)

# Dos partículas: inicializamos con 2 puntos
scat = ax.scatter([electron1.pos[0],  positron1.pos[0], neutron1.pos[0]], [electron1.pos[1], positron1.pos[1], neutron1.pos[1]], c=['red', 'blue', "brown"])

def animate(i):
   
    electron1 @ positron1
    electron1 @ neutron1
    positron1 @ neutron1
   
    
    electron1.actualizarPos(dt =0.03333)
    positron1.actualizarPos(dt =0.03333)
    neutron1.actualizarPos(dt =0.03333)
    nuevas_posiciones = np.array([[electron1.pos[0], electron1.pos[1]], [positron1.pos[0], positron1.pos[1]], [neutron1.pos[0], neutron1.pos[1]]])

    scat.set_offsets(nuevas_posiciones)
    return (scat,)

# Animación
ani = animation.FuncAnimation(fig, animate, frames= 1000, interval=1, blit=True)

plt.show()