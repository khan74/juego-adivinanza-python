# Piedra, papel o tijeras

turnos_maximos = 3
turno = 1
puntos_jugador1 = 0
puntos_jugador2 = 0
jugador1 = 'string'
jugador2 = 'string'

nombre1 = input('¿Como se llamará el jugador 1?: ')
nombre2 = input('¿Como se llamará el jugador 2?: ')

txt = 'Turno {0}! {1}, que eliges? ¿Piedra, papel o tijeras?: '

while turno <= turnos_maximos:
    jugador1 = input(txt.format(turno,nombre1)).lower()
    jugador2 = input(txt.format(turno,nombre2)).lower()

    condicion1 = (jugador1 == "piedra" and jugador2 == "tijera")
    condicion2 = (jugador1 == 'papel' and jugador2 == 'piedra')
    condicion3 = (jugador1 == 'tijera' and jugador2 == 'papel')    
    
    if jugador1 == jugador2:
        print("¡EMPATE!")
    elif condicion1 or condicion2 or condicion3:
        print(nombre1, 'suma un punto!')
        puntos_jugador1 += 1
    else:
        print(nombre2, 'suma un punto!')
        puntos_jugador2 += 1
    turno += 1

if puntos_jugador1 == puntos_jugador2:
    print("¡EMPATE!, ambos jugadores tienen ", puntos_jugador1, 'puntos')
elif puntos_jugador1 > puntos_jugador2:
    print('Ha ganado ', nombre1, 'con ', puntos_jugador1, 'puntos' )
else:
    print('Ha ganado ', nombre2, 'con ', puntos_jugador2, 'puntos' )

input('El juego ha terminado, presiona ENTER para salir')