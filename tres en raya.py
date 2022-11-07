"""
Juego de Tres en Raya Aleatorio
Fecha: 07/11/2022
Autor: Oscar Gonzalez Lujan
"""
# Posibles variantes:
# -5 en raya
# -3 en raya inverso
# -notakto
# -3 en raya de turno aleatorio
# -cuadrado mágico (pares vs impares)
# -Jugador 2 automático
# -Jugador 1 y 2 automáticos
# -Simulación N partidas automáticas y estadística
import random
import time

def bienvenida():
    print("\t**************************************************")
    print("\t********Juego del Tres en Raya Aleatorio 1DAW*******")
    print("\t**************************************************")
    return

def presentacionJugadores():
    jugador1Nombre = input("Jugador 1, ¿cuál es tu nombre?: ")
    time.sleep(0.25)
    ficha1 = input(f"{jugador1Nombre}, ¿qué ficha eliges? (X/O): ")
    time.sleep(1)
    jugador2Nombre = input("Jugador 2, ¿cuál es tu nombre?: ")
    time.sleep(0.25)
    if ficha1 == 'X': ficha2 = 'O' 
    else: ficha2 = 'X'
    print(f"{jugador2Nombre}, tu ficha es {ficha2}")
    return jugador1Nombre, jugador2Nombre, ficha1, ficha2

def pintarTablero(tablero):
    print()
    print("\t##################################################")
    print("\t##\t \t##\t \t##\t \t##")
    print(f"\t##\t{tablero[0]}\t##\t{tablero[1]}\t##\t{tablero[2]}\t##")
    print("\t##\t \t##\t \t##\t \t##")
    print("\t##################################################")
    print("\t##\t \t##\t \t##\t \t##")
    print(f"\t##\t{tablero[3]}\t##\t{tablero[4]}\t##\t{tablero[5]}\t##")
    print("\t##\t \t##\t \t##\t \t##")
    print("\t##################################################")
    print("\t##\t \t##\t \t##\t \t##")
    print(f"\t##\t{tablero[6]}\t##\t{tablero[7]}\t##\t{tablero[8]}\t##")
    print("\t##\t \t##\t \t##\t \t##")
    print("\t##################################################")
    print()
    return

def hacerJugada (jugador):
    while True:
        posicion = int(input(f"{jugador}, ¿dónde quieres poner ficha? [0-8]: "))
        if tablero[posicion] == '' :
            return posicion
        else:
            print("Casilla ocupada!\n")

def comprobarPartida(ficha1):
    # Compruebo líneas horizontales
    if tablero[0] == ficha1 and tablero[1] == ficha1 and tablero[2] == ficha1:
        return True
    elif tablero[3] == ficha1 and tablero[4] == ficha1 and tablero[5] == ficha1:
        return True
    elif tablero[6] == ficha1 and tablero[7] == ficha1 and tablero[8] == ficha1:
        return True
    # Compruebo líneas verticales
    elif tablero[0] == ficha1 and tablero[3] == ficha1 and tablero[6] == ficha1:
        return True
    elif tablero[1] == ficha1 and tablero[4] == ficha1 and tablero[7] == ficha1:
        return True
    elif tablero[2] == ficha1 and tablero[5] == ficha1 and tablero[8] == ficha1:
        return True
    # Compruebo líneas diagonales
    elif tablero[0] == ficha1 and tablero[4] == ficha1 and tablero[8] == ficha1:
        return True
    elif tablero[2] == ficha1 and tablero[4] == ficha1 and tablero[6] == ficha1:
        return True
    else:
        return False

#Secuencia principal de programas
bienvenida()
tablero = ['']*9
pintarTablero(tablero)
time.sleep(1)

jugador1Nombre, jugador2Nombre, ficha1, ficha2 = presentacionJugadores()
time.sleep(1)
time.sleep(1)

# Sólo para debug
# jugador1Nombre, jugador2Nombre, ficha1, ficha2 = 'Albert', 'Oscar', 'X', 'O'

# Bucle principal
ganador = False
pintarTablero(tablero)
while True:
    time.sleep(1)
    jugada = random.choice([jugador1Nombre, jugador2Nombre])
    #Turno jugador 1
    if jugada == jugador1Nombre:
        posicion = hacerJugada(jugador1Nombre)
        tablero[posicion] = ficha1
        time.sleep(0.25)
        pintarTablero(tablero)
        time.sleep(1)
        ganador = comprobarPartida(ficha1)
        if ganador: 
            print(f"\nFelicidades {jugador1Nombre}!!! Has ganado la partida")
            break
    #Turno jugador 2
    else:
        posicion = hacerJugada(jugador2Nombre)
        tablero[posicion] = ficha2
        time.sleep(0.25)
        pintarTablero(tablero)
        time.sleep(0.25)
        ganador = comprobarPartida(ficha2)
        if ganador: 
            print(f"\Felicidades {jugador2Nombre}!!! Has ganado la partida")
            break


"""
Juego de Tres en Raya
Fecha: 07/11/2022
Autor: Oscar Gonzalez Lujan
"""
import random
import time

def bienvenida():
    print("\t**************************************************")
    print("\t********Bienvenido al Tres en Raya aleatorio by 1ºDAW*******")
    print("\t**************************************************")
    return

def presentacionJugadores():
    jugador1Nombre = input("Jugador 1, ¿cuál es tu nombre?: ")
    time.sleep(0.25)
    ficha1 = input(f"{jugador1Nombre}, ¿qué ficha eliges? (X/O): ")
    time.sleep(1)
    jugador2Nombre = input("Jugador 2, ¿cuál es tu nombre?: ")
    time.sleep(0.25)
    if ficha1 == 'X': ficha2 = 'O' 
    else: ficha2 = 'X'
    print(f"{jugador2Nombre}, tu ficha es {ficha2}")
    return jugador1Nombre, jugador2Nombre, ficha1, ficha2

def pintarTablero(tablero):
    print()
    print("\t##################################################")
    print("\t##\t \t##\t \t##\t \t##")
    print(f"\t##\t{tablero[0]}\t##\t{tablero[1]}\t##\t{tablero[2]}\t##")
    print("\t##\t \t##\t \t##\t \t##")
    print("\t##################################################")
    print("\t##\t \t##\t \t##\t \t##")
    print(f"\t##\t{tablero[3]}\t##\t{tablero[4]}\t##\t{tablero[5]}\t##")
    print("\t##\t \t##\t \t##\t \t##")
    print("\t##################################################")
    print("\t##\t \t##\t \t##\t \t##")
    print(f"\t##\t{tablero[6]}\t##\t{tablero[7]}\t##\t{tablero[8]}\t##")
    print("\t##\t \t##\t \t##\t \t##")
    print("\t##################################################")
    print()
    return

def hacerJugada (jugador):
    while True:
        posicion = int(input(f"{jugador}, ¿dónde quieres poner ficha? [0-8]: "))
        if tablero[posicion] == '' :
            return posicion
        else:
            print("Casilla ocupada!\n")

def comprobarPartida(ficha1):
    # Compruebo líneas horizontales
    if tablero[0] == ficha1 and tablero[1] == ficha1 and tablero[2] == ficha1:
        return True
    elif tablero[3] == ficha1 and tablero[4] == ficha1 and tablero[5] == ficha1:
        return True
    elif tablero[6] == ficha1 and tablero[7] == ficha1 and tablero[8] == ficha1:
        return True
    # Compruebo líneas verticales
    elif tablero[0] == ficha1 and tablero[3] == ficha1 and tablero[6] == ficha1:
        return True
    elif tablero[1] == ficha1 and tablero[4] == ficha1 and tablero[7] == ficha1:
        return True
    elif tablero[2] == ficha1 and tablero[5] == ficha1 and tablero[8] == ficha1:
        return True
    # Compruebo líneas diagonales
    elif tablero[0] == ficha1 and tablero[4] == ficha1 and tablero[8] == ficha1:
        return True
    elif tablero[2] == ficha1 and tablero[4] == ficha1 and tablero[6] == ficha1:
        return True
    else:
        return False

#Secuencia principal de programas
bienvenida()
tablero = ['']*9
pintarTablero(tablero)
time.sleep(1)

jugador1Nombre, jugador2Nombre, ficha1, ficha2 = presentacionJugadores()
time.sleep(1)
time.sleep(1)

# Sólo para debug
# jugador1Nombre, jugador2Nombre, ficha1, ficha2 = 'Albert', 'Oscar', 'X', 'O'

# Bucle principal
ganador = False
pintarTablero(tablero)
while True:
    time.sleep(1)
    jugada = random.choice([jugador1Nombre, jugador2Nombre])
    #Turno jugador 1
    if jugada == jugador1Nombre:
        posicion = hacerJugada(jugador1Nombre)
        tablero[posicion] = ficha1
        time.sleep(0.25)
        pintarTablero(tablero)
        time.sleep(1)
        ganador = comprobarPartida(ficha1)
        if ganador: 
            print(f"\nFelicidades {jugador1Nombre}!!! Has ganado la partida")
            break
    #Turno jugador 2
    else:
        posicion = hacerJugada(jugador2Nombre)
        tablero[posicion] = ficha2
        time.sleep(0.25)
        pintarTablero(tablero)
        time.sleep(0.25)
        ganador = comprobarPartida(ficha2)
        if ganador: 
            print(f"\Felicidades {jugador2Nombre}!!! Has ganado la partida")
            break