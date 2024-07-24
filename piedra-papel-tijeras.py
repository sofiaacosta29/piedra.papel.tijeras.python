nombre1 = input("¿Cómo se llamará el jugador 1?")
nombre2 = input("¿Cómo se llamará el jugador 2?")

jugador1 = input("¡Hola jugador1! ¿Qué eliges? ¿Piedra, papel o tijeras?")
jugador2 = input("¡Hola jugador2! ¿Qué eliges? ¿Piedra, papel o tijeras?")

if jugador1 == jugador2:
    print("¡Ha sido un empate!")
elif (jugador1 == "piedra" and jugador2 == "tijeras") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijeras" and jugador2 == "papel"):
    print("Ha ganado el jugador 1")
else:
    print("Ha ganado el jugador 2")