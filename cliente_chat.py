#!/usr/bin/env python

import socket


clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Crear el socket

clientsocket.connect(('10.108.33.32',8080)) #Se conecta al servidor (IP,puerto)

#Entra en el bucle si está conectado
while 1:
        data = str.encode(input('>')) #Escribimos mensaje
        clientsocket.send(data)  #Se envía al servidor
        if not data or data == str.encode("salir"): break  #Si no hay mensaje (no envía)
        newdata = clientsocket.recv(1024).decode()  #Recibe la respuesta del servidor
        if newdata == "salir": break
        print ('Servidor dice: ', newdata) #Imprime la respuesta

clientsocket.close()  #Cierra el socket
