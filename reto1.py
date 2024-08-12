#Realiza un programa en donde dos jugadores puedan jugar Piedra, Papel o Tijeras

jugador1 = input("Jugador 1, Escoge Piedra, Papel o Tijera: ").lower()
jugador2 = input("Jugador 2, Escoge Piedra, Papel o Tijera: ").lower()


winner_player1 = f"Jugador 1 GANA, {jugador1.capitalize()} gana a {jugador2.capitalize()}"
winner_player2 = f"Jugador 2 GANA, {jugador2.capitalize()} gana a {jugador1.capitalize()}"
draw_players = f"Esto es un empate, ambos jugadores escogieron: {jugador1.capitalize()}"


if jugador1 == jugador2:
    print(draw_players)
elif (jugador1 == "piedra" and jugador2 == "tijera") or \
     (jugador1 == "papel" and jugador2 == "piedra") or \
     (jugador1 == "tijera" and jugador2 == "papel"):
    print(winner_player1)
else:
    print(winner_player2)
