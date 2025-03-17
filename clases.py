import random
from variables import *

class Tablero:
    def __init__(self):
        self.tablero_real = [[" "] * tamanio for _ in range(tamanio)]
        self.tablero_visible = [[" "] * tamanio for _ in range(tamanio)]

    def colocar_barco(self, longitud):
        colocado = False
        

        while not colocado :
            fila, columna = random.randint(0, tamanio - 1), random.randint(0, tamanio - 1)
            direccion = random.choice(["N", "S", "E", "O"])  # Norte, Sur, Este, Oeste
            posiciones = []

            if direccion == "E" and columna + longitud <= tamanio:
                posiciones = [(fila, columna + i) for i in range(longitud)]
            elif direccion == "O" and columna - (longitud - 1) >= 0:
                posiciones = [(fila, columna - i) for i in range(longitud)]
            elif direccion == "S" and fila + longitud <= tamanio:
                posiciones = [(fila + i, columna) for i in range(longitud)]
            elif direccion == "N" and fila - (longitud - 1) >= 0:
                posiciones = [(fila - i, columna) for i in range(longitud)]

            # Verifica si las posiciones están libres antes de colocar el barco
            if posiciones and all(self.tablero_real[x][y] == " " for x, y in posiciones):
                for x, y in posiciones:
                    self.tablero_real[x][y] = "B"
                colocado = True


    
    def recibir_disparo(self, fila, col):
        if self.tablero_real[fila][col] == "B":
            self.tablero_real[fila][col] = "X"
            self.tablero_visible[fila][col] = "X"
            return True
        else:
            self.tablero_visible[fila][col] = "O"
            return False
    
    def todos_hundidos(self):
        return all("B" not in fila for fila in self.tablero_real)

class Jugador:
    def __init__(self, nombre, es_maquina=False):
        self.nombre = nombre
        self.es_maquina = es_maquina
        self.tablero = Tablero()
        self.vidas = sum(longitud * cantidad for longitud, cantidad in BARCOS.items())  
        self.disparos_realizados = set()

    def colocar_barcos(self):
        for longitud, cantidad in BARCOS.items():
            for _ in range(cantidad):
                self.tablero.colocar_barco(longitud)


    def disparar(self, enemigo):
        if self.es_maquina:
            while True:
                fila, col = random.randint(0, tamanio - 1), random.randint(0, tamanio - 1)
                if (fila, col) not in self.disparos_realizados:
                    self.disparos_realizados.add((fila, col))
                    break
            print(f"La máquina dispara a ({fila}, {col})")
        else:
            while True:
                try:
                    fila, col = map(int, input("Introduce coordenadas (fila columna): ").split())
                    if 0 <= fila < tamanio and 0 <= col < tamanio and (fila, col) not in self.disparos_realizados:
                        self.disparos_realizados.add((fila, col))
                        break
                    print("Coordenadas inválidas o ya disparaste ahí.")
                except ValueError:
                    print("Introduce números válidos.")

        impacto = enemigo.tablero.recibir_disparo(fila, col)
        
        if impacto:
            enemigo.tablero.tablero_visible[fila][col] = "X"
        else:
            enemigo.tablero.tablero_visible[fila][col] = "O"
        
        if impacto:
            enemigo.vidas -= 1  # Reducimos las vidas si impactamos
        return impacto

    
    def derrotado(self):
        return self.vidas <= 0  # Se considera derrotado si todas sus vidas llegan a 0

