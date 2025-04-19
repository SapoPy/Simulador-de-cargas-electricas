import numpy as np

class CargaElec:
    def __init__(self, q: float = -1.0, masa: float = 1.0, posicion = np.array([0,0]), velocidad = np.array([0,0]), Fuerza = np.array([0.0,0.0]), enlace = 0, constante_k = 1):
        self.q = q           # Valor de la carga
        self.masa = masa     # Valor de la masa              
        self.pos = posicion    # Vector de la posicion que le aplica    
        self.vel = velocidad    # Vector de la velocidad que le aplica
        self.fuerza = Fuerza    # Vector de la fuerza que le aplica
        self.enlace = enlace 
        self.k = constante_k

    def printval(self):
        """
        Muestra en terminal los atributos del objeto
        """
        print(f"\n{self}\nCarga = {self.q}\nMasa = {self.masa}\nPosicion = {self.pos}\nVelocidad = {self.vel}\nFuerza aplicada = {self.fuerza}\n")
    
    def campo_electrico(self, X, Y):
        "Calcula el campo eléctrico producido por esta carga en los puntos (X, Y)."
        k_e = 10

        dx =   X - self.pos[0]
        dy =   Y - self.pos[1] 
        r2 = dx**2 + dy **2

        E =  k_e * self.q / r2
        Ex = E * dx / np.sqrt(r2)
        Ey = E * dy / np.sqrt(r2)
        return Ex, Ey
    
    def campo_gravitatorio(self, X, Y):
        "Calcula el campo gravitacional producido por esta carga en los puntos (X, Y)."
        G_g = 1
    

        dx = X - self.pos[0]
        dy =  Y - self.pos[1]
        r2 = dx**2 + dy **2

        Gravedad =   - G_g * self.masa / r2
        Gravedad_x = Gravedad * dx / np.sqrt(r2)
        Gravedad_y = Gravedad * dy / np.sqrt(r2)
        return Gravedad_x, Gravedad_y
    
    def __matmul__(self, other) -> None:
        "Calcula las fuerza que se aplican mutuamente 2 cargas y se les suma a su atrubuto Fuerza"
        k_e = 10
        G_g = 1

        if self.q == 0 or other.q == 0:
            dpos = self.pos - other.pos
            r2 = dpos[0]**2 + dpos[1] **2

            Sum_fuerza = - G_g * self.masa * other.masa / r2 * dpos -self.k * dpos * self.enlace * other.enlace
            self.fuerza  = self.fuerza +  Sum_fuerza
            other.fuerza = other.fuerza - Sum_fuerza 
        else:

            dpos = self.pos - other.pos
            r2 = dpos[0]**2 + dpos[1] **2
            Sum_fuerza = (k_e * self.q * other.q - G_g * self.masa * other.masa) / r2 * dpos -self.k * dpos* self.enlace * other.enlace
            self.fuerza  = self.fuerza +  Sum_fuerza
            other.fuerza = other.fuerza - Sum_fuerza
    
    def __add__(self, other):
        if abs(self.q + other.q) < 0.01:
            return CargaElec(0, self.masa + other.masa, (self.pos + other.pos)/2, self.vel + other.vel, self.fuerza + other.fuerza)

        return CargaElec(self.q + other.q, self.masa + other.masa, (self.pos + other.pos)/2, self.vel + other.vel, self.fuerza + other.fuerza)


    def actualizarPos(self, dt = 0.1):
        self.vel = self.fuerza / self.masa * dt + self.vel
        self.pos = self.vel * dt + self.pos
        self.fuerza = 0

def linea_de_cargas(cargas: list, Num_cargas: int, coord_i, coord_f, valor_Q = -1, valor_masa = 1):
    for i in range(Num_cargas):
        lam = i/Num_cargas
        cargas.append(CargaElec(valor_Q,valor_masa , posicion = coord_i * lam + coord_f - lam * coord_f))

def circulo_de_cargas(cargas: list,Num_cargas: int, centro, radio, frac = 1,  desfase = 0, valor_Q = -1, valor_masa = 1):
    for i in range(Num_cargas):
        theta = i/Num_cargas * 2 * np.pi * frac
        cargas.append(CargaElec(valor_Q, valor_masa, posicion= (np.array([radio*np.cos(theta + desfase), radio*np.sin(theta + desfase) ]) + centro) ))