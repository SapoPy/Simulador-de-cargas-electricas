import numpy as np

class CargaElec:
    def __init__(self, q, x, y):
        self.q = q        # Magnitud de la carga
        self.x = x        # Posición en x
        self.y = y        # Posición en y

    def campo(self, X, Y):
        """Calcula el campo eléctrico producido por esta carga en los puntos (X, Y)."""
        k_e = 1
        dx = X - self.x
        dy = Y - self.y
        r2 = dx**2 + dy**2
        r2[r2 == 0] = 1e-20  # evitar división por cero
        E = self.q / r2
        Ex = E * dx / np.sqrt(r2)
        Ey = E * dy / np.sqrt(r2)
        return Ex, Ey

def linea_de_cargas(cargas, Num_cargas, coord_i, coord_f, valor_Q = 1):
    for i in range(Num_cargas):
        lam = i/Num_cargas
        cargas.append(CargaElec(valor_Q, coord_i[0] * lam + coord_f[0] - lam * coord_f[0], coord_i[1] * lam + coord_f[1] - lam * coord_f[1]))

def circulo_de_cargas(cargas,Num_cargas, centro, radio, frac = 1,  desfase = 0, valor_Q = 1):
    for i in range(Num_cargas):
        theta = i/Num_cargas * 2 * np.pi * frac
        cargas.append(CargaElec(valor_Q, radio*np.cos(theta + desfase) + centro[0], radio*np.sin(theta + desfase) + centro[1] ))