# 🚢 Hundir la Flota (Battleship Game)

Este proyecto es una implementación en **Python** del clásico juego de "Hundir la Flota" (Battleship).  
Se juega desde la **terminal** y enfrenta a un **jugador humano** contra una **máquina** que dispara de forma aleatoria.

## 📜 Descripción del juego

El objetivo del juego es **destruir todos los barcos del adversario** antes de que el adversario destruya los tuyos.  
Cada jugador tiene un **tablero de 10x10** donde se colocan los barcos de forma aleatoria.  

En cada turno:
- **El jugador introduce coordenadas (fila, columna)** para disparar al tablero enemigo.
- **Si acierta un barco**, puede volver a disparar.
- **Si falla**, el turno pasa a la máquina.
- **La máquina dispara de forma aleatoria** en el tablero del jugador.

El juego termina cuando un jugador **pierde todos sus barcos**.

## Funciones clave del código:

  -  **mostrar_tablero():** Muestra los tableros correctamente en la terminal.
  -  **colocar_barco():** Posiciona los barcos aleatoriamente en el tablero.
  -  **disparar():** Permite al jugador o a la máquina hacer un disparo.
  -  **jugar_turno():** Maneja los turnos y actualiza los tableros
