import random

def dibujarTablero(tablero):
    print('   |   |')
    print(' ' + tablero[7] + ' | ' + tablero[8] + ' | ' + tablero[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + tablero[4] + ' | ' + tablero[5] + ' | ' + tablero[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + tablero[1] + ' | ' + tablero[2] + ' | ' + tablero[3])
    print('   |   |')

def ingresaLetraJugador():
    # Permite al jugador tipear que letra desea ser.
    letra = ''
    while not (letra == 'X' or letra == 'O'):
        print('¿Deseas ser X o O?')
        letra = input().upper()

       # el primer elemento de la lista es la letra del jugador, el segundo es la letra de la computadora.
    if letra == ' ':
        return ['X', 'O']
    else:
        return ['O', 'X']

def quienComienza():
       if random.randint(0, 1) == 0:
           return 'La computadora'
       else:
           return 'El jugador'

def jugarDeNuevo():
    # Esta funcion devuelve True (Verdadero) si el jugador desea volver a jugar, de lo contrario devuelve False (Falso).
    print('¿Deseas volver a jugar? (sí/no)?')
    return input().lower().startswith('s')

def hacerJugada(tablero, letra, jugada):
    tablero[jugada] = letra

def esGanador(t, l):
    #Dado un tablero y la letra de un jugador, devuelve True (verdadero) si el mismo ha ganado.
    #t = tablero y l = letra.
    return ((t[7] == l and t[8] == l and t[9] == l) or  #horizontal superior
            (t[4] == l and t[5] == l and t[6] == l) or  # horizontal medio
            (t[1] == l and t[2] == l and t[3] == l) or  # horizontal inferior
            (t[7] == l and t[4] == l and t[1] == l) or  # vertical izquierda
            (t[8] == l and t[5] == l and t[2] == l) or  # vertical medio
            (t[9] == l and t[6] == l and t[3] == l) or  # vertical derecha
            (t[7] == l and t[5] == l and t[3] == l) or  # diagonal
            (t[9] == l and t[5] == l and t[1] == l))  # diagonal


def obtenerDuplicadoTablero(tablero):
     #Construye una copia del tablero original y devuelve una referencia al nuevo tablero.
     #La lista dupTablero está vacía, el bucle for recorre tablero agregando una copia de los valores del original al duplicado, luego devuelve dupTablero
     dupTablero = []

     for i in tablero:
         dupTablero.append(i)

     return dupTablero

def hayEspacioLibre(tablero, jugada):
    # Devuelte true si hay espacio para la jugada en el tablero.
    # Si el elemento en el índice no es un espacio simple, está ocupado y no es una jugada válida
    return tablero[jugada] == ' '

def obtenerJugadaJugador(tablero):
    # Permite al jugador escribir el número del espacio.
    jugada = ' '
    while jugada not in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] or not hayEspacioLibre(tablero, int(jugada)):
        # la primera comprueba si la jugada va del 1 al 9.
        # la segunda comprueba que la jugada entró en un espacio libre llamando a hayEspacioLibre() que devolverá true
        # los operadores not se agregan a ambos lados de modo que será true cuando cualquiera de los dos deje de cumplirse y
        # de esta manera el bucle seguirá pidiendo al jugador que ingrese una jugada valida.
        print('¿Cuál es tu próxima jugada? (1-9)')
        jugada = input() #input devuelve cadena
    return int(jugada)  #ponemos int para que nos devuelva un entero de esa cadena

def elegirAzarDeLista(tablero, listaJugada):
    # Devuelve una jugada válida en el tablero de la lista recibida.
    # Devuelve None si no hay ninguna jugada válida.
    jugadasPosibles = []
    for i in listaJugada:
        if hayEspacioLibre(tablero, i):
          jugadasPosibles.append(i)

    # listaJugada es una lista de enteros con posibles espacios para elegir.
    # elegirAzarDeLista comprobará primero que es válido hacer una jugada en un espacio y luego devolver un entero de los posibles.
    # JugadasPosibles comienza como una lista vacía, el bucle for itera sobre listaJugada, las jugadas
    # para las que hayEspacioLibre devuelven true y entonces se agregan a jugadasPosibles mediante append

    if len(jugadasPosibles) != 0:
        return random.choice(jugadasPosibles)
    else:
        return None
    # en jugadasPosibles están todas las jugadas que estaban en la listaJugada y tambien son espacios libres.
    # Si la lista no está vacía es porque hay al menos un espacio libre.


def obtenerJugadaComputadora(tablero, letraComputadora):
    # Dado un tablero y la letra de la computadora, determina que jugada efectuar.
      if letraComputadora == 'X':
          letraJugador = 'O'
      else:
          letraJugador = 'X'

     # Primero, verifica si podemos ganar en la próxima jugada
      for i in range(1, 10):
         copia = obtenerDuplicadoTablero(tablero)
         if hayEspacioLibre(copia, i):
             hacerJugada(copia, letraComputadora, i)
             if esGanador(copia, letraComputadora):
                 return i

     # Verifica si el jugador podría ganar en su próxima jugada, y lo bloquea.
      for i in range(1, 10):
         copia = obtenerDuplicadoTablero(tablero)
         if hayEspacioLibre(copia, i):
             hacerJugada(copia, letraJugador, i)
             if esGanador(copia, letraJugador):
                 return i

     # Intenta ocupar una de las esquinas de estar libre.
         jugada = elegirAzarDeLista(tablero, [1, 3, 7, 9])
         if jugada != None:
            return jugada

      # Intenta ocupar el centro.
         if hayEspacioLibre(tablero, 5):
            return 5

      # Ocupa alguno de los lados.
            return elegirAzarDeLista(tablero, [2, 4, 6, 8])


def tableroCompleto(tablero):
    # Devuelve True si cada espacio del tablero fue ocupado, caso contrario devuele False.
    for i in range(1, 10):
        if hayEspacioLibre(tablero, i):
            return False
    return True


print('¡Bienvenido al Ta Te Ti!')

while True:
    # Resetea el tablero
    elTablero = [' '] * 10
    letraJugador, letraComputadora = ingresaLetraJugador()
    turno = quienComienza()
    print(turno + ' irá primero.')
    juegoEnCurso = True

    while juegoEnCurso:
        if turno == 'El jugador':
            # Turno del jugador
            dibujarTablero(elTablero)
            jugada = obtenerJugadaJugador(elTablero)
            hacerJugada(elTablero, letraJugador, jugada)

            if esGanador(elTablero, letraJugador):
                dibujarTablero(elTablero)
                print('¡Felicidades, has ganado!')
                juegoEnCurso = False
            else:
                if tableroCompleto(elTablero):
                    dibujarTablero(elTablero)
                    print('¡Es un empate!')
                    break
                else:
                    turno = 'La computadora'

        else:
            # Turno de la computadora
            jugada = obtenerJugadaComputadora(elTablero, letraComputadora)
            hacerJugada(elTablero, letraComputadora, jugada)

            if esGanador(elTablero, letraComputadora):
                dibujarTablero(elTablero)
                print('¡La computadora te ha vencido! Has perdido.')
                juegoEnCurso = False
            else:
                if tableroCompleto(elTablero):
                    dibujarTablero(elTablero)
                    print('¡Es un empate!')
                    break
                else:
                   turno = 'El jugador'

    if not jugarDeNuevo():
        break
