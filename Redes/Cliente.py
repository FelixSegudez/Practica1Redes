#!/usr/bin python3

import socket, os

import socket, os


def Jugada():
    while True:

        tablero()

        f = input("fila   : ")

        try:
            f = int(f)
        except ValueError:
            tablero()
            f = input("fila   : ")

        if f <= 3:
            break

    while True:
        tablero()
        c = input("Colmna   : ")

        try:
            c = int(c)
        except ValueError:
            tablero()
            print("fila    :", f)
            c = input("Columna   : ")

        if c <= 3:
            break

    return 3 * (int(f) - 1) + (int(c) - 1)


def tablero():
    #os.system("cls")
    print("                    ")
    print("     1   2   3      ")
    print("   +---+---+---+    ")
    print("1  | %c | %c | %c | " % (M[0], M[1], M[2]))
    print("   +---+---+---+    ")
    print("2  | %c | %c | %c | " % (M[3], M[4], M[5]))
    print("   +---+---+---+    ")
    print("3  | %c | %c | %c | " % (M[6], M[7], M[8]))
    print("   +---+---+---+    ")
    print("                    ")


M = ['#', '#', '#', '#', '#', '#', '#', '#', '#']
end = False

HOST = "192.168.64.5"  # Hostname o  dirección IP del servidor
PORT = 65432  # Puerto del servidor
buffer_size = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
    TCPClientSocket.connect((HOST, PORT))

    TCPClientSocket.send(bytes("juguemos",'utf-8'))

    # Creamos un bucle para mantener la conexion
    while True:

        p = Jugada()
        while True:

            if M[p] != 'X' and M[p] != 'O':

                break
            else:
                tablero()
                p = Jugada()

        M[p] = 'X'
        tablero()
        P=str(p)
        TCPClientSocket.send(bytes(P,'utf-8'))

        while True:
            if (M[0] == "X" and M[1] == "X" and M[2] == "X"):
                print("\n\nGane")
                end = True
                break
            elif (M[3] == "X" and M[4] == "X" and M[5] == "X"):
                print("\nGane")
                end = True
                break
            elif (M[6] == "X" and M[7] == "X" and M[8] == "X"):
                print("\nGane")
                end = True
                break
            elif (M[0] == "X" and M[3] == "X" and M[6] == "X"):
                print("\nGane")
                end = True
                break
            elif (M[1] == "X" and M[4] == "X" and M[7] == "X"):
                print("\nGane")
                end = True
                break
            elif (M[2] == "X" and M[5] == "X" and M[8] == "X"):
                print("\nGane")
                end = True
                break
            elif (M[0] == "X" and M[4] == "X" and M[8] == "X"):
                print("\nGane")
                end = True
                break
            elif (M[2] == "X" and M[4] == "X" and M[6] == "X"):
                print("\nGane")
                end = True
                break
            else:
                break

        if end == True:
            break

        p = int(TCPClientSocket.recv(2))
        print("indice recibido = ", p, "\n")
        M[p] = 'O'

        while True:
            if (M[0] == "O" and M[1] == "O" and M[2] == "O"):
                print("\n\nPerdi")
                break
            elif (M[3] == "O" and M[4] == "O" and M[5] == "O"):
                print("\nPerdi")
                break
            elif (M[6] == "O" and M[7] == "O" and M[8] == "O"):
                print("\nPerdi")
                break
            elif (M[0] == "O" and M[3] == "O" and M[6] == "O"):
                print("\nPerdi")
                break
            elif (M[1] == "O" and M[4] == "O" and M[7] == "O"):
                print("\nPerdi")
                break
            elif (M[2] == "O" and M[5] == "O" and M[8] == "O"):
                print("\nPerdi")
                break
            elif (M[0] == "O" and M[4] == "O" and M[8] == "O"):
                print("\nPerdi")
                break
            elif (M[2] == "O" and M[4] == "O" and M[6] == "O"):
                print("\nPerdi")
                break
            else:
                break

    print("\nel juego ha terminado")
    TCPClientSocket.close()
