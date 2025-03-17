from clases import *
from variables import *
from funciones import *

def jugar():
    print("\n\n🚢💥 ¡Bienvenido a Hundir la Flota! 💥🚢\n")

    # Crear jugadores
    jugador = Jugador("Jugador")
    maquina = Jugador("Máquina", es_maquina=True)

    # Colocar barcos
    print("\n🚢 Colocando barcos del jugador...")
    jugador.colocar_barcos()
    
    print("\n🤖 Colocando barcos de la máquina...")
    maquina.colocar_barcos()

    turno_jugador = True  # Empieza el jugador

    while not jugador.derrotado() and not maquina.derrotado():
        print("\n\n=== TABLEROS ===")

        # Tablero del jugador con impactos recibidos
        print("\n🛡️ Tu tablero:")
        mostrar_tablero(jugador.tablero.tablero_real, jugador.tablero.tablero_visible, es_jugador=True)

        # Tablero de los disparos del jugador en la máquina
        print("\n🎯 Tablero de ataques:")
        mostrar_tablero(maquina.tablero.tablero_real, maquina.tablero.tablero_visible, es_jugador=False)

        if jugador.derrotado():
            print("\n💀 La máquina ha destruido todos tus barcos. ¡Has perdido! 💀")
            return
        if maquina.derrotado():
            print("\n🏆 ¡Felicidades! Has destruido todos los barcos de la máquina. ¡Has ganado! 🎉")
            return

        while turno_jugador:
            print("\n🎯 Tu turno:")
            if not jugar_turno(jugador, maquina):
                turno_jugador = False  # Si falla, cede el turno
            if maquina.derrotado():
                print("\n🏆 ¡Felicidades! Has destruido todos los barcos de la máquina. ¡Has ganado! 🎉")
                return

        while not turno_jugador:
            print("\n🤖 Turno de la máquina:")
            if not jugar_turno(maquina, jugador):
                turno_jugador = True  # Si falla, cede el turno
            if jugador.derrotado():
                print("\n💀 La máquina ha destruido todos tus barcos. ¡Has perdido! 💀")
                return

jugar()