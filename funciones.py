from variables import *

def mostrar_tablero(tablero_real, tablero_visible, es_jugador=True):
    """
    - `es_jugador=True`: Muestra el tablero del jugador con sus barcos y los disparos recibidos.
    - `es_jugador=False`: Muestra el tablero del enemigo con solo los impactos realizados por el jugador.
    """
    espaciado = 3
    tabla_lista = []

    # Encabezado de columnas
    encabezado = ["   "] + [f"{i:>{espaciado}}" for i in range(tamanio)]
    tabla_lista.append(" ".join(encabezado))
    tabla_lista.append("  " + "-" * (espaciado * tamanio + tamanio))

    # Contenido del tablero
    for i in range(tamanio):
        fila_lista = [f"{i:<2} |"]
        for j in range(tamanio):
            if es_jugador:
                # Tablero del jugador (mostrar barcos y disparos de la máquina)
                if tablero_real[i][j] == "B" and tablero_visible[i][j] != "X":  # Barco intacto
                    fila_lista.append(" B |")
                else:
                    fila_lista.append(f" {tablero_visible[i][j]} |")  # Impactos visibles en el tablero
            else:
                # Tablero del enemigo (solo mostrar disparos hechos por el jugador)
                if tablero_visible[i][j] in ("X", "O"):
                    fila_lista.append(f" {tablero_visible[i][j]} |")
                else:
                    fila_lista.append(" . |")
        tabla_lista.append("".join(fila_lista))
        tabla_lista.append("  " + "-" * (espaciado * tamanio + tamanio))

    # Imprimir el tablero en la consola
    print("\n".join(tabla_lista))

def jugar_turno(jugador, enemigo):
    turno_extra = jugador.disparar(enemigo)
    
    print("\nTu tablero (con barcos y disparos recibidos):")
    mostrar_tablero(jugador.tablero.tablero_real, jugador.tablero.tablero_visible, es_jugador=True)

    print("\nTablero de disparos del jugador (dónde has disparado en el enemigo):")
    mostrar_tablero(enemigo.tablero.tablero_real, enemigo.tablero.tablero_visible, es_jugador=False)

    if turno_extra:
        print("¡Acertaste! Puedes disparar de nuevo.")
    else:
        print("Fallaste.")
    
    return turno_extra
