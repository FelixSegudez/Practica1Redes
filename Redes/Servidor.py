#!/usr/bin python3
import socket

from random import randrange


M = ['#','#','#','#','#','#','#','#','#']

HOST = "127.0.0.1"  # Direccion de la interfaz de loopback estándar (localhost)
PORT = 65432  # Puerto que usa el cliente  (los puertos sin provilegios son > 1023)
buffer_size = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPServerSocket:
    TCPServerSocket.bind((HOST, PORT))


    TCPServerSocket.listen()
    print("El servidor TCP está disponible y en espera de solicitudes")

    sc, addr = TCPServerSocket.accept()
    mensaje = sc.recv(10)
    if mensaje == "juguemos":
        print("jugando con cliente ", addr[0])

    apagar = False
    while True:
        # El metodo recv recibe tantos bytes como le indiquemos
        p = int(sc.recv(2))
        print("indice recibido = ", p)

        if p == 9:
            break

        M[p] = 'X'

        while True:
            if (M[0] == "X" and M[1] == "X" and M[2] == "X"):
                print("\n\nPerdi")
                apagar = True
                break
            elif (M[3] == "X" and M[4] == "X" and M[5] == "X"):
                print("\nPerdi")
                apagar = True
                break
            elif (M[6] == "X" and M[7] == "X" and M[8] == "X"):
                print("\nPerdi")
                apagar = True
                break
            elif (M[0] == "X" and M[3] == "X" and M[6] == "X"):
                print("\nPerdi")
                apagar = True
                break
            elif (M[1] == "X" and M[4] == "X" and M[7] == "X"):
                print("\nPerdi")
                apagar = True
                break
            elif (M[2] == "X" and M[5] == "X" and M[8] == "X"):
                print("\nPerdi")
                apagar = True
                break
            elif (M[0] == "X" and M[4] == "X" and M[8] == "X"):
                print("\nPerdi")
                apagar = True
                break
            elif (M[2] == "X" and M[4] == "X" and M[6] == "X"):
                print("\nPerdi")
                apagar = True
                break
            else:
                break
        if apagar == True:
            break

        while True:
            k = randrange(0, 9)
            if M[k] == '#':
                M[k] = 'O'
                break

        print("indice enviado = ", k, "\n")
        # El servidor le responde al cliente
        sc.send(str(k))

        while True:
            if (M[0] == "O" and M[1] == "O" and M[2] == "O"):
                print("\n\nGane")
                apagar = True
                break
            elif (M[3] == "O" and M[4] == "O" and M[5] == "O"):
                print("\nGane")
                apagar = True
                break
            elif (M[6] == "O" and M[7] == "O" and M[8] == "O"):
                print("\nGane")
                apagar = True
                break
            elif (M[0] == "O" and M[3] == "O" and M[6] == "O"):
                print("\nGane")
                apagar = True
                break
            elif (M[1] == "O" and M[4] == "O" and M[7] == "O"):
                print("\nGane")
                apagar = True
                break
            elif (M[2] == "O" and M[5] == "O" and M[8] == "O"):
                print("\nGane")
                apagar = True
                break
            elif (M[0] == "O" and M[4] == "O" and M[8] == "O"):
                print("\nGane")
                apagar = True
                break
            elif (M[2] == "O" and M[4] == "O" and M[6] == "O"):
                print("\nGane")
                apagar = True
                break
            else:
                break

        if apagar == True:
            break
    print("\n\nel juego ha terminado")

    # Cerramos la instancia del socket cliente y servidor
    sc.close()
    TCPServerSocket.close()