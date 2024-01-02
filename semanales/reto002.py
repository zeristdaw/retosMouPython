'''
/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 *
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
 */
'''

jugador1 = ""
jugador2 = ""

contador1 = 0
contador2 = 0

secuencia = ["p1" ,"p1" ,"p2" ,"p2" ,"p1" ,"p2" ,"p1" ,"p1"]

for i in secuencia:

    if i == "p1":
        contador1 = contador1 + 1
    if i == "p2":
        contador2 = contador2 + 1

    if contador1 == 0:
        jugador1 = "love"
    if contador1 == 1:
        jugador1 = "15"
    if contador1 == 2:
        jugador1 = "30"

    if contador2 == 0:
        jugador2 = "love"
    if contador2 == 1:
        jugador2 = "15"
    if contador2 == 2:
        jugador2 = "30"

    if contador1 >= 3 and contador1 == contador2:
        jugador1 = "Deuce"
        jugador2 = ""
    if contador1 == 3 and contador2 < 3:
        jugador1 = "40"
    if contador2 == 3 and contador1 < 3:
        jugador2 = "40"

    if contador1 > 3 and contador1 == contador2 + 1:
        jugador1 = "Ventaja jugador1"
    if contador1 > 3 and contador1 == contador2 + 2:
        jugador1 = "Victoria jugador1"

    if contador2 > 3 and contador2 == contador1 + 1:
        jugador1 = "Ventaja jugador2"
    if contador2 > 3 and contador2 == contador1 + 2:
        jugador1 = "Victoria jugador2"

    if jugador1 == "Deuce" or jugador1 == "Ventaja jugador1" or jugador1 == "Victoria jugador1" or jugador1 == "Ventaja jugador2" or jugador1 == "Victoria jugador2":
        print(f'{jugador1}')
    else:
        print(f'{jugador1} - {jugador2}')

